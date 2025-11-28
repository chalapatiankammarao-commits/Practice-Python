x = 6
y = "phani"
#print(x, '' , end = '')
#print(y) 

a = [1,2,3,4,5,6]
#print(a)

f = ["orange", "banana", "cherry"]
#print(f)

#global variable vs local variable

y = "awesome"

def myfunc():
    global y
    y = "fantastic"
print("Python is " + y)
myfunc()
    
print("Python is " + y) 