import requests

httpbin = 'https://httpbin.org'

# get basic
# ---------

# response = requests.get(f'{httpbin}/get')
# print(response.status_code)

# print(response.text)
# print(response.json())  # response.text as json if is json

# request params
# --------------

# * bare-bones

# response = requests.get(f'{httpbin}/get?name=Joerg&age=60')
# print(response.json())

# * more pythonic

# response = requests.get(f'{httpbin}/get', 
#                         params={
#                             'name': 'Joerg',
#                             'age': 60,
#                         })
# print(response.url)
# print(response.json())

# * -> url-encoding

response = requests.get(f'{httpbin}/get', 
                        params={
                            'name': 'Jörg',
                            'age': 60,
                        })
print(response.url)
print(response.json())

# POST
# ----

response = requests.get(f'{httpbin}/get', 
                        params={
                            'name': 'Jörg',
                            'age': 60,
                        })
print(response.url)
print(response.json())
