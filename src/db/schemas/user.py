
def user_schema(user) -> dict:
    return {'id': str(user['_id']),
            'username': user['username'],
            'email': user['email'],
            'full_name': user['full_name'],
            'disabled': user['disabled']
            }


def userdb_schema(userdb) -> dict:
    return {'id': str(userdb['_id']),
            'username': userdb['username'],
            'email': userdb['email'],
            'full_name': userdb['full_name'],
            'disabled': userdb['disabled'],
            'hashed_password': userdb['hashed_password']
            }


def users_schema(users) -> list:
    return [user_schema(user) for user in users]
