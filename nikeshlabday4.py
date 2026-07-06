#task1
'''i=6
while i<=5:
    print(i)
    i+=1'''
#task2
'''i=1
while i<=10:
    print(i)
    i+=1'''

#task3
'''i=10
while i>=1:
    print(i)
    i-=1'''

#task4
'''i=2
while i<=20:
    print(i)
    i+=2'''

#task5
'''i=1
while i<=20:
    print(i)
    i+=2'''

#task6
'''i=1
s=0
while i<=50:
    s+=i
    i+=1
print(s)'''

#task7
'''n=6
i=1
while i<=10:
    print(n,"*",i,"=",n*i)
    i+=1,'''

#task8
'''n=12345
c=0
while n>0:
    c+=1
    n//=10
print(c)'''

#task9
'''n=12345
rev=0
while n>0:
    rev= rev * 10 + n % 10
    n//=10
print(rev)'''

#task11
'''a=int(input("enter a:"))
b=0
t=a
while t>0:
    d=t%10
    b=(b*10)+d
    t=t//10
print(b)
if b==a:
    print("palindrom")
else:
    print("not palindrom")'''

#task12
'''a=int(input("enter a:"))
b=0
c=1
t=a
while t>0:
    d=t%10
    b+=d
    c*=d
    t=t//10
print(b)
print(c)
if b==c:
    print("spy number")
else:
    print("not spy number")'''

#task13
'''n=1234
s=0
while n>0:
    s+=n%10
    n//=10
print(s)'''

#task14
'''n=12345
p=1
while n>0:
    p*=n%10
    n//=10
print(p)'''

#task15
'''n=153
t=n
s=0
while n>0:
    d=n%10
    s+=d**3
    n//=10
if t==s:
    print("armstrong")
else:
    print("not armstrong")'''

#task16
'''n=int(input("enter n:"))
l=0
while n>0:
    d=n%10
    if d>l:
        l=d
    n//=10
print(l)'''

#task17
'''n=int(input("enter n:"))
s=10
while n>0:
    d=n%10
    if d<s:
        s=d
    n//=10
print(s)'''

#task18
'''n=6
a=0
b=1
for i in range(n):
    print(a,end="")
    c=a+b
    a=b
    b=c
print(i)'''

#task19
n=int(input("enter n:"))
f=1
while n>0:
    f*=n
    n-=1
print(f)



    


    
