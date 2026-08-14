#Exceptional handling
#zero division error
'''try:
    a =10
    b = 0
    c = a/b
except ZeroDivisionError:
    print("noo")
else:
    print(c)'''

#value error
'''try:
    age = int("hello")
    print(age)

except ValueError:
    print("value error")'''

#type error
'''try:
    a = 10+'h'
    print(a)
except TypeError:
    print("type error")'''

#Index error
'''try:
    a = [1,2,3,4]
    print(a[5])
except IndexError:
    print("index error")'''

#Multiple condition
'''try:
    a = int("hello")
except ValueError:
    print("value error")
except ZeroDivisionError:
    print("zero division error")
else:
    print(a)'''

#Raise
'''age = -6
if age < 0:
    raise ValueError("Not application")
print("okk")'''

#File handling
#create and write
'''file =open("nikesh.txt",'w')
file.write("hii Im learning python")
file.close()
print("create succefully")'''

#read
'''file =open("nikesh.txt",'w')
file.write("hii Im learning python")
file.close()
print("create succefully")
file = open("nikesh.txt",'r')
a = file.read()
print(a)
file.close()'''

#line by line
'''file =open("nikesh.txt",'w')
file.write("hii Im learning python")
file.close()
print("create succefully")
file = open("nikesh.txt",'r')
for line in file:
    print(file)
file.close()'''

#read only 1 line
'''file =open("nikesh.txt",'w')
file.write("hii Im learning python")
file.close()
print("create succefully")
file = open("nikesh.txt",'r')
print(file.read())
file.close()'''

#append
'''file =open("nikesh.txt",'a')
file.write("\n java")
file.close()
print("create succefully")
file=open("nikesh.txt",'r')
a = file.read()
print(a)
file.close()'''

#Exceptional + file handling
try:
    file = open("naresh.txt",'r')
    a = file.read()
    file.close()
except FileNotFoundError:
    print("file not found")
else:
    print(a)








