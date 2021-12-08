    # imports the class
from classCalculatingCostAPM import calculatingCost
# from tabulate import tabulate

    # this functions creates a list of object
def listItemsAPM():
        # here i had used the tabulate function to display the food item and their corresponding price
        # in tabular form, but since installing the pip is required i have disabled it
    # print("Price list of food items")
    # priceList = [["Food item", "Price/pound (USD)"], ["Dry Cured Iberian Ham", "$177.80"], 
    # ["Wagyu Steaks", "450.00"], ["Matsutake Mushrooms", "272.00"], ["Kopi Luwak Coffee","306.50"], 
    # ["Moose Cheese", "487.20"], ["White Truffles", "3600.00"], ["Blue Fin Tuna", "3603.00"], 
    # ["Le Bonnotte Potatoes", "270.81"]]
    # print(tabulate(priceList, headers="firsrow", tablefmt="grid"))
        # input validation that loops the input if user fails to enter a valid data that is more than 1.
        # the number that is inputted will determine the number of repetition for the loop after that
        # obtains the food name and weight
    while True:
        numberOfItems = int(input("How many items will you order today? "))
        if numberOfItems < 1:
            print("Number of items must be greater than 0.")
            numberOfItems = int(input("Re-enter number of items you will order today: "))
        else:
            break
        # global keyword allows other functions to access the list
    global listOfItems 
        # declare empty list
    listOfItems = []
    startingIndex = 0
        # prompts the user to input the food name and the desired weight using a loop 
        # in the range of the number of items the user inputted at the beginning.
    for item in range(numberOfItems):
            # displays the nth number of item
        startingIndex += 1
        print(f"Item #{startingIndex}")
        nameOfFood = input("Enter name of food: ")
            # validates whether the input is within the condition or not. if not, it will continue
            # to loop and break if it finally meets the condition.
        while True:
            amountOflb = float(input("Enter amount, in pounds: "))
            if amountOflb < 1:
                print("Amount of pounds must be greater than 0.")
                amountOflb = float(input("Re-enter amount of pounds: "))
            else:
                break
            # appends the inputted data (name and weight) into the list, which is passed to the class
            # and becomes its object. each data is assigned as its corresponding attribute
        listOfItems.append(calculatingCost(name=nameOfFood, amount=amountOflb))
    return listOfItems
    
    # this function displays the summary of the items purchased (content of the list) and accepts
    # the list as a parameter
def displayListAPM(listOfItems):
    print("\nHere's a summary of the items purchased:")
    print("----------------------------------------")
        # using loop to display each of the item, repeats according the number of items
    for item in listOfItems:
        print(item, "\n")

    # this function calculates the grand total cost of the item and accepts the list as a parameter
def calculationAPM(listOfItems):
    # starting index
    total = 0
    for item in listOfItems:
        # calculates the cost of each food item using the public mutator method, in which the loop
        # will add up the grand total if there are more than one item
        total += calculatingCost.costCalculatorAPM(item)
    print(f"The total cost will be ${total:,.2f}")
    return total

    # main function calls the 3 functions above
def main():
    listItemsAPM()
    displayListAPM(listOfItems)
    calculationAPM(listOfItems)
if __name__ == '__main__':
    main()
