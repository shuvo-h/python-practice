from config.database import db

class Pet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20),)
    age = db.Column(db.Integer)
    owner_id = db.Column(db.Integer, db.ForeignKey('people.id'))    # keep reference of foreign key of id of People class

     # define relationship with People
    owner = db.relationship('People', back_populates='pets')
    
     # print string representation
    def __repr__(self):
        return f"Pet(id={self.id},age={self.age},name={self.name},owner_id={self.owner_id})"
    
    # convert to dictionary with populated fields
    def to_dict_MYTILS(self):
        owner_info = {
            'id': self.owner.id,
            'name': self.owner.name,
            'email': self.owner.email  # People class has an 'email' attribute
        } if self.owner else None
         
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'owner_id': self.owner_id,
            'owner': owner_info
        }