import random
import string

def create_new_food(data):
    food_id = generate_random_id()
    food = {
        'id': food_id,
        'food_type': data['food_type'],
        'food_name': data['food_name']
    }
    return food

def generate_random_id():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=10))
