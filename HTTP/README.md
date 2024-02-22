google.com --> DNS lookup --> request from server



steps:
1. DNS adress --> Find the correct addres
2. Computer makes a rquest to a server
3. Server processes the request
4. Server issues a response
----> 2,3,4 ---> Request/Response cycle


DNS lookup : Like a phone book for internet. Takes domain names and turns into IP address. 

HHTP Headers: 
- sentwith both requests and responses
- provide additional info 
- accept :accepted content-types eg: html
- cache control
- user-agent

Response bodies:
404 --> not found
500 --> server side errors
3xx --> redirect
2xx --> Successful code

HTTP verbs:
- Get , Post --> common type of requests
- Get : Retrieve data, data paseed as query string, can e cahd, can be bookmarked, should have no side effects
- Post : useful for writing data. Eg: Writing comments on instagram, daa passedin request boy, can have side effects, not cached, cant be bookmarked 


API :
- Application Program Interface
- Allows you to get data from another application without needing to understand how the application works
- can send data back in diffrent forms
- eg of companies with APIS: Github, Spotify, Google

Request Headers:
- used to specify what kind of o/p can be requested. 
- requests.get(url,headers{__:__})
- requests.get(url,headers{__:__},params":{__:__})

Query String:
- pass data to the server as a part of the GET request  