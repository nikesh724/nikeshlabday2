#Esay Level tasks
#tasks1
'''def function():
    print("Hello world")
function()'''

#tasks2
'''def add(a,b):
    print("add:",a+b)
add(10,20)'''

#tasks3
'''def sub(a,b):
    print("sub:",a-b)
sub(10,20)'''

#tasks4
'''def mult(a,b):
    print("mult:",a*b)
mult(10,20)'''

#tasks5
'''def div(a,b):
    print("div:",a/b)
div(10,20)'''

#tasks6
'''def square(a):
    print("square:",a**2)
square(10)'''

#tasks7
'''def cube(a):
    print("cube:",a**3)
cube(10)'''

#tasks8
'''def even_odd(i):
    if i % 2 == 0:
        print("even")
    else:
        print("odd")
even_odd(10)'''

#tasks9
'''def largest(a,b):
    return a if a>b else b
print(largest(10,20))'''

#tasks10
'''def area_rectangle(lenght,width):
    return lenght*width
print(area_rectangle(10,20))'''

#intermediate level questions
#tasks
'''def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(5))'''

#tasks2
'''def prime(n):
    if n < 2:
        return True
    else:
        for i in range(2,n):
            if n % i == 0:
                return False
            else:
                return True
print(prime(5))
print(prime(10))'''

#tasks3
'''def fibonacci(n):
    a = 0
    b = 1
    for i in range(n):
        print(a,end=" ")
        a, b = b, a + b
num = int(input("enter number of terms:"))
fibonacci(num)'''

#tasks4
'''def reverse_string(s):
    return s[::-1]
text = input("enter string:")
print("reversed:",reverse_string(text))'''

#tasks5
'''def count_vowels(s):
    count = 0
    for ch in s.lower():
        if ch in 'aeiou':
            count += 1
        return count
text = input("enter a string:")
print("vowels:",count_vowels(text))'''

#tasks6
'''def palindrome(s):
    return s == s[::-1]
text = input("enter a string:")
if palindrome(text):
    print("palidrome")
else:
    print("not palidrome")'''

#tasks7
'''def second_largest(lst):
    lst = list(set(lst))
    lst.sort()
    return lst[-2]
numbers = [10,20,30,40,50]
print("second largest:",second_largest(numbers))'''

#tasks8
'''def remove_duplicates(lst):
    return list(set(lst))
numbers = [1,2,2,3,4,4,5]
print(" After removing duplicates:", remove_duplicates(numbers))'''

#tasks9
'''def char_frequency(s):
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch,0) + 1
    return freq
print(char_frequency("banana"))'''

#tasks10
'''def sum_list(lst):
    return sum(lst)
print(sum_list([10,20,30,40]))'''

#lambda function
#tasks1
'''a = lambda x,y: x+y
print(a(10,5))'''

#tasks2
'''a = lambda n: n**2
print(a(10))'''

#tasks3
'''a = lambda n: n**3
print(a(10))'''

#tasks4
'''is_even = lambda n: n % 2 == 0
print(is_even(10))
print(is_even(7))'''

#tasks5
'''largest = lambda a,b: a if a > b else b
print(largest(10,25))'''

#intermediate
#tasks6
'''students = [("nikesh",22),("ram",21),("john",19),("ravi",20)]
print(sorted(students,key=lambda x:x[1]))'''

#tasks7
'''marks = [("nikesh",90),("naresh",80),("john",75),("ravi",65)]
print(sorted(marks,key=lambda x:x[1]))'''

#tasks8
'''words = ["python","java","HTML","c++"]
print(max(words,key=len))'''

#tasks9
'''discount = lambda p:p*0.9
print(discount(500))'''

#tasks10
'''fahrenheit = lambda x: (x*9/5)+32
print(fahrenheit(10))'''

#map function
#tasks1
'''a = [10]
b = list(map(lambda x:x**2,a))
print(b)'''

#tasks2
'''a = ["nikesh","naresh","johm","ravi"]
b = list(map(lambda x: x.upper(),a))
print(b)'''

#tasks3
'''a = [10,20,30,40,50]
b = list(map(lambda x: x+10,a))
print(b)'''

#tasks4
'''a = [2,3,4,5,6,7]
b = list(map(lambda x: x*2,a))
print(b)'''

#tasks5
'''a = [10,20,30]
b = list(map(lambda x: x**3,a))
print(b)'''

#intermediate
#tasks6
'''a = [10,20,30]
b = list(map(lambda x: x*9/5+32,a))
print(b)'''

#tasks7
'''worker = [20000,25000,30000,35000]
salary = list(map(lambda x: x+5000,worker))
print(salary)'''

