import unittest

from hashemail.hash_email import HashEmail


class HashEmailTests(unittest.TestCase):

    def setUp(self):
        self.test_email = "TeSt@eXaMpLe.CoM"
        self.emailhash = HashEmail(self.test_email)
        self.expectedHash = '149ce4995c9157e7fffb2ad59dbe426f9067bb78f43edd26d5b991b49fbbd1a8'

    def test_hashvalue(self):
        self.assertEqual(self.emailhash.hash_value(), self.expectedHash)

    def test_lower(self):
        self.assertEqual(self.emailhash.email, "test@example.com")

    def test_raw(self):
        self.assertEqual(self.emailhash.raw_email, self.test_email)
