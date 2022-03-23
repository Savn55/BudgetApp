# testing module for each function 
# add additional test functions if needed.

import unittest
import budget

class UnitTests(unittest.TestCase):
  def setUp(self):
    self.food = budget.Category("Food")
    self.entertainment = budget.Category("Entertainment")

  def test_deposit(self):
    self.food.deposit(900, "deposit")
    actual = self.food.ledger[0]
    expected = {"amount": 900, "description": "deposit"}
    self.assertEqual(actual, expected, 'Expected `deposit` method to create a specific object in the ledger instance variable.')
    self.food.deposit(45.56)
    actual = self.food.ledger[1]
    expected = {"amount": 45.56, "description": ""}
    self.assertEqual(actual, expected, 'Expected calling `deposit` method with no description to create a blank description.')

  def test_withdraw(self):
    self.food.deposit(900, "deposit")
    self.food.withdraw(45.67, "milk, cereal, eggs, bacon, bread")
    actual = self.food.ledger[1]
    expected = {"amount": -45.67, "description": "milk, cereal, eggs, bacon, bread"}
    self.assertEqual(actual, expected, 'Expected `withdraw` method to create a specific object in the ledger instance variable.')

  def test_withdraw_no_funds(self):
    self.food.deposit(100,'deposit')
    eligible_withdraw = self.food.withdraw(100.10)
    self.assertEqual(eligible_withdraw, False, "'Expected withdraw' method to return 'False'.")

  def test_get_balance(self):
    self.food.deposit(900, "deposit")
    self.food.withdraw(45.67, "milk, cereal, eggs, bacon, bread")
    actual = self.food.get_balance()
    expected = 854.33
    self.assertEqual(actual, expected, 'Expected balance to be 54.33')

  def test_transfer(self):
    self.food.deposit(900, "deposit")
    self.food.withdraw(45.67, "milk, cereal, eggs, bacon, bread")
    self.food.transfer(20, self.entertainment)
    actual = self.food.ledger[2]
    expected = {"amount": -20, "description": "Transfer to Entertainment"}
    self.assertEqual(actual, expected, 'Expected `transfer` method to create a specific ledger item in food object.')
    actual = self.entertainment.ledger[0]
    expected = {"amount": 20, "description": "Transfer from Food"}
    self.assertEqual(actual, expected, 'Expected `transfer` method to create a specific ledger item in entertainment object.')

  def test_check_funds(self):
    self.food.deposit(10, 'deposit')
    actual = self.food.check_funds(20)
    expected = False
    self.assertEqual(actual,expected, "Expected 'check_funds' method to be False")
    actual = self.food.check_funds(10)
    expected = True
    self.assertEqual(actual,expected, "Expected 'check_funds' method to be True")

  def test_to_string(self):
    self.food.deposit(900, "deposit")
    self.food.withdraw(45.67, "milk, cereal, eggs, bacon, bread")
    self.food.transfer(20, self.entertainment)
    actual = str(self.food)
    expected = f"*************{self.food.name}*************\ndeposit                 900.00\nmilk, cereal, eggs, bac -45.67\nTransfer to Entertainme -20.00\nTotal: 834.33"
    self.assertEqual(actual, expected, 'Expected different string representation of object.')


if __name__ == "__main__":
    unittest.main()
