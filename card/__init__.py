from flask import Flask
from flask_restful import Api
from flask_mongoengine import MongoEngine
from flask_cors import CORS


app = Flask(__name__)
app.config["MONGODB_SETTINGS"] = {
    "db": "devices",
    "host": "mongodb://localhost/purchase_items",
}
db = MongoEngine(app)
api = Api(app)
CORS(app)
# cors = CORS(app, resources={r"/purchase_item": {"origins": "*"}})

# CORS(app, resources={r"/purchase_item/item/*": {"origins": "*"}})
# CORS(app, resources={r"/purchase_item/user/*": {"origins": "*"}})
# CORS(app, resources={r"/purchase_item": {"origins": "*"}})

from .models import purchase_items_model
from .services import purchase_items_service
from .controllers import purchase_items_controller
