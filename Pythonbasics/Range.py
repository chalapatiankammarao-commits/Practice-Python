x = range(10)
print(x)
print(list(x))

x = range(3, 10)
print(x)
print(list(x))

x = range(2, 10, 2)
print(x)
print(list(x))

for i in range(10):
    print(i)

print(list(range(5)))
print(list(range(10)))
print(list(range(2, 10, 2)))
    
x = range(20)
print(x[2])
print(x[2:])
print(x[-2])
print(x[2:])
print(x[-1:-6])

#membership testing
x = range(2,20,3)
print(6 in x)
print(3 in x)

x = range(10)
print(len(x))

x = range(3, 19, 2)
print(len(x))
 