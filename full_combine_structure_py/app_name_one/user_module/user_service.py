import random
import string

def create_new_user(data):
    user_id = generate_random_id()
    user = {
        'id': user_id,
        'email': data['email'],
        'name': data['name']
    }
    return user

def generate_random_id():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=10))
