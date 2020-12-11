import unittest

from models.merchant import Merchant
from models.tag import Tag
from models.transaction import Transaction

class TestTransaction(unittest.TestCase):
    def setUp(self):
        self.transaction_1 = Transaction("Bought food from Tesco", 50, "Tesco", "Groceries")


    def test_transaction_has_description(self):
        self.assertEqual("Bought food from Tesco", self.transaction_1.description)


    def test_transaction_has_amount(self):
        self.assertEqual(50, self.transaction_1.amount)


    def test_transaction_has_merchant(self):
        self.assertEqual("Tesco", self.transaction_1.merchant)

    
    def test_transaction_has_tag(self):
        self.assertEqual("Groceries", self.transaction_1.tag)