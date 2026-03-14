"""Write a program to create a class Computer with a private attribute max_price and methods sell(to display)
 the selling price and setmaxprice(change the private attribute max_price).
   Now create an object for the class Computer.
 Try changing the value of max price and use the sell function to display the updated price.
   Use a setter function to update the value and again display the price."""
class Computer:
    def __init__(self):
        self.__max_price = 1000

    def sell(self):
        print(f"Selling Price: {self.__max_price}")
    def set_max_price(self, price):
        self.__max_price = price

ob=Computer()
ob.set_max_price(1500)
ob.sell()
ob.set_max_price(2000)
ob.sell()