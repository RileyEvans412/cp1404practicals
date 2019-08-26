"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

sales = float(input("Enter your sales: $"))
while sales > 0:
    if sales >= 1000:
        print("Your bonus is: $", (sales * 0.15))
    else:
        print("Your bonus is: $", (sales * 0.10))
    sales = float(input("Enter your sales: $"))
print("Thanks for visiting")