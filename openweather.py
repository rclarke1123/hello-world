# Python program to find current weather details of any city or zipcode
# using openweathermap api

print('''This program will display the current weather
details of any city or zipcode using openweathermap''')
    
  
# import required modules 
import requests, json 
  
# Enter your API key here 
api_key = "35213e9e5cc4350f31cb60fdc72729c6"
  
# base_url variable to store url 
base_url = "http://api.openweathermap.org/data/2.5/weather?"


  
# Give city name or zipcode
def chooseData ():
  data=''
  while data !='City name' and 'Zipcode':
      print("Enter city name or Zip code: ")
      data= input()

      return data  
  
# complete_url variable to store 
# complete url address 
complete_url = base_url + "appid=" + api_key + "&q=" + chooseData()
  
# get method of requests module 
# return response object 
response = requests.get(complete_url) 
  
# json method of response object  
# convert json format data into 
# python format data 
x = response.json()

 
  
# Now x contains list of nested dictionaries 
# Check the value of "cod" key is equal to 
# "404", means city is found otherwise, 
# city is not found 
if x["cod"] != "404": 
  
    # store the value of "main" 
    # key in variable y 
    y = x["main"] 
  
    # store the value corresponding 
    # to the "temp" key of y 
    current_temperature = y["temp"]
      
    # store the value corresponding 
    # to the "pressure" key of y 
    current_pressure = y["pressure"] 
  
    # store the value corresponding 
    # to the "humidity" key of y 
    current_humidiy = y["humidity"] 
  
    # store the value of "weather" 
    # key in variable z 
    z = x["weather"] 
  
    # store the value corresponding  
    # to the "description" key at  
    # the 0th index of z 
    weather_description = z[0]["description"] 
  
    # print following values 
    print(" Temperature (in Fahrenheit) = " +
                    str((current_temperature*1.8)-459.67) + 
          "\n atmospheric pressure (in hPa unit) = " +
                    str(current_pressure) +
          "\n humidity (in percentage) = " +
                    str(current_humidiy) +
          "\n description = " +
                    str(weather_description)) 
  
else: 
    print(" City Not Found ") 
