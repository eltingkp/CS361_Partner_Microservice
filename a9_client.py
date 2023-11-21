import socket
import json

client = socket.socket()

client.connect(('localhost', 3000))

movie_object = {"data": "https://api.themoviedb.org/3/search/movie?query=comedy&include_adult=false&language=en-US&page=1&api_key=ae3ce3a5748e76935541a0dac7366a35"}

json_string = json.dumps(movie_object)

client.send(bytes(json_string, 'utf-8'))

message = client.recv(1024).decode()

print(message)
