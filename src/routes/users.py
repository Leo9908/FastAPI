from fastapi import APIRouter, Depends

router = APIRouter(prefix='/users')

@router.post('/create')
async def create_user():
    pass
