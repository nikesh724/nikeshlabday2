#list
'''#task1
num =[1,2,3,4,5,6,7,8,9,10]
for i in num:
    if i%2==0:
        print(i)'''

'''#task2
a = [10,11,12,13,14,15]
print("largest num:",max(a))
print("smallest num:",min(a))'''

'''#task3
num = [10,20,30]
total = sum(num)
average = total/len(num)
print("sum:",total)
print("average:",average)'''

'''#task4
numbers = [10,20,30,40,50,20]
unique = set(numbers)
print(unique)'''

'''#task5
numbers = [10,20,30,40,50]
numbers.sort()
print("second largest numbers:",numbers[-2])'''

'''#task6
a = [1,2,3,4,5,6]
a.reverse()
print(a)'''

'''#task7
a = [1,2,3,4]
b = [5,6,7,8]
merged = list(a+b)
print(merged)'''

'''#task8
a = [2,4,6,8,2,3,5,2]
a.count(2)
print("count =",a.count(2))'''

'''#task9
a = [1,2,3,4,5,6,7,8]
even =[]
odd =[]
for i in a:
    if i%2==0:
        even.append(i)
    elif i%2!=0:
        odd.append(i)

else:
    print("even:",even)
    print("odd:",odd)'''

'''#task10
student = ["Naresh","Nikesh","Ram","sakthi"]
name = input("enter student name:")
if name in student:
    print("student found")
else:
    print("student not found")'''

#tuple
#task1
'''subject = ("Python","java","c++","SQL","AI")
for i in subject:
    print(i)'''

#task2
'''subject = ("Python","java","c++","SQL","AI")
print(len(subject))'''

#task3
'''numbers = (10,20,30,40,50,20,60,70,20,80)
print(numbers.count(20))'''

#task4
'''subject = ("Python","java","c++","SQL","AI")
print("index of c++:",subject.index("c++"))'''

#task5
'''a = (10,20,30,40,50)
b = list(a)
print(b)'''

#task6
'''a = (10,20,30,40,50)
print(max(a))
print(min(a))'''

#task7
'''a = (1,2,3,4)
b = (5,6,7,8)
c = a+b
print("concatenate:",c)'''

#task8
'''a = (10,20,30,40,50)
if 20 in a:
    print("20 exists in the tuple")
else:
    print("20 does not exists in the tuple")'''

#task9
'''marks = (80,70,60,50)
tuple = tuple(marks)
average = sum(marks)/len(marks)
print("Tuple:",tuple)
print("average:",average)'''

#task10
'''a = (10,20,30,40,50)
print("First element:",a[0])
print("Middle element:",a[-3])
print("Last element:",a[-1])'''

#Set
#task1
'''a = {1,2,3,4}
b = {3,4,5,6}
print(a.union(b))'''

#task2
'''set1 = {1,2,3,4,5,6}
set2 = {5,6,7,8}
intersection_set = set1.intersection(set2)
print("set1 =",set1)
print("set2 =",set2)
print("intersection_set =",intersection_set)'''

#task3
'''a = {1,2,3,4,5}
b = {3,4,5,6,7}
print(a.difference(b))
print(b.difference(a))'''

#task4
'''a = {1,2,3,4,5}
b = {3,4,5,6,7}
print(a.symmetric_difference(b))'''

#task5
'''numbers = {10,20,30,40,20,50,60,20,70}
unique_numbers = list(set(numbers))
print("List of numbers:",numbers)
print("List of duplicate numbers:",unique_numbers)'''

#task6
'''a = {1,2,3}
b = {1,2,3,4,5,6}
print(a.issubset(b))
print(b.issubset(a))'''
#task7
'''a = {1,2,3}
b = {1,2,3,4,5,6}
print(a.issuperset(b))
print(b.issuperset(a))'''

#task8
'''a = {1,2,3,4,5}
a.add(6)
a.remove(2)
print(a)'''

#task9
'''classA = {"naresh","nikesh","sakthi","ramkumar"}
classB = {"nikesh","ramkumar","arun","bala"}
common_student = classA.intersection(classB)
print("common student :",common_student)'''

