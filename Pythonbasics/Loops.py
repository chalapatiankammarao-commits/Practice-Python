 #the while loops
x = 1
while x < 8:
    print(x)
    x += 1

#break statement
b = 1
while b < 9:
    print(b)
    if b == 4:
        break
    b += 1
#continue statement
d = 1
while d < 8:
    d += 1
    if d == 3:
        continue
    print(d)

#else statement
f = 1 
while f < 5:
    print(f)
    f += 1
else:
    print(" f is no longer less than 6")

v = 1
while v < 6:
    print(v)
    v += 1

g = 1
while g < 7:
    print(g)
    if g == 3:
        break
    g += 1
       
h = 1
while h < 7:
    h += 1
    if h == 3:
       continue
    print(h)

#for loops
fruits = {"apple", "banana", "design"}
for x in fruits:
    print(x)

c = ["mango", "chapati", "kingdom"]
for x in c:
    print(x)

#looping through a string
d = "banana"
for x in d:
    print(x)

#the break statement
mylife = ["simple", "entertainment", "comedy"]
for y in mylife:
    print(y)
    if y == "comedy":
        break
    
c = ('study', 'orange', 'follow')
for v in c:
    if v == "orange":
        break
    print(v)
#continue statement
x = ('coloumn', 'design','ginger')
for b in x:
    if b == 'design':
        continue
    print(b)

#the range function
for x in range(6):
    print(x)

for x in range (2, 6):
    print(x)

for u in range(2, 30, 3):
    print(u)

for t in range(2, 8):
    print(t)
else:
    print("not executed")
                       
for c in range(3, 36):
    if c == 25: break
    print(c)
else:
    print("no not at all")

#nested loops
c = ["school", "bench", "sparow"]
v = ["friend", "google",]
for l in c:
    for m in v:
        print(l, m)
        
#the pass statement
for f in [1, 4, 5]:
    pass              

for x in range(6):
  if x == 3:
    break
  print(x)
else:
  print("Finally finished!")
  
balance = 400
amount = 401
while balance >= amount:
    print(balance - amount)
    break
else:
    print("Error: insufficient funds")
    
code = int(input("enter the code"))
while code == 200:
    print("success")
    if code == 404:
        print("Not found")
    elif code == 500:
        print("server error")
    else:
        print("Unknown Status")
        break
    print(code)
    
    
code = int(input("enter status code"))
while True:
    if code == 200:
        print("Success")
        break
    elif code == 404:
        print("Not Found")
        break
    elif code == 500:
        print("Server Down")
        break
    else:
        print("else where")
        
x = 1
while x < 6:
    print(x)
    if x == 3:
        break
    x += 1
    
y = 1
while y < 6:
    y += 1
    if y == 3:
        continue
    print(y)


    
    
        

          
          