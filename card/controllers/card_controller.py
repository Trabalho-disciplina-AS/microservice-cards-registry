from flask import request, jsonify
from flask_restful import Resource
from card import app, api
import json
import io

'''
{
    "name": "",
    "number": "",
    "cpf_credit_card": "",
    "cvv": "",
    "month": "",
    "year": "",
}
'''

'''
POST -> add card (Other Service validate)
GET -> Return all cards
'''



class CardController(Resource):
    def get(self):
        cards = get_all_cards()
        return cards, 200

    def post(self):
        # import ipdb; ipdb.set_trace()
        data_json = {
            "product_id": request.json["_id"],
            "user_agent": request.headers.get("User-Agent"),
        }
        insert_purchase_item(data_json)
        return "OK", 200

    def put(self):
        user_agent = request.headers.get("User-Agent")

        purchase_items = update_purchase_items_by_user_id(
            user_agent, request.json
        )

        return {"msg": "ok"}, 200


# api.add_resource(PurchaseItemUserAgentController, "/purchase_item/<user_agent>")

api.add_resource(PurchaseItemItemIDController, "/purchase_item/item/<item_id>")
api.add_resource(PurchaseItemUserIDController, "/purchase_item/user/<user_id>")
api.add_resource(PurchaseItemController, "/purchase_item")
