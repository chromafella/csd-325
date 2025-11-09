import requests

response = requests.get('http://www.google.com')

print("REQUESTING WWW.GOOGLE.COM: ")
print(response.status_code)

#200 if everything's fine
#404 not found

print('')
print('')
print('')
print('')

print('REQUESTING API.OPEN-NOTIFY.ORG/ASTROS: ')
response = requests.get("http://api.open-notify.org/astros")
print("CODE: ")
print(response.status_code)

print("JSON: ")
print(response.json())

