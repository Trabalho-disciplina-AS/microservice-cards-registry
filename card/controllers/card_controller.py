from flask import request, jsonify
from flask_restful import Resource
from card.services.card_service import get_card_by_user_id, insert_card, delete_card_by_id
from card import app, api
import json
import requests
import io

"""
{
    "name": "",
    "number": "",
    "cpf_credit_card": "",
    "cvv": "",
    "month": "",
    "year": "",
}
"""

"""
POST -> add card (Other Service validate)
GET -> Return all cards
"""


class CardController(Resource):
    def get(self):
        user_id = request.args.get("user_id")
        cards = get_card_by_user_id(user_id)
        cards = json.loads(cards.to_json())
        new_cards = []
        for card in cards:
            card['_id'] = card['_id']['$oid']
            new_cards.append(card)

        return new_cards, 200

    def post(self):
        data_json = {
            "user_id": request.headers.get('User-Agent'),
            "card_holder": request.json["card_holder"],
            "number": request.json["number"],
            "cpf_holder": request.json["cpf_holder"],
            "cvv": request.json["cvv"],
            "month": request.json["month"],
            "year": request.json["year"],
        }
        url = f"http://localhost:4002/validate?number={data_json['number']}&cvv={data_json['cvv']}"

        # import ipdb; ipdb.set_trace()
        response = requests.get(url)
        if response.status_code == 400: 
            return response.json(), 400


        card_id = insert_card(data_json)
        return card_id, 200

    def delete(self):
        card_id = request.args.get("card_id")
        delete_card_by_id(card_id)
        return {"msg": "success delete"}, 200

# api.add_resource(PurchaseItemUserAgentController, "/purchase_item/<user_agent>")

api.add_resource(CardController, "/card")
