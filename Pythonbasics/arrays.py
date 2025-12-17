x = ["apple", "banana", "kiwi"]
print(x)

x = ["apple", "banana", "kiwi"]
print(x[0])

x = ["apple", "banana", "kiwi"]
x[0] = "orange"
print(x)

x = ["apple", "banana", "kiwi"]
print(len(x))

#looping array elements
x = ["apple", "banana", "kiwi"]
for y in x:
    print(y)
#adding elements
x = ["apple", "banana", "kiwi"]
x.append("orange")
print(x)

#removing elements
x = ["apple", "banana", "kiwi"]
x.pop(1)
print(x)
#using pop() method
x = ["apple", "banana", "kiwi"]
x.pop()
print(x)
#using remove method
x = ["apple", "banana", "kiwi"]
x.remove("banana")
print(x)

x = ["apple", "banana", "kiwi", "apple"]
u = x.count("apple")
print(u)

