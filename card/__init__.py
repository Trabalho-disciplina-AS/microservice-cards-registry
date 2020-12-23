from flask import Flask
from flask_restful import Api
from flask_mongoengine import MongoEngine
from flask_cors import CORS


app = Flask(__name__)
app.config["MONGODB_SETTINGS"] = {
    "db": "cards",
    "host": "mongodb+srv://adrilene:arq2201@cluster0.a3msk.mongodb.net/test?authSource=admin&replicaSet=atlas-2nqljv-shard-0&readPreference=primary&appname=MongoDB%20Compass&ssl=true"
}



db = MongoEngine(app)
api = Api(app)
CORS(app)
# cors = CORS(app, resources={r"/purchase_item": {"origins": "*"}})

# CORS(app, resources={r"/purchase_item/item/*": {"origins": "*"}})
# CORS(app, resources={r"/purchase_item/user/*": {"origins": "*"}})
# CORS(app, resources={r"/purchase_item": {"origins": "*"}})

from .models import card_model
from .services import card_service
from .controllers import card_controller
