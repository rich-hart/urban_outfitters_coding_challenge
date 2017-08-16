from tornado.testing import (
    AsyncTestCase,
    AsyncHTTPClient,
    gen_test,
)

from pymongo import MongoClient

import json
import urllib
import unittest

#FIXME: Database must be manually dropped
# and tests individually run in order. 

class TestRewardsService(AsyncTestCase):

    @gen_test
    def test_GET_rewards_endpoint(self):
        client = AsyncHTTPClient(self.io_loop)
        response = yield client.fetch("http://localhost:7050/rewards")
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
        response = yield client.fetch("http://localhost:7050/purchases")
        self.assertEqual(
            '[]',
            response.body
        )

    @gen_test
    def test_POST_purchases_endpoint(self):
        client = AsyncHTTPClient(self.io_loop)
        post_data = {
            'email_address': 'test@domain.com',
            'order_total': 0.0,
        }
        body = urllib.urlencode(post_data)
        response = yield client.fetch("http://localhost:7050/purchases", method='POST', headers=None, body=body)
        exprected_item = {
            u'order_total': 0.0, u'email_address': u'test@domain.com'}
        returned = json.loads(response.body)
        self.assertIsInstance(returned, list)
        self.assertEqual(len(returned), 1)
        returned_item = returned[0]
        self.assertIn('id', returned_item)
        returned_item.pop('id')
        self.assertEqual(exprected_item, returned_item)
