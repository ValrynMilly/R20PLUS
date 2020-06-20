from application import db
from application.models import Users, Characters, Inventory

db.drop_all()
db.create_all()
