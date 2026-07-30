# Supermarket Billing System

def bill():
    total = 0

    while True:
        item = input("Enter item name: ")
        price = float(input("Enter item price: "))
        qty = int(input("Enter quantity: "))

        amount = price * qty
        total += amount

        print("Amount =", amount)

        choice = input("Add another item? (y/n): ")
        if choice == "n":
            break

    print("\n----- BILL -----")
    print("Total Amount =", total)

    if total >= 1000:
        discount = total * 0.10
        total = total - discount
        print("Discount = 10%")
    else:
        print("No Discount")

    print("Final Amount =", total)

def main():
    print("=== Supermarket Billing System ===")
    bill()

main()