#iterator
'''a = ["adrin","keerthinath","vishradh","anasha"]
it = iter(a)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))'''

#using for loop
'''num = [10,20,30,40,]
it = iter(num)
for n in it:
    print(n)'''

#using string
'''text = "python"
it = iter(text)
while True:
    try:
        letter = next(it)
        print(letter)
    except StopIteration:
        break'''

#generate
'''def python():
    yield "nikesh"
    yield "keersh"
    yield "vishra"
    yield "anasha"

g = python()
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))'''

#using for loop
def number_generator():
    for i in range(1,6):
        yield i
    for num in number_generator():
        print(num)
