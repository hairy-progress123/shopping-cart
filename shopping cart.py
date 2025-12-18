
Item = input("What item do you want to purchase: ")
Quantity = int(input(f"How many {Item} do you want: "))
Price = float(input("What is the price of the item :"))
Total = Price * Quantity
Discount = Total / 100 * 20
Total_after_discount = Total - Discount
tax = Total_after_discount / 100 * 18 
Total_after_tax = Total_after_discount + tax 
print(f"Your total is: {Total_after_tax} ")

