import json
import tornado.web

from pymongo import MongoClient
from tornado.gen import coroutine


class PurchasesHandler(tornado.web.RequestHandler):

    def _update_rewards(self, email_address):
#        import ipdb; ipdb.set_trace()

        account = {
            '_id': email_address,
            'email_address': email_address,
            'reward_points': None,
            'rewards_tier': None,
            'reward_tier_name': None,
            'next_rewards_tier': None,
            'next_rewards_tier_name': None,
            'next_rewards_tier_progress': None,
        }

        client = MongoClient("mongodb", 27017)
        db = client["Rewards"]
        rewards = list(db.rewards.find({}, {"_id": 0}))
        db = client["Purchases"]
     
        purchases_total = 0.0
        for purchase in db.purchases.find({ 'email_address':email_address }):
            purchases_total += purchase['order_total']
        account['reward_points'] = int(purchases_total)
        rewards = sorted(rewards, key=lambda reward: reward['points'])
        for i in range(0,len(rewards)):
            reward = rewards[i]
            if account['reward_points'] >= reward['points']:
                account['rewards_tier'] = reward['tier']
                account['reward_tier_name'] = reward['rewardName']
                if i+1 < len(rewards):
                    next_reward = rewards[i+1]
                    account['next_rewards_tier'] = next_reward['tier']
                    account['next_rewards_tier_name'] = next_reward['rewardName']
                    percent_complete = (float(account['reward_points'] - reward['points']) / float(next_reward['points'] - reward['points']) ) * 100.0
                    account['next_rewards_tier_progress'] = percent_complete
                else:
                    account['next_rewards_tier'] = None
                    account['next_rewards_tier_name'] = None
                    account['next_rewards_tier_progress'] = None
         
        db = client["Accounts"]
        db.accounts.replace_one({ 'email_address':email_address },account, upsert=True)                                 
        return account           
                 

    @coroutine
    def get(self):
        client = MongoClient("mongodb", 27017)
        db = client["Purchases"]
        purchases = list(db.purchases.find({}, {"_id": 0}))
        self.set_status(200)
        self.write(json.dumps(purchases))

    @coroutine
    def post(self):
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

        self._update_rewards(purchase['email_address'])

        self.write(json.dumps([data]))




