#python lists
#list
mylist = ["apple", "banana", "orange", "mangoo"]
print(mylist)

#allow duplicates
x = ["apple", "banana", "cherry", "orange", "cherry"]
print(x)

#list length
x = ["apple", "banana", "kiwi", "mangoo"]
print(len(x))

#list itrms - data types
x = [23, 45, 56,78]
y = ["apple", "banana", "cat"]
z = [True, False, False]
print(x, y, z)

#access list items
x = ["apple", "banana", "orange"]
print(x[2])

#nagetive index
x = ["apple", "banana", "orange"]
print(x[-2])

#range of indexes
x = ["apple", "banana", "orange", "kiwi", "orange", "apple"]
print(x[2:5])

x= ["apple", "banana", "orange", "kiwi", "orange", "apple"]
print(x[-5:-2])


x= ["apple", "banana", "orange", "kiwi", "orange", "apple"]
print(x[2:])


x= ["apple", "banana", "orange", "kiwi", "orange", "apple"]
print(x[:5])


x= ["apple", "banana", "orange", "kiwi", "orange", "apple"]
print(x[:])

#check items exist

x = ["apple", "banana", "orange", "kiwi", "orange", "apple"]
if "apple" in x:
    print("yes, 'apple' in x")
    
#change list items
x = ["apple", "banana", "orange", "kiwi", "orange", "apple"]
x[1] = "black bukket"
print(x)

#change a range of item values
x = ["apple", "banana", "orange", "kiwi", "orange", "apple"]
x[2:5] = ["black current", "water melon", "pinapple"]
print(x)

y=["apple", "banana", "orange", "kiwi", "orange", "apple"]
y[1:3] = ["water melon"]
print(y)

#insert items
x = ["apple", "banana", "orange", "kiwi", "orange", "apple"]
x.insert(2, "water melon")
print(x)

#add list items ,append method
x = ["apple", "banana", "orange", "kiwi", "orange", "apple"]
x.append("juice")
print(x)

#extend list
x = ["apple", "banana", "orange", "kiwi", "orange", "apple"]
y = ["collage", "collageId",]
x.extend(y)
print(x)
#add any iterable (like tuple,sets,dictionaries etc)
x = ["apple", "banana", "orange", "kiwi", "orange", "apple"]
y = ("jungle", "photo")
x.extend(y)
print(x)
#remove spacified item
x = ["apple", "banana", "orange", "kiwi", "orange", "apple"]
x.remove("orange")
print(x)


x = ["apple", "banana", "orange", "kiwi", "orange", "apple", "banana"]
x.remove("banana")
print(x)

#remove spacified index we can use pop()
x = ["apple", "banana", "orange", "kiwi", "orange", "apple"]
x.pop(2)
print(x)

x = ["apple", "banana", "orange", "kiwi", "orange", "apple"]
x.pop()
print(x)

x = ["apple", "banana", "orange", "kiwi", "orange", "apple"]
del x[0]
print(x)


x = ["apple", "banana", "orange", "kiwi", "orange", "apple"]
x.clear()
print(x)
#sort lists
x = ["apple", "banana", "orange", "kiwi", "orange", "apple"]
x.sort()
print(x)

#sort numerically
x = [100, 50, 30, 45, 56]
x.sort(reverse = True)
print(x)

x = ["apple", "banana", "Oange", "Kwi", "orange", "apple"]
x.sort()
print(x)

x = ["apple", "orange", "kiwi", "orange", "apple"]
x.sort(key = str.lower)
print(x)
#copy a list use copy()

x = ["apple", "banana", "orange", "kiwi", "orange", "apple"]
y = x.copy()
print(y)
#use list()

x = ["apple", "banana", "orange", "kiwi", "orange", "apple"]
y = list((x))
print(y)

#use slice operator [:]
x = ["apple", "banana", "orange", "kiwi", "orange", "apple"]
y = x[:]
print (y)

#join lists

list1 = ["apple", "banana", "orange", "kiwi", "orange", "apple"]
list2 = [2, 5, 8, 4]
list3 = list1 + list2
print(list3)

#using apend() join the lists
list1 = ["apple", "banana", "orange", "kiwi", "orange", "apple"]
list2 = [2, 5, 8, 9,]
for x in list2:
    list1.append(x)
    print(list1)

#using extend method jon the lists
list1 = ["apple", "banana", "orange", "kiwi", "orange", "apple"]
list2 = [2, 5, 8, 9,]
list1.extend(list2)
print(list1)

x =  ["apple", "banana", "orange", "kiwi", "orange", "apple"]
y = [1, 2, 3,4]
x.append(y)
print(x)

x = ["apple", "banana", "orange", "kiwi", "orange", "apple"]
x.clear()
print(x)

x =  ["apple", "banana", "orange", "kiwi", "orange", "apple"]
y = x.copy()
print(y)

x =  ["apple", "banana", "orange", "kiwi", "orange", "apple"]
y = x.count("apple")
print(y)

x = ["apple", "banana", "orange", "kiwi", "orange", "apple"]
y = (1, 3, 5, 7)
x.extend(y)
print(x)

x = ["apple", "banana", "orange", "kiwi", "orange", "apple"]
x.insert(2, "mangoo")
print(x)

x = ["apple", "banana", "orange", "kiwi", "orange", "apple"]
x.pop(2)
print(x)

x = ["apple", "banana", "orange", "kiwi", "orange", "apple"]
x.remove("orange")
print(x)

x = ["apple", "banana", "orange", "kiwi", "orange", "apple"]
x.reverse()
print(x)

X = ["apple", "banana", "orange", "kiwi", "orange", "apple"]
X.clear()
print(X)

    
































myList = ["apple", "banana", "cherry", "date", "cherry"]
#fruits = ["grapes", "mango", "kiwi"]
myList.reverse()
print(myList)






