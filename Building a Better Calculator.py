print("Building a Better Calculator Start from 2:00 minute")
num1 = float (input ("Enter firs number: "))
op = input ("Enter operator: ")
num2 = float(input("Enter second number:"))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == ("/"):
    print(num1 / num2)
elif op == ("*"):
    print(num1 * num2)
else:
    print("Invalid operator")
