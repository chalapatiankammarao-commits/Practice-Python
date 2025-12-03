#python sets set
a = {"apple","banana","chai","dog"}
print(a)
#duplicate items not allowed
#set = {"goat", "elephant", "america", "loin", "elephant"}
print(set)

#True or 1 is considered as the same values,and are treated as duplicates
x = {1, 3, 8, 0, 6, 1, True}
print(x)

#False or 0 is considered as the same values,and are treated as duplicates
x = {1, 3, 8, 0, 6, 1, True, False}
print(x)

#set = {"abc", 34, True, 40, "male"}
print(set)

#type of my set
#set = {"abc", 34, True, 40, "male"}
print(type(set))

#The set constructer
#myset = set(("appollo", "keerthi", "navodaya", "kakinada"))
#print(myset)

#access set items
#a= {"abc", 34, True, 40, "male"}
for x in a:
    print(x)
    
set = {"abc", 34, True, 40, "male"}
print("male" in set)

#add method
#
#set = {"abc", 34, True, 40, "male"}
set.add("apple")
print(set)

#add sets using update method
set = {"abc", 34, True, 40, "male"}
myset = ("appollo", "keerthi", "navodaya", "kakinada")
set.update(myset)
print(set)

#add any iterable
set = {"abc", 34, True, 40, "male"}
mylist = ["appollo", "keerthi", "navodaya", "kakinada"]
set.update(mylist)

#remove set items
f = {"appollo", "keerthi", "navodaya", "kakinada"}
f.remove("keerthi")
print(f)

m = {"appollo", "keerthi", "navodaya", "kakinada"}
m.discard("appollo")
print(m)

d = {"appollo", "keerthi", "navodaya", "kakinada"}
d.pop()
print(d)

k = {"appollo", "keerthi", "navodaya", "kakinada"}
k.clear()
print(k)

#join sets
#there are several ways to join the sets in python
#union(), update(),intersection(),symmetric_difference()

#union
set1 = {"apple", "sentence", "uploaded"}
set2 = {"happy", "sad", "mad"}
set3 = set1.union(set2)
print(set3)

a = {"apple", "sentence", "uploaded"}
b = {"happy", "sad", "mad"}
c = a|b
print(c)

#update()
myset = {"apple", "sentence", "uploaded"}
thisset = {"happy", "sad", "mad"}
myset.update(thisset)
print(myset)

#join a set and tuple with union

a = {"mom", "dad", "sister"}
b = ("brother", "elder brother", "elder sister")
c = a.union(b)
print(c)

#intersection ,kepp only duplicates
a = {"banana", "orange", "cherry", 0, True}
b = {"apple", "kiwi", "banana", 1, False}
c = a.intersection(b)
print(c)
#using & symbol 
a = {"banana", "orange", "cherry"}
b = {"apple", "kiwi", "banana"}
c = a & b
print(c)

#intersection_update
a = {"banana", "orange", "cherry"}
b = {"apple", "kiwi", "banana"}
a.intersection_update(b)
print(a)

#difference
a = {"banana", "orange", "cherry"}
b = {"apple", "kiwi", "banana"}
c = a.difference(b)
print(c)
#using (-) symbol
a = {"banana", "orange", "cherry"}
b = {"apple", "kiwi", "banana"}
c = a - b
print(c)
#difference_update method
a = {"banana", "orange", "cherry"}
b = {"apple", "kiwi", "banana"}
a.difference_update(b)
print(a)

#symmetric difference
a = {"banana", "orange", "cherry"}
b = {"apple", "kiwi", "banana"}
c = a.symmetric_difference(b)
print(c)
#using ^ symbol 
a = {"banana", "orange", "cherry"}
b = {"apple", "kiwi", "banana"}
c = a ^ b
print(c)

#symmetric_difference_update
a = {"banana", "orange", "cherry"}
b = {"apple", "kiwi", "banana"}
a.symmetric_difference_update(b)
print(a)

#python frozenset
a = frozenset({"apple", "banana", "chip"})
print(a)



