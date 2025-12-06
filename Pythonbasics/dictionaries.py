Employee = {
    "name" : "Phani",
    "age" : 25,
    "job" : "software"
}
car = {
    "brand" : "Tata",
    "colour" : "Black",
    "cost" : 800000
}
del Employee
car.clear()
#print(Employee)
print(car)

x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")
    
#dictionaries
d = {
    "name" : "pavan",
    "age" : "34",
    "qualification" : "m.tech"
} 
print (d)

c = {
    "name" : "pavan",
    "age" : "34",
    "qualification" : "m.tech"
} 
print(c["name"])

#duplicates not allowed
b = {
    "phone" : "android",
    "colour" : "white",
    "weight" : 6,
    "colour" : "black"
}
print(b)

#length of the dictionaries
a = {
    "name" : "pavan",
    "age" : "34",
    "qualification" : "m.tech"
}
print(len(a))

#the dict constructor
a = dict(naam = "apple", colour = "black", gender = "male")
print(a)

#access items
thisdict = {
    "name" : "kumar",
    "age" : 35,
    "colour" : "red"
}
x = thisdict["colour"]
print(x)
#to grt() model
thisdict = {
    "name" : "kumar",
    "age" : 35,
    "colour" : "red"
}
x = thisdict.get("colour")
print(x)
#use keys() model to get keys in the dictionary
thisdict = {
    "name" : "kumar",
    "age" : 35,
    "colour" : "red"
}
x = thisdict.keys()
print(x)
#add keys in dictionary
thisdict = {
    "name" : "kumar",
    "age" : 35,
    "colour" : "red"
}
thisdict["weight"] = 45
print(thisdict)

#get values()
thisdict = {
    "name" : "kumar",
    "age" : 35,
    "colour" : "red"
}
x = thisdict.values()
print(x)

#change valus
thisdict = {
    "name" : "kumar",
    "age" : 35,
    "colour" : "red"
}
thisdict["colour"] = "black"
print(thisdict)

#get items
thisdict = {
    "name" : "kumar",
    "age" : 35,
    "colour" : "red"
}

x = thisdict.items()
print(x)
thisdict["colour"] = "black"
print(x)

#check if key is exists
thisdict = {
    "name" : "kumar",
    "age" : 35,
    "colour" : "red"
}
if "age" in thisdict:
    print("yes, 'age' is existed")
    
#change items
thisdict = {
    "name" : "kumar",
    "age" : 35,
    "colour" : "red"
}
thisdict["colour"] = "black"
print(thisdict)

#update dictionary
thisdict = {
    "name" : "kumar",
    "age" : 35,
    "colour" : "red"
}
thisdict.update({"colour" : "yellow"})
print(thisdict)

#add items
thisdict = {
    "name" : "kumar",
    "age" : 35,
    "colour" : "red"
}
thisdict["height"] = 5.9
print(thisdict)

#update dictionary for adding new items
thisdict = {
    "name" : "kumar",
    "age" : 35,
    "colour" : "red"
}
thisdict.update({"power" : "34kg"})
print(thisdict)

#remoove items using pop()
thisdict = {
    "name" : "kumar",
    "age" : 35,
    "colour" : "red"
}
thisdict.pop("colour")
print(thisdict)

#using popitem()
thisdict = {
    "name" : "kumar",
    "age" : 35,
    "colour" : "red"
}
thisdict.popitem()
print(thisdict)

#using del
thisdict = {
    "name" : "kumar",
    "age" : 35,
    "colour" : "red"
}
del thisdict["colour"]
print(thisdict)

#using clear()
thisdict = {
    "name" : "kumar",
    "age" : 35,
    "colour" : "red"
}
thisdict.clear()
print(thisdict)

#copy dictionary
thisdict = {
    "name" : "kumar",
    "age" : 35,
    "colour" : "red"
}
x = thisdict.copy()
print(x)

#use dict() fun
thisdict = {
    "name" : "kumar",
    "age" : 35,
    "colour" : "red"
}
x = dict(thisdict)
print(x)

#nested dictionaries
ourdict = {
    "child1" : {
        "name" : "email",
        "adderess" : "kondapoor"
    },
    "child2" : {
        "age" : 23,
        "village" : "martur"
    },
    "child3" : {
        "announce" : "ment",
        "colleage" : "qis"   
    },
}
print(ourdict)
#create three dictionaries,then create one dictionary and that will contain the other three dictionaries
men1 = {
    "name" : "email",
    "adderess" : "kondapoor"
}
men2 = {
    "sir" : "angelina",
    "mother" : "gupta"
}
men3 = {
    "apple" : "ball",
    "king" : "bang"
}
mydict = {
    "men1" : men1,
    "men2" : men2,
    "men3" : men3
}
print(mydict)
print(mydict["men2"]["sir"])

child = {
    "name" : "email",
    "adderess" : "kondapoor"
}
x = child.fromkeys("name")
print(x)







    
    
    



