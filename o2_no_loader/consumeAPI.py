import requests

url = 'http://localhost:5000/api/tariffs/AddMultipleTariffs'
headers = {'Accept' : 'application/json', 'Content-Type' : 'application/json'}
r = requests.post(url, data=open('plans.json', 'rb'), headers=headers)