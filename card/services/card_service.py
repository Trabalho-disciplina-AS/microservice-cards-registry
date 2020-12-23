from card.models.card_model import Cards
import json
import requests


def get_card_by_user_agent(user_agent):
    return Cards.objects(user_agent=user_agent)

def insert_card(body: dict):
    card = Cards(**body)
    card.save()
    return str(card.id)

def delete_card_by_id(id):
    Cards.objects(id=id).delete()