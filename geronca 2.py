geronca_num1 = int(input("Enter a number: "))
geronca_num2 = int(input("Enter another number: "))
geronca_operator = input("Enter operator: ")

if geronca_operator == "+":
    geronca_sum = geronca_num1 + geronca_num2
    print(geronca_sum)
elif geronca_operator == "-":
    geronca_difference = geronca_num1 - geronca_num2
    print(geronca_difference)
elif geronca_operator == "*":
    geronca_product = geronca_num1 * geronca_num2
    print(geronca_product)
elif geronca_operator == "/":
    geronca_quotient = geronca_num1 / geronca_num2
    print(geronca_quotient)
else:
    print("Invalid operator/input")
