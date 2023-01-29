from fastapi import APIRouter, Depends, HTTPException, status
from src.db.models.user import User, UserInDB
from src.db.client import db_client
from src.db.schemas.user import user_schema, users_schema
from bson import ObjectId
from passlib.context import CryptContext

router = APIRouter(prefix='/users')


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password):
    return pwd_context.hash(password)


def get_user(key: str, value):
    try:
        user = user_schema(db_client.users.find_one({key: value}))
        return User(**user)
    except:
        return {'error': 'No se ha encontrado el usuario'}


# response_model para saber que va a devolver y ayuda con la documentacion
@router.get('/', response_model=list[User])
async def get_all():
    return users_schema(db_client.users.find())


# Pasar id por el path
@router.get('/{id}')
async def get(id: str):
    return get_user('_id', ObjectId(id))


@router.post('/', response_model=User)
async def create(user: UserInDB):
    if type(get_user('email', user.email)) == User:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='El usuario ya existe')
    elif type(get_user('username', user.username)) == User:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='El usuario ya existe')

    user.hashed_password = get_password_hash(user.hashed_password)
    user_dict = dict(user)
    # Para que no se guarde el id como un null sino que lo genere MongoDB
    del user_dict['id']
    id = db_client.users.insert_one(user_dict).inserted_id
    new_user = user_schema(db_client.users.find_one({'_id': id}))
    # Los ** se usan para desempaquetar diccionarios
    # En este caso me sirve para no pasarle un diccionario
    # al crear el User, sino pasarle los atributos
    return User(**new_user)


@router.put('/', response_model=User)
async def update(user: User):
    user_dict = dict(user)
    del user_dict['id']
    try:
        db_client.users.find_one_and_replace(
            {'_id': ObjectId(user.id)}, user_dict)
    except:
        return {'error': 'No se ha encontrado el usuario'}

    return get_user('_id', ObjectId(user.id))


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete(id: str):
    found = db_client.users.find_one_and_delete({'_id': ObjectId(id)})
    if not found:
        return {'error': 'No se ha eliminado al usuario'}
