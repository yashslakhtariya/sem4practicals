import requests

url = requests.get('https://xkcd.com/353')
url2 = requests.get('https://images.bbtmedia.com/sites/default/files/styles/extra_large__600x600_/public/art_originals/0025_TLC%2020.jpg')

# print(url)

# response = requests.get('https://jsonplaceholder.typicode.com/posts')

# print(response.status_code) # prints the HTTP status code of the response
# print(response.json()) # prints the JSON response content

with open('demo.jpg', 'wb') as f:
     f.write(url2.content)