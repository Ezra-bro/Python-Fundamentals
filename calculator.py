num1 = int(input("Enter the firstnumber :"))
operator = input("Enter the operation sign ")
num2 = int(input("Enter the secondnumber :"))

if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "/":
    print(num1 / num2)
elif operator == "^":
    print(num1 ** num2)
elif operator == "%":
    print(num1 % num2)
else:
    print("Operation not supported!!Please enter the correct operation")



