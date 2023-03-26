import unittest
from BankAccount import BankAccount

class TestBankAccount(unittest.TestCase):

    def setUp(self):
        self.account = BankAccount(1000)

    # Tests for deposit method
    def test_deposit_positive(self):
        self.account.deposit(500)
        self.assertEqual(self.account.get_balance(), 1500)

    def test_deposit_zero(self):
        self.account.deposit(0)
        self.assertEqual(self.account.get_balance(), 1000)

    def test_deposit_negative(self):
        with self.assertRaises(ValueError):
            self.account.deposit(-500)
            
    # Tests for withdraw method
    def test_withdraw_positive(self):
        self.assertTrue(self.account.withdraw(500))
        self.assertEqual(self.account.get_balance(), 500)

    def test_withdraw_zero(self):
        self.assertTrue(self.account.withdraw(0))

    def test_withdraw_negative(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(-500)

    # Tests for transfer method
    def test_transfer_success(self):
        target_account = BankAccount(500)
        self.assertTrue(self.account.transfer(target_account, 400))
        self.assertEqual(self.account.get_balance(), 600)
        self.assertEqual(target_account.get_balance(), 900)

    def test_transfer_fail(self):
        target_account = BankAccount(500)
        self.assertFalse(self.account.transfer(target_account, 1200))
        self.assertEqual(self.account.get_balance(), 1000)
        self.assertEqual(target_account.get_balance(), 500)

    # Tests for can_withdraw method
    def test_can_withdraw_true(self):
        self.assertTrue(self.account.can_withdraw(500))

    def test_can_withdraw_false(self):
        self.assertFalse(self.account.can_withdraw(1200))

    def test_can_withdraw_exact(self):
        self.assertTrue(self.account.can_withdraw(1000))

if __name__ == "__main__":
    unittest.main()
