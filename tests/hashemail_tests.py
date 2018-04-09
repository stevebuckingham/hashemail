import unittest

from hashemail.hash_email import HashEmail


class HashEmailTests(unittest.TestCase):

    def setUp(self):
        self.test_email = "TeSt@eXaMpLe.CoM"
        self.emailhash = HashEmail(self.test_email)
        self.expectedHash = 'c641e0b90582e3e7f192f655798f27a625b7e198cf8c153b2f5c2ba3c947c38f'

    def test_hashvalue(self):
        self.assertEqual(self.emailhash.hash_value(), self.expectedHash)

    def test_lower(self):
        self.assertEqual(self.emailhash.email, "test@example.com")

    def test_raw(self):
        self.assertEqual(self.emailhash.raw_email, self.test_email)
