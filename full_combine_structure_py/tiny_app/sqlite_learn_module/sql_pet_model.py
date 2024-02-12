from config.database import db

class Pet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20),)
    age = db.Column(db.Integer)
    owner_id = db.Column(db.Integer, db.ForeignKey('people.id'))    # keep reference of foreign key of id of People class
    
