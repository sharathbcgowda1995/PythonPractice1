import json
import requests

#first step
response = requests.get("https://reqres.in/api/users?page=2")

#Response can be printed in 3 ways
print("Response can printed using CONTENT : ", response.content)
print("Response can printed using TEXT : ", response.text)
print("Response can printed using JSON : ", response.json())

#status code
print("Status code is : ",response.status_code)

#Assertion
assert  response.status_code==200,"Assertion failed"
print("Assertion successfull ")

