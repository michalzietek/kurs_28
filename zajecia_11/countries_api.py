import requests

# onet_request = requests.get("https://www.onet.pl/")
#
# print(onet_request.content)
#
# print(onet_request.status_code)
#
# print(onet_request)

country_api = requests.get("https://restcountries.com/v3.1/all")

#print(country_api.content)
print(type(country_api.content))
print(country_api.json())
