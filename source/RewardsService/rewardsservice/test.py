from tornado.testing import (
    AsyncTestCase,
    AsyncHTTPClient,
    gen_test,
)


class TestRewardService(AsyncTestCase):

    @gen_test
    def test_GET_reward_endpoint(self):
        client = AsyncHTTPClient(self.io_loop)
        response = yield client.fetch("http://localhost:7050/rewards")
        self.assertIn(
            '{"tier": "A", "points": 100, "rewardName": "5% off purchase"}',
            response.body
        )
