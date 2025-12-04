#python if
a = 10
b= 5
if a > b:
    print("yes, a is grater than b")

number = 15
if number >0:
    print("yes number is grater than zero")

is_logi_ur = True
if is_logi_ur:
    print("yes")      
#if elif
x = 10
y = 15
if x > y:
    print("no")
elif x ==y:
    print("yes")
elif x < y:
    print("o my god")
    
#else
d = 23
g = 35
if d > g:
    print("yes")
elif d == g:
    print("no")
else :
    print("nothing")

username = "emil"
if len(username) > 0:
    print(f"welcome, {username}!")
else:
    print("no")
    
#shorted hand if... else  ternary operator
a = 54
c = 67
print("z") if a > c else ("b")

w = 10
x = 7
bigger = w if w > x else x
print("mommy",bigger) 
#multiple conditionds in one line
f = 56
g = 65
print("A") if f > g else print("B") if f < g else print("H")

#logical operators 'and' 'or' 'not'
a = 300
d = 400
c = 100
if a > c and a < d:
    print("noise is there")
    
a = 290
b = 540
if a > b or a < b:
    print("the sun raises in the east")
 
w = 23
d = 45
if not w > d:   
    print("do you know")
    
#nested if
x = 45
if x > 10:
    print("above ten")
    if x > 20:
        print("above twenty")
    else:
        print("above nothing")

#pass statement
a = 19
c = 45
if a > c:
    pass
else:
    print("pass will pass")
        
