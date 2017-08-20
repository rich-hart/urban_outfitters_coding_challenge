import json
import tornado.web

from pymongo import MongoClient
from tornado.gen import coroutine
import re

class AccountsHandler(tornado.web.RequestHandler):


    @coroutine
    def get(self,email_address=None):
        client = MongoClient("mongodb", 27017)
        db = client["Accounts"]
        if email_address:
            key = {'email_address':email_address}
            rewards = list(db.accounts.find(key, {"_id": 0}))
        else: 
            rewards = list(db.accounts.find({}, {"_id": 0}))
        self.write(json.dumps(rewards))

