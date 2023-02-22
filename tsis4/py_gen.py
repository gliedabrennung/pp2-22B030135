def generator(N):
    for i in range(N): 
        yield i**2
a = int(input())
for x in generator(a):
    print (x)

def generator(n):
    for i in range(n): 
        if i % 2 == 0:
            yield i
n = int(input())
for x in generator(n):
    print (x)

def generator(b):
    for i in range(b): 
        if i % 3 == 0:
            yield i
        elif i % 4 == 0:
            yield i
b = int(input())
for y in generator(b):
    print (y)

def squares(a1, b1):
    for i in range(a1, b1): 
        yield i**2
a1 = int(input())
b1 = int(input())
for h in squares(a1, b1):
    print (h)

def generator(n1):
    for i in reversed(range(n1)): 
        yield i
n1 = int(input())
for w in generator(n1):
    print (w)
