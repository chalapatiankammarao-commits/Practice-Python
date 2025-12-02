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







