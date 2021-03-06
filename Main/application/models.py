from application import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(id):
    return Users.query.get(int(id))

class Users(db.Model, UserMixin):
    __tablename__ = 'Users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(50), nullable=False, unique=False, autoincrement=True)
    last_name = db.Column(db.String(50), nullable=False, unique=False, autoincrement=True)
    username = db.Column(db.String(30), nullable=False, unique=True, autoincrement=True)
    email = db.Column(db.String(120), nullable=False, unique=True, autoincrement=True)
    password = db.Column(db.String(500), nullable=False, autoincrement=True)
    children = db.relationship("Characters")
    
    
    def __repr__(self):
        return ''.join(['UserID: ', str(self.id), '\r\n', 'Email: ', self.email])
    
class Characters(db.Model, UserMixin):
    __tablename__ = 'Characters'
    id = db.Column(db.Integer, primary_key=True)
    Characte_name = db.Column(db.String(50), nullable=False, unique=True)
    first_name = db.Column(db.String(50), nullable=False, unique=False)
    char_class = db.Column(db.String(30), nullable=False, unique=False)
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
    Users_id = db.Column(db.Integer, db.ForeignKey('Users.id'))
    inventory = db.relationship("Inventory", uselist=False, backref="characters")
    
    def __repr__(self):
        return ''.join(['UserID: ', str(Users.id), '\r\n', 'Character ID: ', self.id])
    
class Inventory(db.Model, UserMixin):
    __tablename__ = 'Inventory'
    id = db.Column(db.Integer, primary_key=True)
    health_potions = db.Column(db.Integer, nullable=True)
    scrolls = db.Column(db.Integer, nullable=True)
    keys = db.Column(db.Integer, nullable=True)
    arrows = db.Column(db.Integer, nullable=True)
    shortsword = db.Column(db.Integer, nullable=True)
    longsword = db.Column(db.Integer, nullable=True)
    character_id = db.Column(db.Integer, db.ForeignKey('Characters.id'))

    
    def __repr__(self):
        return ''.join(['UserID: ', str(Users.id), '\r\n', 'Inventory ID: ', self.id])