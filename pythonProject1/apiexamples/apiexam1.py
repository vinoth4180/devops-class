#https://developer.nrel.gov
#https://developer.nrel.gov/api/alt-fuel-stations/v1.json?fuel_type=E85,ELEC&state=CA&limit=2&api_key=gVl6k04aFcnQ0PU5oiTf2a6ZUKYNANwc8Ogr5bcb
import requests
# res=requests.get("https://developer.nrel.gov/api/alt-fuel-stations/v1.json?fuel_type=E85,ELEC&state=CA&limit=2&api_key=gVl6k04aFcnQ0PU5oiTf2a6ZUKYNANwc8Ogr5bcb")
# print(res.status_code)
# print(res.text)
# print(res.json())
# print(list(res.json()))



api_address='http://api.openweathermap.org/data/2.5/weather?appid=3b38f7256941d04dc249f965f535ca29&q='
city = input('City Name :')
url = api_address + city
print(url)
json_data = requests.get(url).json()
print(json_data)
format_add = json_data['weather'][0]['main']
format_add2 = json_data['coord']['lon']
format_add3 = json_data['coord']['lat']
format_add1 = json_data['weather'][0]['description']
print(format_add,"and ",format_add1)
print(format_add,"and ",format_add2)
print(format_add,"and ",format_add3)
