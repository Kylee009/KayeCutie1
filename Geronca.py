geroncaname = input("Name: ")

geronca_calculation = input('''\nChoose from below to calculate:
|Power|
|Voltage|
|Current|

''').strip().capitalize()

if geronca_calculation == "Power":
    geronca_current = float(input("Current: "))
    geronca_voltage = float(input("Voltage: "))
    geronca_power = geronca_current * geronca_voltage
    print(f"Power is {geronca_power:,.2f} Watt/s.")

elif geronca_calculation == "Current":
    geronca_power = float(input("Power: "))
    geronca_voltage = float(input("Voltage: "))
    geronca_current = geronca_power / geronca_voltage
    print(f"Current is {geronca_current:,.2f} Ampere/s.")

elif geronca_calculation == "Voltage":
    geronca_power = float(input("Power: "))
    geronca_current = float(input("Current: "))
    geronca_voltage = geronca_power / geronca_current
    print(f"Voltage is {geronca_voltage:,.2f} Volt/s.")

else:
    print("Invalid input")
