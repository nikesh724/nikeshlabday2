#task1
'''marks=int(input("enter a marks:"))
if marks>=35:
    print("pass")
else:
    print("fail")'''

#task2
'''age=int(input("enter age:"))
if age>=18:
    print("eligible for voting")
else:
    print("not eligible for voting")'''

#task3
'''bill=float(input("enter a bill:"))
if bill>=5000:
    print("bill:",(bill*10/100))
else:
    print("final amount:",bill)'''

#task4
'''user=str(input("enter a user:"))
password=str(input("enter a password:"))
if user=="ramkumar" and  password=="12345":
    print("verify the password")
else:
    print("not verify the password")'''

#task5
'''marks=int(input("enter a marks:"))
if marks>=90:
    print("grade A")
elif marks>=75:
    print("grade B")
elif marks>=50:
    print("grade C")
else:
    print("fail")'''

#task6
'''a=int(input("enter a:"))
b=int(input("enter b:"))
cal=input("enter +,-,*,/:")
if cal=="+":
    print(a+b)
elif cal=="-":
    print(a-b)
elif cal=="*":
    print(a+b)
elif cal=="/":
    print(a+b)
else:
     print("not cal")'''

#task7
'''units=int(input("enter a units:"))
if units<=100:
    print(units*2)
elif units<=200:
    print(units*3)
elif units>=200:
    print(units*5)
else:
    print("not units consum")'''

#task8
'''age=int(input("enter a age:"))
if age<=5:
    print("Ticket free")
elif age<=12:
    print("Ticket 50")
elif age>=12:
    print("Ticket 100")
else:
    print("age:",age)'''
#task9
'''salary=int(input("enter a salary:"))
score=int(input("enter a score:"))
if salary>=30000 and score>=700:
    print("the eligible for the lone")
else:
    print("not eligible for the lone ")'''
#task10
'''percentage=int(input("enter a percentage:"))
score=int(input("enter a score:"))
if percentage>=60 and score>=70:
    print("the eligible for the collage")
else:
     print("not eligible for the collage ")'''
#task11
'''percentage=int(input("enter a percentage:"))
aptitude=int(input("enter a aptitude:"))
if percentage>=65 and aptitude>=75:
    print("the eligible for the company")
else:
     print("not eligible of the company")'''
#task12
score=int(input("enter a score:"))
attendance=int(input("enter a attendance:"))
if score>=80 and attendance>=75:
    print("the eligible for the scholarship")
else:
     print("not eligible of the scholarship")
    #task13
'''balance = int(input("enter a balance:"))
amount = int(input("enter amount:"))
if balance >= amount:
    pin=str(input("enter a pin:"))
    if pin =="1234":
        print("transaction successfully")
    else:
        print("wrong pin")
else:
    print("insufficient balance")'''

#task14
'''username = str(input("enter a username:"))
if username =="nikesh":
    password =input("enter password:")
    if password =="8248660":
        otp =input("enter otp:")
        if otp =="1111":
            print("login successful")
        else:
            print("invalid otp")
    else:
        print("worng password")
else:
    print("wrong username")'''

#task15
'''doctor =input("doctor available (yes/no):")
if doctor =="yes":
    slot =input("slot available (yes/no):")
    if slot =="yes":
        print("appointment confirmed")
    else:
        print("no slot available")
else:
    print("doctor not available")'''

#task16
'''regis=input("regis (yes/no):")
if regis =="yes":
    fees =input("fees paid (yes/no):")
    if fees =="yes":
        print("access granded")
    else:
        print("pay fees")
else:
    print("not regis")'''

#task17
'''exp =int(input("enter a exp:"))
if exp>=3:
    rat = int(input("enter a rat:"))
    if rat>=8:
        print("bonus eligible")
    else:
        print("low rat")
else:
    print("not eligible")'''

#task18
'''ticket =input("ticket is available (yes/no):")
if ticket =="yes":
    fees = input("fees cleared (yes/no):")
    if fees =="yes":
        print("allow access")
    else:
        print("not fees cleared")
else:
    print("hall ticket is not available")'''

#task19
'''select =input("select for admission (yes/no):")
if select =="yes":
    room = input("room available (yes/no):")
    if room =="yes":
        print("allotted room")
    else:
        print("no room available")
else:
    print("admission not confirmed")'''

#task20
amount =float(input("enter purchase amount:"))
member =input("premium member (yes/no):")
if member =="yes" and amount>5000:
    discount = amount * 20/100
elif  member =="no" and amount>5000:
    discount = amount * 10/100
else:
    discount = 0

print("discount:",discount)
print("final amount =",amount-discount)
     
    



    




        
     
    

    







        
     
    

    
