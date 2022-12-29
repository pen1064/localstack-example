from unittest import TestCase

import testutils_s3


class Test(TestCase):
    def Setup(self):
        self.maxDiff = None

    @classmethod
    def setup_class(cls):
        print("setting up the class")
        testutils_s3.create_lambda("s3_lambda")
        testutils_s3.create_bucket("test-bucket")

    @classmethod
    def teardown_class(cls):
        print("Tearing down the class")
        testutils_s3.delete_lambda("s3_lambda")
        testutils_s3.delete_bucket("test-bucket")

    def test_lambda_return_correct_message(self):
        payload = testutils_s3.invoke_function("s3_lambda", "test_item")
        self.assertEqual(payload["message"], "object placed")
