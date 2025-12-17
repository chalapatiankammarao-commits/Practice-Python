#generators yield keyword
def myfunc(n):
    count = 1
    while count<= n:
        yield count
        count += 1
for num in myfunc(5):
    print(num)
    
def infunc(n):
    x = 1
    while x<= n:
        yield x
        x += 1
for y in infunc(7):
    print(y)
    
#using next with generators
def ourfunc():
    yield "emil"
    yield "mango"
    yield "apple"
gen = ourfunc()
print(next(gen))
print(next(gen))
print(next(gen))
#generators save memory
def myinfunc(n):
    for i in range(n):
        yield i
        
gen = myinfunc(1000000)
print(next(gen))
print(next(gen))
print(next(gen))

#using next with generator
def youfunc():
    yield "emil"
    yield "apple"
    yield "banana"
gen = youfunc()
print(next(gen))
print(next(gen))
print(next(gen))

#generator expression
list_com = [x *x for x in range(5)]
print(list_com)

gen_exp = (x * x for x in range(5))
print(gen_exp)
print(list(gen_exp))
#using generator expression sum of squares
gen_exp = sum(x * x for x in range(10))
print(gen_exp)


def inourfnc():
    yield 1
    yield 2
    yield 3
for value in inourfnc():
    print(value)
    
def inyoufunc(n):
    count = 1
    while count <= n:
        yield count
        count += 1
for i in inyoufunc(9):
    print(i)

def fibonacci():
    a , b = 0, 1
    while True:
        yield a
        a, b = b, a+b
gen = fibonacci()
for _ in range(100):
    print(next(gen))
    

    
    
    


        
    

