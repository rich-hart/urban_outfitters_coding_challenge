from tornado.testing import (
    AsyncTestCase,
    AsyncHTTPClient,
    gen_test,
)

from pymongo import MongoClient

import json
import urllib
import unittest

from handlers.account_handler import AccountsHandler

#FIXME: Database must be manually dropped
# and tests individually run in order. 

class TestRewardsService(AsyncTestCase):

    @gen_test
    def test_GET_rewards_endpoint(self):
        client = AsyncHTTPClient(self.io_loop)
        response = yield client.fetch("http://localhost:7051/rewards")
        exprected = {
            "tier": "A",
            "points": 100,
            "rewardName": "5% off purchase",
        }
        returned = json.loads(response.body)
        self.assertIn(exprected, returned)


class TestPurchasesService(AsyncTestCase):

    @gen_test
    def test_GET_purchases_endpoint(self):
        client = AsyncHTTPClient(self.io_loop)
        response = yield client.fetch("http://localhost:7051/purchases")
        self.assertEqual(response.code,200)


    @gen_test
    def test_POST_purchases_endpoint(self):
        client = AsyncHTTPClient(self.io_loop)
        post_data = {
            'email_address': 'test@domain.com',
            'order_total': 5.0,
        }
        body = urllib.urlencode(post_data)
        response = yield client.fetch("http://localhost:7051/purchases", method='POST', headers=None, body=body)
        self.assertEqual(response.code,201)






