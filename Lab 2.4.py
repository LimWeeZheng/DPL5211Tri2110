# Student ID: 1201200463
# Student Name: Lim Wee Zheng

BANANA = 1.5
GRAPE = 5.6

print("Invoice for Fruits Purchase")
print("---------------------------------")
qty1 = int(input("Enter the quantity (comb) of bananas bought: "))
qty2 = int(input("Enter the amount (kg) of grapes bought: "))

total1 = qty1 * BANANA
total2 = qty2 * GRAPE
grandtotal = total1 + total2

print("Item \t\t Qty \t Price \t\t Total")
print("Banana (combs) \t {} \t RM{:.2f} \t RM{:.2f}".format(qty1,BANANA,total1))
print("Grapes (kg) \t {} \t RM{:.2f} \t RM{:.2f}".format(qty2,GRAPE,total2))
print("Total: RM{:.2f}".format(grandtotal))