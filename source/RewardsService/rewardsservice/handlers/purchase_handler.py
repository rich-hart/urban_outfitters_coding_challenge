import json
import tornado.web

from pymongo import MongoClient
from tornado.gen import coroutine


class PurchasesHandler(tornado.web.RequestHandler):

    @coroutine
    def get(self):
        client = MongoClient("mongodb", 27017)
        db = client["Purchases"]
        purchases = list(db.purchases.find({}, {"_id": 0}))
        self.set_status(200)
        self.write(json.dumps(purchases))

    @coroutine
    def post(self):
#        import ipdb; ipdb.set_trace()
        client = MongoClient("mongodb", 27017)
        db = client["Purchases"]
        purchase = {
            'email_address': self.get_argument('email_address', ''),
            'order_total': float(self.get_argument('order_total', 0.0))
        }

        db.purchases.insert_one(purchase)

        self.set_status(201)

        purchases = list(db.purchases.find({}, {"_id": 0}))

        data = {
            'id': str(purchase['_id']),
            'email_address': purchase['email_address'],
            'order_total': purchase['order_total'],
        }

        self.write(json.dumps([data]))


