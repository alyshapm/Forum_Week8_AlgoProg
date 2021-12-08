class calculatingCost:
        # initializer method that accepts 2 parameter (input from user), creates the objects
    def __init__(self, name="", amount=0.0):
        self.__name = name
        self.__amount = amount
        self.__price = self.fromPricelistAPM()
        self.__calculatedPrice = self.costCalculatorAPM()
    
        # mutator method that allows the attributes to be modified
    def setAmountAPM(self, amount):
        self.__amount = amount
    def setNameAPM(self, name):
        self.__name = name
    def setCalculatedPriceAPM(self, calculatedPrice):
        self.__calculatedPrice = calculatedPrice

        # private method that stores the pricelist, and assigns the object the price according
        # to its name
    def fromPricelistAPM(self):
        if self.__name == "Dry Cured Iberian Ham":
            self.__price = 177.80
        elif self.__name == "Wagyu Steaks":
            self.__price = 450.00
        elif self.__name == "Matsutake Mushrooms":
            self.__price = 272.00
        elif self.__name == "Kopi Luwak Coffee":
            self.__price = 306.50
        elif self.__name == "Moose Cheese":
            self.__price = 487.20
        elif self.__name == "White Truffles":
            self.__price = 3600.00
        elif self.__name == "Blue Fin Tuna":
            self.__price = 3603.00
        elif self.__name == "Le Bonnotte Potatoes":
            self.__price = 270.81
        else:
            self.__price = 0.00
        # i have added a return statement here because when i use the accessor method to pass on the
        # value, for some reason it displays as its default value, therfore affecting the calculation
        return self.__price

    
        # public method that calculates the total cost of the food from its price and desired amount
    def costCalculatorAPM(self):
        self.__calculatedPrice = self.__amount * self.__price
        return self.__calculatedPrice

        # accessor method used to access the hidden objects
    def getNameAPM(self):
        return self.__name
    def getAmountAPM(self):
        return self.__amount

        # returns a human-readable format and displays information abou the food item
    def __str__(self):
        return f"Item: {self.getNameAPM()} \nAmount ordered: {self.getAmountAPM()} lb \nPrice/pound: ${self.fromPricelistAPM():,.2f} \nPrice of order: ${self.costCalculatorAPM():,.2f}"