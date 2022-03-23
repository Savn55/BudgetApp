import budget
from unittest import main # importing testing module

food = Category('food')
clothing = Category('clothing')
auto = Category('auto')
food.deposit(1000,'deposit')
clothing.deposit(1000,'deposit')
food.withdraw(583, 'grocery') 
food.transfer(140.89, clothing)
print(food)
print(clothing)
print(food.get_balance())

# Run unit tests automatically
main(module='test_module', exit=False)