#task10
'''a = {1,2,3}
b = {4,5,6}
print(a.isdisjoint(b))'''

#dictionary
#task1
'''student = {"1.Name":"Nikesh",
           "2.Age":22,
           "3.Course":"B.tech(CYS)",
           "4.City":"Salem"}
print(student)'''

#task2
'''a ={"1.Python","2.Java","3.HTML"}
a.add({"4.CSS"})
print(a)'''

#task3
'''a = {"Name":"Nikesh","Age":22}
a.update({"Age":23})
print(a)'''

#task4
'''a = {1:"Python",2:"Java",3:"CSS"}
a.__delitem__(3)
print(a)'''

#task5
'''a = {1:"Python",2:"Java",3:"CSS"}
print(a.keys())'''

#task6
'''a = {1:"Python",2:"Java",3:"CSS"}
print(a.values())'''

#task7
'''a = {1:"Python",2:"Java",3:"CSS"}
if 1 in a:
    print("key exists")
else:
    print("key not exists")'''

#task8
'''a = [10,20,30,10,20,50,60]
frequency = {}
for i in a:
    frequency[i] = frequency.get(i,0)+1
print(frequency)'''

#task9
'''marks = {"arun":85,"bala": 92, "ram": 88, "nikesh":95}
highest = max(marks,key=marks.get)
print("student with highest marks:",highest)
print("marks:",marks[highest])'''

#task10
'''a ={1,2,3,4}
b = {5,6,7,8}
a.update(b)
print(a)'''

#scenario-based tasks
#list
#task1
cart = []
'''#Add products
cart.append("Book")
cart.append("Pen")
#Remove a products
cart.remove("Pen")
#Display all products
print("Shopping cart:")
for item in cart:
    print(item)'''

#task2
'''student = ["Nikesh","Naresh","Ram","Anu"]
name = input("enter student name:")
if name in student:
    print(name,"is present")
else:
    print(name,"is absent")'''

#Tuple
#task1
'''days = ("monday","tuesday","wednesday","thursday","friday","saturday","sunday")
num = int(input("enter a number (1-7):"))
print("days:",days[num-1])'''

#task2
'''GPS = (13.0827,80.2707)
print("latitude:",GPS[0])
print("longitude:",GPS[1])'''

#SET
#task1
'''visitors = {"v101","v102","v103","v104"}
print("unique visitors:")
print(visitors)'''

#task2
'''a = {"python","java","MySQL"}
b = {"python","HTML","MySQL"}
print("common coures:")
print(a&b)'''

#Dictionary
#task1
'''employee = {"ID":724,"Name":"Nikesh","Department":"IT","Salary":25000}
print(employee)'''

#task2
'''contact = {"Nikesh":8248660113,"Sampathkumar":9894885498}
name = input("enter name:")
print("phone number:",contact[name])'''

#task4
'''marks = {"nikesh":90,"naresh":85}
marks["naresh"] = 95
topper = max(marks,key=marks.get)
print("marks:",marks)
print("topper:",topper)'''

#task4
'''libery = {101:"python",102:"java",103:"MySQL"}
book = int(input("enter book id:"))
print("book name:",libery[book])'''

#challenge tasks
#tasks1
'''list = [10,20,30,40,50]
tuple = tuple(list)
set = set(tuple)
dictionary = {i:i for i in set}
print(list)
print(tuple)
print(set)
print(dictionary)'''

#tasks2
'''list = [1,2,3,2,4,3,5]
count = {}
for i in list:
    count[i] = count.get(i,0)+1
for i in count:
    if count[i]>1:
        print(i)'''

#tasks3
'''text = "apple mongo apple"
word = text.split()
count = {}
for i in word:
    count[i] = count.get(i,0)+1
print(count)'''

#tasks4
'''a = [1,2,3,4,5]
b = [3,4,5,6,7]
common = set(a) & set(b)
print(common)'''

#task5
students = {"nikesh":90,"naresh": 85}
print("students:",list(students.keys()))
print("marks:",students)
print("topper:",max(students,key=students.get))

