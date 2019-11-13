print("List Functions Start from 1:10 minute")
print ("Example1:")
lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Ayse", "Sinan", "Semih", "Krem"]
print(friends)


print ("Example2:")
lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Ayse", "Sinan", "Semih", "Krem"]
print(lucky_numbers)


print ("Example3:")
lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Ayse", "Sinan", "Semih", "Krem"]
friends.extend(lucky_numbers)
print(friends)
print("extend: genisletmek, uzatmak, devam ettirmek")


print ("Example4:")
lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Ayse", "Sinan", "Semih", "Krem"]
friends.append("Betul")
print(friends)
print("append: yazdigimiz satirin sonuna yeni bilgi eklemek")



print ("Example5:")
lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Ayse", "Sinan", "Semih", "Krem"]
friends.insert(1, "Betul")
print(friends)
print("insert: yazdigimiz satirin arasina yeni bilgi eklemek")


print ("Example5:")
lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Ayse", "Sinan", "Semih", "Krem"]
friends.remove("Semih")
print(friends)
print("remove: yazdigimiz satirdan bir bilgiyi silmek")



print ("Example6:")
lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Ayse", "Sinan", "Semih", "Krem"]
friends.clear()
print(friends)
print("clear: yazdigimiz tum satirlari silmek icin")



print ("Example7:")
lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Ayse", "Sinan", "Semih", "Krem"]
friends.pop()
print(friends)
print("pop: yazdigimiz satirdaki son nesneyi silmek icin")



print ("Example8:")
lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Ayse", "Sinan", "Semih", "Krem"]
print(friends.index("Ayse"))
print("index: yazdigimiz satirdaki nesnelerin sirasini gosterir ")



print ("Example9:")
lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Ayse", "Sinan", "Sinan", "Semih", "Krem"]
print(friends.count("Sinan"))
print("count: yazdigimiz satirdaki bir nesnenin kac kez gectigini sayar")


print ("Example10:")
lucky_numbers = [4, 8, 15, 16, 23,]
friends = ["Ayse", "Sinan", "Semih", "Krem"]
friends.sort( )
print (friends)
print("sort: yazdigimiz satirdaki nesneleri alfabetik siraya sokar")



print ("Example11:")
lucky_numbers = [ 42, 8, 15, 16, 23]
friends = ["Ayse", "Sinan", "Semih", "Krem"]
lucky_numbers.sort( )
print (lucky_numbers)
print("sort: yazdigimiz satirdaki nesneleri alfabetik siraya sokar")



print ("Example12:")
lucky_numbers = [ 42, 8, 15, 16, 23]
friends = ["Ayse", "Sinan", "Semih", "Krem"]
lucky_numbers.reverse( )
print (lucky_numbers)
print("reverse: yazdigimiz satirdaki nesneleri sondan basa dogru siraliyor")


print ("Example13:")
lucky_numbers = [ 42, 8, 15, 16, 23]
friends = ["Ayse", "Sinan", "Semih", "Krem"]
friends2 =friends.copy( )
print (friends2)
print("reverse: yazdigimiz satirdaki nesneleri sondan basa dogru siraliyor")

