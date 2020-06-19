from application import db
from application.models import Users, Characters

db.drop_all()
db.create_all()