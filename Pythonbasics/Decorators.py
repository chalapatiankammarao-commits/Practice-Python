def changecase(func):
    def myinner():
        return func().upper()
    return myinner
@changecase
def myFunction():
     return "Phani Bhardwaj"
print(myFunction()) 

#decorators
def my_func(fun):
    def innerfunc():
        return fun().upper()
    return innerfunc
@my_func
def myfunc():
    return "Hello Sally"
print(myfunc())

def my_function(func):
    def innerfun():
        return func().upper()
    return innerfun
@my_function
def ourfunc():
    return "bhagavan"
print(ourfunc())

def our_func(a):
    def innerfunc():
        return a().upper()
    return innerfunc
@our_func
def inourfunc():
    return "hello bagavan"
def inmyfunc():
    return "hello kavya"
print(inmyfunc())
print(inourfunc())

#arguments in the decorated functions
def myfunc(func):
    def innerfun(x):
        return func(x).upper()
    return innerfun
@myfunc
def inmyfunc(nam):
    return "hello " + nam
def inourfunc():
    return "hello guntur"
print(inmyfunc("john"))
print(inourfunc())

#*args and **kwargs
def inmyfunc(fun):
    def innerfunc(*args, **kwargs):
        return fun(*args, **kwargs).upper()
    return innerfunc
@inmyfunc
def inourfunc(name):
    return "good evening " + name
def inyoufunc(key):
    print(inourfunc("aravind"))
    print(inyoufunc("govind"))

    
