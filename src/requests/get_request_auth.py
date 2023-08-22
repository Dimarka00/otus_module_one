import requests

r = requests.get('https:/httpbin.org//basic-auth/user/password', auth=('user', 'password'))
print(r.text)
