import requests

# url = "https://www.google.com"
# response = requests.get(url)

# print(f"the response code of {url} is  {response.status_code}")

url = "https://icanhazdadjoke.com/search"
response = requests.get(url,headers={"Accept":"text/plain"})
response1 = requests.get(url,headers={"Accept":"application/json"},params={"term":"cat"})

#print(response1.text)
#printtext)) # this is a string ---> "{"":"""}"
#print(response1.json())
data = response1.json() #this will be a dictionary and not string.  --->{"":""}
print(data['results'])

'''
{"id":"1gyskqz51ob","joke":"What did the father tomato say to the baby tomato whilst on a family walk? Ketchup.","status":200}

{'id': '1gyskqz51ob', 'joke': 'What did the father tomato say to the baby tomato whilst on a family walk? Ketchup.', 'status': 200}
'''


