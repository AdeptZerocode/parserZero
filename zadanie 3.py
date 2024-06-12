import requests

url = "https://jsonplaceholder.typicode.com/posts"

data = {
    "title" : "foo",
    "body" : "bar",
    "userId" : 1

}

responce = requests.post(url, data=data)

print(responce.status_code)

print(f"ответ - {responce.json()}")