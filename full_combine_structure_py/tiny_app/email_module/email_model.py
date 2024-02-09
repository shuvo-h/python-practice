from config.database import db
from datetime import datetime

class Users(db.Model):
    id = db.Column(db.Integer,primary_key=True) 
    email = db.Column(db.String(150),unique=True)
    name = db.Column(db.String(200),nullable=False)
    # isSuccess = db.Column(db.Boolean,nullable=False,default=False)
    # date_added = db.Column(db.DateTime,default=datetime.utcnow)

    # create a string represent
    def __repr__(self):
        return f"User(id={self.id}, email='{self.email}', name='{self.name}'"
    
    # convert to dictionary
    def to_dict(self):
        return {
            'id': self.id,
            'email': self.email,
            'name': self.name,
            # 'isSuccess': self.isSuccess,
            # 'date_added': self.date_added.strftime('%Y-%m-%d %H:%M:%S')  # Format the datetime
        }
    