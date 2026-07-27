from datetime import datetime
print("=== Supermarket Billing System ===")
n = int(input("Enter number of items: "))
total = 0

for i in range(n):
    print("\nItem", i + 1)
    name = input("Item Name: ")
    price = float(input("Price: "))
    qty = int(input("Quantity: "))

    amount = price * qty      
    total += amount           

print("\n------ BILL ------")
print("Date:", datetime.now())
print("Total Amount:", total)

if total >= 1000:             
    discount = total * 0.10
    final = total - discount  
    print("Discount (10%):", discount)
else:
    final = total

print("Final Amount:", final)
print("Thank You! Visit Again.")
