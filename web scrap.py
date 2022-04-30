import requests
r = requests.get('www.mycaptian.com')
print(r.url)
print(r.status_code)
