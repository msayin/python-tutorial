print("Build a Translator Start from 2:52 minute")
print("Example1")

def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            translation = translation + "g"
        else:
            translation = translation+letter
    return translation
print (translate(input("Enter a phrase:")))




print("Example2")

def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower ()in "aeiou":
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + letter
    return translation
print (translate(input("Enter a phrase:")))
