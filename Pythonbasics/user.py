import requests

#url = "https://jsonplaceholder.typicode.com/users"
#payload = {
 ##########print(res.json())



import requests

url = "https://jsonplaceholder.typicode.com/users"
payload = {
  'id': 1, 
  'name': 'Phani', 
  'username': 'Ankamma', 
  'email': 'Phani@123.biz',
  
  'id': 2, 
  'name': 'Ankamma', 
  'username': 'Ankamma', 
  'email': 'Ankamma@123.biz', 
    }  # your payload with 'id': 1

res = requests.put(f"{url}/1", json=payload)
print(res.status_code)
print(res.json())

