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

#fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

#(green, *tropic, red, blue) = fruits

#print(green)
#(tropic)
#print(red)
#print(blue)

#tuples
mytuple = ("aravind", "gunashekar", "sudheer", "gopal")
print(mytuple)

#allow duplicate
mytuple = ("aravind", "gunashekar", "sudheer", "gopal", "aravind", "sudheer")
print(mytuple)
#length of the tuple
mytuple = ("aravind", "gunashekar", "sudheer", "gopal")
print(len(mytuple))

#create tuple with one value

mytuple = ("anand",)
print(mytuple)

mytuple = ("anand")
print(mytuple)

#access tuple items with indexing

mytuple = ("aravind", "gunashekar", "sudheer", "gopal")
print(mytuple[2])

#negative index
mytuple = ("aravind", "gunashekar", "sudheer", "gopal")
print(mytuple[-4:-1])

#check if items is exits

mytuple = ("aravind", "gunashekar", "sudheer", "gopal")
if "aravind" in mytuple:
    print("yes, 'aravind' in mytuple")

#update tuple

mytuple = ("aravind", "gunashekar", "sudheer", "gopal")
x = list(mytuple)
x[2] = "sujatha"
mytuple = tuple(x)
print(mytuple)

mytuple = ("aravind", "gunashekar", "sudheer", "gopal")
x = list(mytuple)
x.append("govind")
mytuple = tuple(x)
print(mytuple)

#tuple to tuple adding
mytuple = ("aravind", "gunashekar", "sudheer", "gopal")
my_tuple = ("suraksha",)
mytuple += my_tuple
print(mytuple)

#remove items in tuples
mytuple = ("aravind", "gunashekar", "sudheer", "gopal")
x = list(mytuple)
x.remove("gunashekar")
mytuple = tuple(x)
print(mytuple)

#unpack tuples
mytuple = ("aravind", "gunashekar", "sudheer", "gopal")
print("aravind",)
print("gunashekar",)
print("sudheer",)
print("gopal",)

#using asterisk*
mytuple = ("aravind", "gunashekar", "sudheer", "gopal")
(green, yellow, *red) = mytuple
print(green)
print(yellow)
print(red)

#join tuples
mytuple = ("aravind", "gunashekar", "sudheer", "gopal")
my_tuple = ("gold", "silver", "platinum",)
z = mytuple + my_tuple
print(z)

#multiply the tuples
mytuple = ("aravind", "gunashekar", "sudheer", "gopal")
mynewtuple = mytuple*2
print(mynewtuple)

#tuple methods count, index
mytuple = ("aravind", "gunashekar", "sudheer", "gopal", "aravind")
x = mytuple.count("aravind")
print(x)

mytuple = ("aravind", "gunashekar", "sudheer", "gopal", "aravind")
x = mytuple.index("aravind")
print(x)














    
    



 



