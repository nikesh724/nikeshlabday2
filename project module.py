from datetime import datetime
import time
import pyttsx3
import qrcode

# Voice Engine
engine = pyttsx3.init()

# Product List
items = {
    1: ("Aashirvaad Atta", 350),
    2: ("Tata Salt", 30),
    3: ("Amul Milk", 32),
    4: ("Fortune Oil", 180),
    5: ("Surf Excel", 120)
}

bill = []
total = 0

print("===== DMART SUPERMARKET =====")
name = input("Customer Name: ")

while True:

    print("\nNo  Brand Name              Price")

    for i, (brand, price) in items.items():
        print(f"{i}. {brand:20} ₹{price}")

    n = int(input("Enter Product No: "))
    q = int(input("Enter Quantity: "))

    brand, price = items[n]

    amount = price * q
    total = total + amount

    bill.append((brand, q, amount))

    more = input("More Items (y/n): ").lower()

    if more == "n":
        break

# GST Calculation
gst = total * 0.05
grand = round(total + gst)

# Date and Time
date_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

# Bill Output
print("\n========== DMART BILL ==========")
print("Customer :", name)
print("Date     :", date_time)
print("-" * 45)

print("Brand Name          Qty     Amount")

for b, q, a in bill:
    print(f"{b:20} {q:<7} ₹{a}")

print("-" * 45)

print("Subtotal    : ₹", total)
print("GST 5%      : ₹", round(gst, 2))
print("Grand Total : ₹", grand)

# QR Code Data
qr_data = f"""
DMART SUPERMARKET

Customer: {name}
Date: {date_time}

Subtotal: Rs.{total}
GST 5%: Rs.{round(gst, 2)}
Grand Total: Rs.{grand}

Thank You! Visit Again.
"""

# Generate QR Code
qr = qrcode.make(qr_data)

# Save QR Code
qr.save("dmart_bill_qr.png")

print("\nQR Code Generated Successfully!")
print("QR Code saved as dmart_bill_qr.png")

# Automatically Show QR Code
qr.show()

# Voice Output
engine.say(
    f"Thank you for shopping. "
    f"Your total bill is {grand} rupees."
)

engine.runAndWait()

print("\nThank You! Visit Again.")

time.sleep(2)