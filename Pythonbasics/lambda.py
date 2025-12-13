#lamda functions
x = lambda a: a + 5
print(x(5))
#number of arguments
y = lambda a, b : a * b
print(y(4, 6))

z = lambda a, b : a / b
print(z(7, 8))

c = lambda a, b, c : a + b + c
print(c(5, 7, 9))

#lambda in functions
def myfunc(n):
    return lambda a: a*n
y = myfunc(3)
print(y(33))

def inmyfunc(n):
    return lambda a : a*n
my = inmyfunc(5)
print(my(44))

def inourfunc(n):
    return lambda a : a*n
my = inourfunc(4)
our = inourfunc(5)
print(my(33))
print(our(77))

def inyourfunc(n):
    return lambda a: a/n
you = inyourfunc(9)
me = inyourfunc(5)
print(you(66))
print(me(44))

#lambda with in built in functions
#using map with lamda
numbers = [2,6,7,5,3]
doubled = list(map(lambda x : x*2,numbers))
print(doubled)

x = (8,6,7,3)
z = tuple(map(lambda y : y * 3,x))
print(z)

#using filter with lambda
numbers = [2,5,6,7,8,9]
oddnumbers = list(filter(lambda a : a % 2 != 0,numbers))
print(oddnumbers)

x = (2,6,8,5,9,3,)
y= tuple(filter(lambda v : v % 2 == 0,x))
print(y)

#using sorted with lambda
words = ("apple", "banana", "pie", "orange", "cherry")
sorted_words = sorted(words,key = lambda x: len(x))
print(sorted_words)

students = [("emil",45), ("tobias",46), ("linus",34)]
students_sorted =sorted(students,key = lambda x: x[0])
print(students_sorted)






