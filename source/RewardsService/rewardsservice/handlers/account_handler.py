import json
import tornado.web

from pymongo import MongoClient
from tornado.gen import coroutine
import re

class AccountHandler(tornado.web.RequestHandler):

    @coroutine
    def get(self):
#        import ipdb; ipdb.set_trace()
        match = re.search(r'[0-9]+',self.request.path):
        if match:
            account_id = match.group()
         

    @coroutine
    def post(self):
        pass

    @coroutine
    def put(self, path):
        pass

