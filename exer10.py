# test case for exer 7
#checking for type error not included
import unittest
from exer7 import BankAccount,StudentAccount

class BankAccTestCase(unittest.TestCase):
    """Test for Bank Account"""

    def setUp(self):
        self.account = BankAccount("Angelli",909090,300)
    
    def test_deposit(self):
        self.account.deposit(100)
        self.assertEqual(self.account.balance, 400)
    
    def test_withdraw(self):
        self.account.withdraw(100)
        self.assertEqual(self.account.balance, 200)
    
    def test_add_interest(self):
        self.account.add_interest()
        self.assertEqual(self.account.balance, 390)

    def test_withdraw_overdraft(self):
        self.account.withdraw(400)
        self.assertEqual(self.account.balance, 300)

class StudentAccTestCase(unittest.TestCase):
    """Test for Student Account"""

    def setUp(self):
        self.account = StudentAccount("Angelli",909090,2000)
    
    def test_deposit(self):
        self.account.deposit(100)
        self.assertEqual(self.account.balance, 2100)
    
    def test_withdraw(self):
        self.account.withdraw(100)
        self.assertEqual(self.account.balance, 1900)

    def test_add_interest(self):
        self.account.add_interest()
        self.assertEqual(self.account.balance, 2600)

    def test_withdraw_overdraft(self):
        self.account.withdraw(2000)
        self.assertEqual(self.account.balance, 2000)

if __name__ == '__main__':
    unittest.main()