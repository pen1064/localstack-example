import testutils
from unittest import TestCase

class Test(TestCase):
    def Setup(self):
        self.maxDiff = None
    @classmethod
    def setup_class(cls):
        print('setting up the class')
        testutils.create_lambda('lambda')

    @classmethod
    def teardown_class(cls):
        print('Tearing down the class')
        testutils.delete_lambda('lambda')

    def test_lambda_return_correct_message(self):
        payload = testutils.invoke_function('lambda')
        self.assertEqual(payload['message'], 'hello meow!')
