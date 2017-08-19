import json
import tornado.web

from pymongo import MongoClient
from tornado.gen import coroutine
import re

class AccountsHandler(tornado.web.RequestHandler):

    @classmethod
    def update(cls, email_address):
        account = {
            'email_address': email_address,
            'reward_points': None,
            'rewards_tier': None,
            'reward_tier_name': None,
            'next_rewards_tier': None,
            'next_rewards_tier_name': None,
            'next_rewards_tier_progress': None,
        }
        client = MongoClient("mongodb", 27017)
        db = client["Accounts"]
        cursor = db.rewards.find({}, {"_id": 0})
        return account

    @coroutine
    def get(self):
        match = re.search(r'[0-9]+', self.request.path)
        if match:
            account_id = match.group()

#        import ipdb; ipdb.set_trace()
#        match = re.search(r'[0-9]+',self.request.path):
#        if match:
#            account_id = match.group()
         

    @coroutine
    def post(self):
        pass

    @coroutine
    def put(self):
        pass

