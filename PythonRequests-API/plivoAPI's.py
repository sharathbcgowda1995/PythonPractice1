import requests

resp=requests.get("https://api.numbers.plivodev.com/v1/Account/MAYJLIZGQ5MWVKZWM4NZ/PhoneNumber/?country_iso=US",auth=('MAYJLIZGQ5MWVKZWM4NZ','MjFkZjQ3MzhiODFlZmY4MjIyODk2NTgxOGVmMDdm'))
print(resp.status_code)
print(resp.json())