print("If Statements Start from 1:40 minute")
print("If Statements yazdigimiz datalara cevap verir")

print("Example1")

print("I wake up" ,
"if it`s cloudy" ,
"I bring an umbrella" ,
"otherwise" ,
"I bring sunglasses")


print("Example2")

print ("I am at a restaurant" ,
"if I want meat" ,
    "I order a steak" ,
"otherwise if I want pasta" ,
"I order spaghetti & meatballs" ,
"I order a salad.")



print("Example3")
is_male = True
if is_male:
    print("You are a male")
else:
    print("You are not a male")


print("Example4")
is_male = True
is_tall = True
if is_male or is_tall:
    print("You are a male or tall or both")
else:
    print ("You neither male nor tall")



print("Example5")
is_male = False
is_tall = True
if is_male or is_tall:
    print("You are a male or tall or both")
else:
    print ("You neither male nor tall")



print("Example6")
is_male = False
is_tall = False
if is_male or is_tall:
    print("You are a male or tall or both")
else:
    print ("You neither male nor tall")



print("Example7")
print ("or ve and aynilar ancak and te her iki durumunda True olmasi gerekiyor")
print("")
is_male = False
is_tall = False
if is_male and is_tall:
    print("You are tall male")
else:
    print ("You are neither not male or not tall or both")




print("Example8")
print("")
is_male = True
is_tall = True
if is_male and is_tall:
    print("You are a tall male")
else:
    print ("You are neither not male or not tall or both")



print("Example9")
print("")
is_male = True
is_tall = False
if is_male and is_tall:
    print("You are a tall male")
else:
    print ("You are neither not male or not tall or both")



print("Example10")
print("")
is_male = True
is_tall = True
if is_male and is_tall:
    print("You are a tall male")
elif is_male and not (is_tall):
    print("You are a short male")
elif not (is_male) and not is_tall:
    print("You are not a male but are tall")
else:
    print("You are either not male or not tall or both")



print("Example11")
print("")
is_male = False
is_tall = True
if is_male and is_tall:
    print("You are a tall male")
elif is_male and not (is_tall):
    print("You are a short male")
elif not (is_male) and is_tall:
    print("You are not a male but are tall")
else:
    print("You are either not male or not tall or both")


print("Example12")
print("")
is_male = True
is_tall = False
if is_male and is_tall:
    print("You are a tall male")
elif is_male and not (is_tall):
    print("You are a short male")
elif not (is_male) and is_tall:
    print("You are not a male but are tall")
else:
    print("You are either not male or not tall or both")


print("Example13")
print("")
is_male = False
is_tall = False
if is_male and is_tall:
    print("You are a tall male")
elif is_male and not (is_tall):
    print("You are a short male")
elif not (is_male) and is_tall:
    print("You are not a male but are tall")
else:
    print("You are not a male and not tall")