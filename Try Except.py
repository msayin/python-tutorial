print("Try Except Start from 3:04 minute")
print("Example1")

number = int (input ("Enter a number:"))
print (number)




print("Example2")
try:
    number = int (input ("Enter a number:"))
    print (number)
except:
    print("Invalid Input")



print("Example3")

try:
    value = 10 / 0
    number = int(input("Enter a number:"))
    print(number)
except ZeroDivisionError:
    print("Divided by zero")