import requests

r = requests.get('https://raw.github.com/kennethreitz/requests/master/README.rst')
print r
print r.headers['Content-Type']
