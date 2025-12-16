#recursion
def myfunc(n):
    if n <= 0:
        print("Done")
    else:
        print(n)
        myfunc(n-1)
myfunc(5)

def inmyfunc(n):
    if n >= 5:
        print("yes")
    else:
        print(n)
        inmyfunc(n+1)
inmyfunc(3)

#base case and recursive case
def factorial(n):
    #base function
    if n == 0 or n == 1:
        return 1
    #recursive function
    else:
        return n * factorial(n-1)
print(factorial(5))

#Fibonacci sequence
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(7))

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(8))
#recursion with lists
def sum_list(numbers):
    if len(numbers) == 0:
        return 0
    else:
        return numbers[0] + sum_list(numbers[1:])
my_list = [1,6,9,0]
print(sum_list(my_list))
#find the maximum value
def find_max(numbers):
    if len(numbers) == 1:
        return numbers[0]
    else:
        max_of_rest = find_max(numbers[1:])
        return numbers[0] if numbers[0] > max_of_rest else max_of_rest
my_list = [1,9,7,3]
print(find_max(my_list))

#recursion depth limit
import sys
print(sys.getrecursionlimit()) 

import sys
sys.setrecursionlimit(2000)
print(sys.getrecursionlimit())


x = 1
while x < 9:
    print(x)
    if x == 3:
        break
    x += 1
    
c = 0
while c < 3:
    print(c)
    c += 1
    
v = 1
while v < 7:
    v += 1
    if v == 3:
        continue
    print(v)
g = 0
while g < 8:
    print(g)
    if g == 3:
        break
    g += 1 
    
h = 0
while h < 10:
    h += 1
    if h == 3:
        continue
    print(h) 

x = 76
if x > 80:
    print("are you sure")
elif x > 50:
    print("yes iam sure")
else:
    print("it's ok")
    