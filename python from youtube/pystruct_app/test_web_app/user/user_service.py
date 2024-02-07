
users = [] # dummy list to store users

def create_user(username,email):
    # raise Exception('manually created throw error')
    if not username or not email:
        return {
            'isSuccess': False,
            'message': 'Username and email are required',
            'http_status': 400
        }
    newUser = {
        'username': username,
        'email': email,
    }
    users.append(newUser)
    
    return {
        'isSuccess': True,
        'message': 'User created successfully',
        'http_status': 201,
        'data': newUser
    }