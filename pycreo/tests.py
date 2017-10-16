import unittest

from pycreo import CreosonClient


class BaseCreoTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.client = CreosonClient()

    def setUp(self):
        resp, err = self.client.connect()
        if err:
            self.fail(f'Cannot connect to server. Detail: {resp}')
        self.sessionId = resp

    def tearDown(self):
        self.client.disconnect(self.sessionId)