#tasks8
'''a = ["cat","apple","dog"]
b = list(map(len,a))
print(b)'''

#tasks9
'''a = ["NIKESH","NARESH","JOHN","RAVI"]
b = list(map(lambda x: x.lower(),a))
print(b)'''

#tasks10
'''a = [100,200,300]
b = list(map(lambda x: x*1.18,a))
print(b)'''

#filter function
#tasks1
'''num = [1,2,3,4,5,6]
even = list(filter(lambda x: x % 2 == 0, num))
print(even)'''

#tasks2
'''num = [1,2,3,4,5,6]
odd = list(filter(lambda x: x % 2!= 0, num))
print(odd)'''

#tasks3
'''num = [-1,2,-3,4,-5,0]
positive = list(filter(lambda x: x > 0, num))
print(positive)'''

#tasks4
'''num = [-1,2,-3,4,-5,0]
negative = list(filter(lambda x: x < 0, num))
print(negative)'''

#tasks5
'''num = [20,30,40,50,60]
greater = list(filter(lambda x: x > 50, num))
print("greater than 50:",greater)'''

#intermediate
#tasks6
'''num = [2,3,4,5,6,7,8]
prime = list(filter(lambda x : x > 1 and all(x % i  for i in range(2,x)),num))
print(prime)'''

#tasks7
'''students = [50,60,70,75,80]
scored = list(filter(lambda x: x > 75, students))
print(scored)'''

#tasks8
'''names = ["Asha","Nikesh","Naresh"]
starting = list(filter(lambda x: x.startswith("A"), names))
print(starting)'''

#tasks9
'''products = [1000,500,1200,700,1500]
costing = list(filter(lambda x: x > 1000, products))
print(costing)'''

#tasks10
'''employees = [10000,20000,30000,40000,50000]
earning = list(filter(lambda x: x > 30000, employees))
print(earning)'''

#recursion
#tasks1
'''def value(n):
    if n>10:
        return
    print(n)
    value(n+1)
value(1)'''

#tasks2
'''def value(n):
    if n<1:
        return
    print(n)
    value(n-1)
value(10)'''

#tasks3
'''def sum(n):
    return 0 if n==0 else n+sum(n-1)
print(sum(5))'''

#tasks4
'''def factorial(n):
    return 1 if n==0 else n*factorial(n-1)
print(factorial(5))'''

#tasks5
'''def name(n):
    if n == 0:
        return
    print("Nikesh")
    name(n-1)
name(5)'''

#intermediate
#tasks6
'''def fibonacci(a,b,n):
    if n == 0:
        return
    print(a, end=" ")
    fibonacci(b,a+b,n-1)
fibonacci(0,1,6)'''

#tasks7
'''def reverse(n):
    return n if len(n)==0 else reverse(n[1:]) + n[0]
print(reverse("python"))'''

#tasks8
'''def GCD(a,b):
    return a if b==0 else GCD(b,a%b)
print(GCD(5,6))'''

#tasks9
'''def count(n):
    return 1 if n<10 else 1+ count(n//10)
print(count(12345))'''

#tasks10
'''def palindrome(n):
    return "palindrome" if n==n[::-1] else "not palindrome"
print(palindrome("madam"))'''

#scenario-based questions
'''#tasks1
def result(m):
    if m >= 75:
        print("distinction")
    elif m >= 60:
        print("first class")
    elif m >= 50:
        print("second class")
    else:
        print("fail")
result(90)'''

#tasks2
'''def salary(n):
    print("salary:",n+n*10/100)
salary(20000)'''

#tasks3
'''def bill(e):
    print("bill:",e*5)
bill(100)'''

#tasks4
'''def voting_eligibility(age):
    if age >= 18:
        print("eligibility")
    else:
        print("not eligibility")
voting_eligibility(22)'''

#tasks5
'''def shop(a):
    GST = a*18/100
    print("total:",a+GST)
shop(1000)'''

#tasks6
'''def bank(balance,deposit,withdrawal):
    print("balance:",balance+deposit-withdrawal)
bank(1000,500,200)'''

#tasks7
'''def attend(p,t):
    print("attend:",p/t*100,"%")
attend(19,20)'''

#tasks8
'''def exam(a,b,c):
    total = a+b+c
    percentage = total/3
    grade = "A"if percentage>=80 else "B"
    print(total,percentage,grade)
exam(90,80,70)'''

#tasks9
'''def fine(days):
    print("fine:",days * 5)
fine(4)'''

#tasks10
def ticket(seats):
    print("cost:",seats * 150)
ticket(3)




















