import requests

# GET
url_endpoint = 'http://127.0.0.1:5000/uppercase'

resp = requests.get(url_endpoint, params={'text': 'This is some text'})

response_json = resp.json()
uppercase_text = response_json["text"]
print(uppercase_text)
