# CS361_Partner_Microservice
 Implementation of partner's microservice


# Project

Movie Database Wrapper 


# Description

This microservice is written in Python. It receives and decodes messages that contain a URL from the client via sockets. The microservice then makes an HTTP request to get the data from the URL and sends it back to the client via sockets. 


# Requirements

Client requires the following Python modules:
- json
- socket

Server requires the following Python modules:
- json
- socket
- requests
  

# Installation 

Install modules as you normally would in your IDE.


# How to programmatically REQUEST data

- Create a socket
- Connect to server
- Create Python object which is a single key value pair. The key is `data` and the value is an API URL.
- Convert Python object to JSON string
- Send JSON string to server in bytes

example:
```py
movie_object = {"data": "https://api.themoviedb.org/3/search/movie?include_adult=false&language=en-US&page=1"}

json_string = json.dumps(movie_object)

client.send(bytes(json_string, 'utf-8'))
```


# How to programmatically RECEIVE data

- Use previously created socket connection
- Receive data from server in bytes
- Decode data to JSON string

example:
```py
    data = client.recv(1024).decode()
```

example of data received: 
```json
{
    "page": 1,
    "results": [
        {
            "adult": false,
            "backdrop_path": null,
            "genre_ids": [
                35
            ],
            "id": 110134,
            "original_language": "en",
            "original_title": "Michael McIntyre's Comedy Roadshow",
            "overview": "This bonus disc from the Michael Mcintyre Stand-Up Collection DVD Box Set contains excerpts from the hilarious second series of Michael's Comedy Roadshow",
            "popularity": 1.043,
            "poster_path": "/q8fPt3MQr3zW6RXo5gbez8bz0Yv.jpg",
            "release_date": "2009-11-16",
            "title": "Michael McIntyre's Comedy Roadshow",
            "video": true,
            "vote_average": 6.9,
            "vote_count": 5
        }
    ],
    "total_pages": 45,
    "total_results": 881
}
```


# UML sequence diagram

![UML Sequence Diagram](/Sequence_diagram.svg)
