from config.database import db
from datetime import datetime
from . import sql_utils

class People(db.Model): 
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150),)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.Text())
    date_joined = db.Column(db.Date,default=datetime.utcnow)
    pets = db.relationship('Pet', backref='people') # keep refrence of Pet collection

    # print string representation
    def __repr__(self):
        return f"User(id={self.id},email={self.email},name={self.name},date_joined={self.date_joined})"
    
    # convert to dictionary 
    def to_dict_MYTILS(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'password': self.password,
            'date_joined': self.date_joined,
        }
    
    # add and commit to db
    def to_add_and_commit_session(self):
        db.session.add(self)
        db.session.commit()

    # delete and commit to db
    def to_delete_and_commit_session(self):
        db.session.delete(self)
        db.session.commit()
    
    def set_hashed_password_myModelTils(self,plain_password):
        self.password = sql_utils.make_password_hash(plain_password)
    
