import json

json_data_source = 'temperature_anomaly.json'

with open(json_data_source,encoding='utf-8') as data:
    anomalies= json.load(data) # .load() is converting/parses the json file to the python dict named 'anomalies'
    
print(anomalies['description']) # print the value of the description part 
#This line prints the 'description' section of the JSON data, which includes metadata about the temperature anomalies (title, units, base period, and missing value indicator).

# this loop will iterate over the 'data' section of the json which contains the year-value pair 
for year, value in anomalies['data'].items():
    year,value=int(year),float(value) # int and float converts the year and value terms from string to respective terms 
    print(f"{year}...{value:6.2f}")
'''The print(f"{year}...{value:6.2f}") line prints each year and its 
corresponding anomaly value, formatted to two decimal places with a width of 6 characters.'''
print('*'*80)

print(anomalies['citation'])
