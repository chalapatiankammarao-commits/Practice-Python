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


    


  