from purchase_items import db
from datetime import datetime


class Cards(db.Document):
    meta = {"collection": "cards"}
    email = db.StringField(required=False)
    name = db.StringField(required=False)
    cpf = db.StringField(required=False)
    cvv = db.StringField(required=False)
    month = db.IntField(required=False)
    year = db.IntField(required=False)
