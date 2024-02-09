import random
import string
from tiny_app.email_module.email_model import Users 
from config.database import db
from datetime import datetime

def sendSMTPemail(data):
    id = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    
    email = data['email']
    name =  data['name']

    try:
        # store the user to database 
        newUser = Users(email=email,name=name)
        db.session.add(newUser)
        db.session.commit()
        return {}
    except Exception as e:
        print(e)
        return {"msg": str(e)}
    
