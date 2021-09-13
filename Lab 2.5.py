# Student ID: 1201200463
# Student Name: Lim Wee Zheng

WATER = 0.15

print("Natural Mineral Water Dispenser")
print("---------------------------------")
litres = int(input("Enter amount of litres: "))
total = litres * WATER
print("Price per litre   = RM {:.2f}".format(WATER))
print("Number of liters  = ",litres)
print("Total : RN {:.2f}".format(total))
