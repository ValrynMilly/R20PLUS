from application import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(id):
    return Users.query.get(int(id))

class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False, unique=True)
    last_name = db.Column(db.String(50), nullable=False, unique=True)
    username = db.Column(db.String(30), nullable=False, unique=True)
    email = db.Column(db.String(120), nullable=False, unique=True)
    password = db.Column(db.String(500), nullable=False)
    
    
    def __repr__(self):
        return ''.join(['UserID: ', str(self.id), '\r\n', 'Email: ', self.email])
    
class Characters(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    Characte_name = db.Column(db.String(50), nullable=False, unique=True)
    first_name = db.Column(db.String(50), nullable=False, unique=True)
    char_class = db.Column(db.String(30), nullable=False, unique=True)
    background = db.Column(db.String(30), nullable=False, unique=False)
    race = db.Column(db.String(30), nullable=False, unique=False)
    alignment = db.Column(db.String(30), nullable=False, unique=False)
    experience_points = db.Column(db.String(30), nullable=False, unique=False)
    strength = db.Column(db.String(30), nullable=False, unique=False)
    dexterity = db.Column(db.String(30), nullable=False, unique=False)
    constitution = db.Column(db.String(30), nullable=False, unique=False)
    intelligence = db.Column(db.String(30), nullable=False, unique=False)
    wisdom = db.Column(db.String(30), nullable=False, unique=False)
    charisma = db.Column(db.String(30), nullable=False, unique=False)
    
    def __repr__(self):
        return ''.join(['UserID: ', str(self.id), '\r\n', 'Email: ', self.email])