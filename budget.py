
#Creating a Category class that tracks budget of different categories.

class Category:
  def __init__(self,name):
    self.name = name 
    self.funds = 0
    self.ledger = [] # list that stores dict 

  def deposit(self, amount, description = ''):
    self.ledger.append({'amount': amount, 'description': description})
    self.funds+=amount
    
  def withdraw(self, amount, description = ""):
    if self.check_funds(amount):
      self.ledger.append({'amount': -amount, 'description':   description})
      self.funds -= amount
      return True
    return False
    
  def get_balance(self):
    return self.funds

  def transfer(self, amount, another):
    if not self.check_funds:
      return False
    self.withdraw(amount, f"Transfer to {another.name}")
    another.deposit(amount, f"Transfer from {self.name}")
    return True
    
  def check_funds(self, amount):
    if self.funds >= amount:
      return True
    return False

  ## string formatting to match given output
  def __str__(self):
    s = ""
    s+=self.name.center(30,"*") + '\n'
    for item in self.ledger:
      if len(item['description']) > 23:
        s+=item['description'][0:23]
      else:
        s+=item['description'][0:23].ljust(23)
      s+='{0:.2f}'.format(item['amount']).rjust(7)
      s+='\n'
    s+="Total: {0:.2f}".format(self.funds)
    return s
