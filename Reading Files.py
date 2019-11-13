#Reading Files Start from 3:12 minute
#Not1: open ("Employees.txt", "r") (r) koydugumuzda bu dosyayi sadece okuyabiliyoruz.
#Not2: open ("Employees.txt", "w") (w) koydugumuzda bu dosya uzerinde yazim yapip degisiklik yapabiliyoruz.
#Not3: open ("Employees.txt", "a") (a) koydugumuzda bu dosyayin altina eklemee yapabiliyoruz ancak dosyayi modife edemiyoruz.
#Not1: open ("Employees.txt", "r+") (r+) koydugumuzda bu dosyayi hem kuyabiliyoruz hemde uzerinde yazabiliyoruz.

print("Example1")


employee_file = open("employees.txt", "r")
print(employee_file.read())
employee_file.close()