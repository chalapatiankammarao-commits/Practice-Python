myTuple = ("Apple", "banana", "orange")
x = list((myTuple))
x[1] = "Grapes"
myTuple = tuple(x)
#print(myTuple)

a = ("Phani", "Ankamma", "Srikanth")
b = ("Ajay", "Ajay2" ,)
c = a + b

#print(c)


#fruits = ("apple", "banana", "cherry")
#print("apple")
#print("banana")


fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red, blue) = fruits

print(green)
print(tropic)
print(red)
print(blue)


