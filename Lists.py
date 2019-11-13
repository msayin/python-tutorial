print("List Start from 1:03 minute")
print ("Not1:Liste yaparken köşeli parantez kullanırız")
friends = ["Ayse", "Sinan","Semih"]
print (friends)


print ("Not2:Liste elementlerden yani isimlerden hangisinin sirasini yazarsak o cikar")
print("Not3:python da siralama 0 sifirdan baslar")
friends = ["Ayse", "Sinan","Semih"]
print (friends[0])

print("Not4:- koyup yukardaki ismin sayisniz yazarsa o isim cikar org:-1")
friends = ["Ayse", "Sinan","Semih"]
print (friends[-1])

print("Not5:" , "eger : iki nokta koyarda deger yazarsak bu iki konta iki deger arasini gosterir] ")
friends = ["Ayse", "Sinan","Semih"]
print (friends[0:2])

print("Not6:" , "eger : iki nokta koyarda deger yazarsak bu iki kontadan sonra yazdigimiz deger sonraki tum isimleri siralar ")
friends = ["Ayse", "Sinan","Semih", "Krem"]
print (friends[1:])

print("Not7:" , "atanan degerler modife edilebilir")
friends = ["Ayse", "Sinan","Semih", "Krem"]
friends [1] = "Munevver"
print (friends[1])