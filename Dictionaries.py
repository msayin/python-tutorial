print("Dictionaries Start from 2:07 minute")

monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}


print (monthConversions.get ("Jan"))
print (monthConversions.get ("Dec"))
print("eger dogru anahtar yazilmazsa gerekli cevam alinamaz")
print (monthConversions.get ("Luv", "Not a valid key"))






