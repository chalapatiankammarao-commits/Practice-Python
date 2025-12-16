#python functions
def myfun():
    print("the sky is blue")
myfun()
#call same function multiple times
def myfunc():
    print("avilable for work")
myfunc()
myfunc()
myfunc()
myfunc()

def forienheat_to_celsius(forienheat):
    return(forienheat - 32) * 5 / 9
print(forienheat_to_celsius(77))
print(forienheat_to_celsius(85))
print(forienheat_to_celsius(92))

#return statement
def my_func():
    return "hello welcome to our colleage"
print(my_func())

#pass statement
def my__func():
    pass

#function arguments
def our_func(fname):
    print (fname + " reference")
our_func("emil")
our_func("jumboo")
our_func("allow")

def infunc(name):
    print("hello " + name)
infunc("emil")
infunc("dog")
infunc("clear")

#number of arguments
def my_Func(name , reference):
    print(name + " " + reference)
my_Func("emil", "develop")
my_Func("jungle", "hello")
my_Func("difficult", "above")

#default parameters
def newfunc(name = "angle"):
    print("hello" , name)
newfunc("emil")
newfunc("offer")
newfunc("jungle")
newfunc()
#key=value syntax
def fun(name, colleage):
    print("my", name + "'s name is " + colleage)
fun(name = "dog", colleage = "buddy" )  
#positional arguments
def fun(name, colleage):
    print("my", name + "'s name is " + colleage)
fun("dog", "buddy")

def ourfun(name, colleage):
    print("my", name + "'s name is " + colleage)
ourfun("buddy", "dog")
#mixing postional and keywords arguments
def fun(name, colleage):
    print("my", name + "'s name is " + colleage)
fun("dog", colleage = "buddy")
 
#passing different data types
def ufunc(fruits):
    for x in fruits:
        print(x)
x = ["apple", "banana", "kiwi"]
ufunc(x) 

def our_fun(person):
    print("Name:", person["name"])
    print("Age:", person["age"])
my_person = {"name": "email", "age": 25}
our_fun(my_person)

#return values
def this_fun(x, y):
    return x + y
result = this_fun(5, 3)
print(result)
#return different data types
def tofunc():
    return["apple", "banana", "cherry"]
fruits = tofunc()
print(fruits[0])
print(fruits[1])
print(fruits[2])

#positional arguments
def dfun(name, /):
    print("hello", name)
dfun("emil")
#key word arguments
def gfun(* , name):
    print("hello", name)
gfun(name = "emil")
#combination of postional only abd keyword only
def otherfun(a, b, /, *, c, d):
    return a + b + c + d 
result =  otherfun(5 , 10, c=15, d=20)
print(result)

# *args and **keyargs
def my_newfunction(*kids):
    print("my yongest child is " + kids[2])
my_newfunction("emil", "tobis", "linus")

#what is *args
def our_function(*args):
    print("type of the funtion:", type(args))
    print("fist arguments:", args[0])
    print("second arguments:", args[1])
    print("third arguments:", args[2])
    print("all arguments:", args)
our_function("emil", "tobias", "linus")

#using *args and regulararguments
def inmyfunc(names, *args):
    for name in args:
        print(names , name)
inmyfunc("emil", "apple", "console", "ultra", "content")

#practical example in *args
def inourfunc(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total
print(inourfunc(1, 2, 3))
print(inourfunc(10, 20, 30, 40,))
print(inourfunc(5))

def inmyfunc(*dats):
    if len(dats) == 0:
      return None
    max_value = dats[0]
    for x in dats:
        if x > max_value:
         max_value = x
    return max_value
print(inmyfunc(3, 7, 2, 9, 1))

#arbitary keywords argumens - *args
def in_myfunc(**args):
    print("his lastname is " + args["name"])
in_myfunc(fame = "fobis" , name = "rao")

def inmy_func(**myvar):
    print("type:", type(myvar))
    print("name:", myvar["name"])
    print("age:", myvar["age"])
    print("all data:", myvar)
inmy_func(name = "emil", age = 45, city = "banglore")
#using **kwargs with regular arguments
def inour_fun(username, **details):
    print("username:", username)
    print("additional details:")
    for key, value in details.items():
        print("", key + ":", value)
inour_fun("emil123", age = 25, city = "oslo", hobby = "coding")

#combine *args and **kwargs
def inmy_ourfunc(title, *args, **kwargs):
    print("title:", title)
    print("positional arguments:", args)
    print("keyword arguments:", kwargs)
inmy_ourfunc("user info", "emil", "tobis", age = 25, city = "oslo")

#unpack arguments
#unpacking lists with *
def myourfunc(a, b, c):
    return a + b + c
numbers = [1, 2, 3]
result = myourfunc(*numbers)
print(result)

#unpacking dictionaries with **
def myinourfunc(fname, lname):
    print("hello", fname, lname)
person = {"fname" : "emil", "lname" : "reference"}
myinourfunc(**person)

def get_greeting():
    print("hello from a function")
get_greeting()
#create withdraw function
def withdraw(amount,balance):
    if amount < balance:
        return (balance - amount)
    if amount > balance:
        return ("error: insufficient funds")
print(withdraw(200,0))
#create calculate grade function
def calculate_grade(marks_list):
    if not marks_list:
        return 0, 0, "F"
    total = sum(marks_list)
    average = total / len(marks_list)
    if average >= 90:
        grade = "A"
    elif average >= 80:
        grade = "B"
    elif average >= 70:
        grade = "c"
    elif average >= 60:
        grade = "D"
    else:
        garde = "F"
    return total, average, grade 
marks_list = [90, 85, 72,84]
print(calculate_grade(marks_list))

#create function get status code
def get_status(code):
    if code == 200:
        return "success"
    elif code == 404:
        return "not found"
    elif code == 500:
        return "server Error"
    else:
        return "Unknown Status"
print(get_status(500))

def myfun():
    print("hello google")
myfun()

def inmyfunc():
    return "what is your name"
print(inmyfunc())
print(inmyfunc())


def inourfunc(fname):
    return("apple is " + fname)
print(inourfunc("sweet"))
print(inourfunc("bad"))
print(inourfunc("hot"))

def youfunc(name):
    print("hello " + name)
youfunc("beautiful")



       
        
         

        
  