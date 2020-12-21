from purchase_items.models.purchase_items_model import PurchaseItems, Item
import json
import requests


def get_purchase_items_by_user_id(user_id):
    return PurchaseItems.objects(user_id=user_id)


def get_purchase_items_by_user_agent(user_agent):
    return PurchaseItems.objects(user_agent=user_agent)


def update_purchase_items_by_user_id(user_agent, update_data):
    key = next(iter(update_data))
    data = {f"set__{key}": update_data[key]}
    return PurchaseItems.objects(user_agent=user_agent).update(**data)


def calculate_price(price, discount_price, discount):
    return price - discount_price if discount else price


def insert_purchase_item(body: dict):
    data_product = requests.get(
        f"http://localhost:5000/product/{body['product_id']}"
    ).json()
    # items_buy = get_purchase_items_by_user_agent(user_agent)

    # items = json.loads(items_buy.to_json())["itens"]
    # Save a new user agente
    purchase_item = PurchaseItems.objects(user_agent=body["user_agent"])
    if not purchase_item:
        PurchaseItems(user_agent=body["user_agent"]).save()

    # Construct Item
    data = {
        "id": body["product_id"],
        "qtd": 1,
        "name": data_product["name"],
        "price": calculate_price(
            data_product["price"],
            data_product["discount_price"],
            data_product["discount"],
        ),
    }
    item = Item(**data)

    # Check item in already exists purchase_item
    purchase = PurchaseItems.objects(itens__id=data["id"])
    if not purchase:
        purchase_item = PurchaseItems.objects.update_one(push__itens=item)


def delete_item_by_item_id(item_id):
    new_purchase_items = json.loads(PurchaseItems.objects(itens__id=item_id).to_json())[
        0
    ]
    del new_purchase_items["_id"]
    del new_purchase_items["created_at"]
    new_itens = [item for item in new_purchase_items["itens"] if item["id"] != item_id]
    PurchaseItems.objects(itens__id=item_id).update(set__itens=new_itens)