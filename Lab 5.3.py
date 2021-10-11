# Student ID : 1201200463
# Student Name : Lim Wee Zheng


def get_cm():
    cm = float(input("Enter centimeter : "))
    m = cm_to_meter(cm)
    print("{:.2f} centimeters is equals to {:.2f} meters".format(cm,m))

def cm_to_meter(centimeter):
    meter = centimeter / 100
    return meter

def get_meter():
    m = float(input("Enter meter : "))
    cm = meter_to_cm(m)
    print("{:.2f} meters is equals to {:.2f} centimeters".format(m,cm))

def meter_to_cm(meter):
    centimeter = meter * 100
    return centimeter

print("======================================")
print("                MENU")
print("======================================")
print("  1.    Convert centimeter to meter")
print("  2.    Convert meter to centimeter")
print("======================================")

choice = int(input("Enter your choice : "))

if(choice == 1):
    get_cm()
elif(choice == 2):
    get_meter()
else:
    print("Invalid choice.")
