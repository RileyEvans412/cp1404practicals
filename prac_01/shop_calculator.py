"""
The program allows the user to enter the number of items and the price of each different item.
Then the program computes and displays the total price of those items.
If the total price is over $100, then a 10% discount is applied to that total before the amount is displayed on the screen.
"""

total_cost = 0

valid_input = False
while valid_input is False:
    number_of_items = int(input("Number of Items: "))
    if number_of_items > 0:
        valid_input = True
    else:
        print("error please enter a valid number")
for i in range(1, number_of_items + 1):
    cost_of_item = float(input("What is the price of " + str(i) + " item: $"))
    total_cost += cost_of_item
if total_cost >= 100:
    total_cost *= 0.9
    print("Total Price for {0:} items after being discounted is ${1:.2f}".format(number_of_items, total_cost))
else:
    print("Total Price for {0:} items is {1:.2f}".format(number_of_items, total_cost))
