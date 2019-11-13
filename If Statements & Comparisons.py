print("If Statements & Comparisons Start from 1:54 minute")
print("If Statements Comparisons yazdigimiz degerleri karsilastirmaya yarar")

print ("Example1")
def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print (max_num(300,40,5))


print ("Example2")
print ("== bir degerin baska bir degere esit olup olmadigini kontrol eder")
def max_num(num1, num2, num3):
    if num1 == num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print (max_num(300,40,5))

print ("Example3")
print ("! bir degerin baska bir degere esit olmadigini ifade eder")
def max_num(num1, num2, num3):
    if num1 != num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print (max_num(300,40,5))