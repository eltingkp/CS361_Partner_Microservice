# CS361_Partner_Microservice
 Implementation of partner's microservice


# Project

Movie Database Wrapper 


# Description

This microservice creates a python object that contains a key value pair. The key is data, and the value is an API url. The python object is converted to a JSON string, and is sent to the server. The server creates a python object that receives and decodes the message from the client. It is then converted to JSON and a variable is created to hold the value (an API url) of the key from the JSON. A get request is sent to the API url, and the response is held in a variable. The server sends the response back to the client in bytes, and the client receives the response. 


# Requirements

Client requires the following modules:
- json
- socket

Server requires the following modules:
- json
- socket
- requests
  

# Installation 

Install modules as you normally would on your IDE 


# How to programmatically REQUEST data
- create socket
- connect to server
- create python object which is a key value pair. the key is "data" and the value is an api url
 - convert python object to json string
 - send json string to server in bytes

example:
```py
movie_object = {"data": "https://api.themoviedb.org/3/search/movie?include_adult=false&language=en-US&page=1"}

json_string = json.dumps(movie_object)

client.send(bytes(json_string, 'utf-8'))
```


# How to programmatically RECEIVE data
- create server socket
- bind socket
- initiate while loop, run while true
- client and server socket connect
- create data python object that receives and decodes message from client

example:
```py
while True:
    client, addr = server.accept()
    print("connected with", addr)

    data = client.recv(1024).decode()
```


# UML sequence diagram
![UML Sequence Diagram]
