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
def inourfunc(key):
    return "good evening " + key
@inmyfunc
def inourfuncc(name):
    return "hello madav and " + name
print(inourfunc(key = "govind"))
print(inourfuncc("aravind"))

#decorator with arguments
def inmyfunc(n):
    def inmyfunc(func):
        def myinne():
            if n == 1:
                a = func().lower()
            else:
                a = func().upper()
            return a
        return myinne
    return inmyfunc
@inmyfunc(1)
def mynewfunc():
    return "hello louis"
print(mynewfunc())

    
    



    
