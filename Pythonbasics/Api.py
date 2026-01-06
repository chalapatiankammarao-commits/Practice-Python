
import requests

url = "https://jsonplaceholder.typicode.com/posts"
res = requests.get(url)
posts = res.json()
for post in posts:
    print("id:", post['id'])
    print("title:", post['title'])
# /users endpoint user name , user email
# /post, /users --- use POST creste 2 
# update 1 user in /Users, 1 in  /posts -- PUT
# delete 1 user in /isers, 1 in /posts

import requests
url = "http://api.open-notify.org/astros.json"
res = requests.get(url)
print(res.json())

import requests
url = "http://api.open-notify.org/astros.json"
res = requests.get(url)
print(res.json())

import requests
url = "https://jsonplaceholder.typicode.com/users"
res = requests.get(url)
users = res.json()
for user in users:
    print("id:",user['id'])
    print("name:",user['name'])
          
import requests
url = "https://jsonplaceholder.typicode.com/posts"
newpost = {
    "id" : "11",
    "Name" : "Ankammarao"  
}
res = requests.post(url,json = newpost)
if res.status_code == 201:
    print("successfully created")
    print(res.json())
else:
    print("not created")
    
import requests
url = "https://jsonplaceholder.typicode.com/posts"
newpost = {
    "id" : "11",
    "name": "Ankammarao" 
}
#res = requests.post(url, json=newpost)
if res.status_code == 201:
    print("User successfully created")
    print(res.json())
#else:
 #   print("Failed to create user")

import requests
url = "https://jsonplaceholder.typicode.com/users"
newuser = {
    "name" : "Phani",
    "id" : 11
}
res = requests.put(url,json = newuser)
print(res.json())



   
    



    
    
    

 