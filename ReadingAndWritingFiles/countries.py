input_filename='country_info.txt'

countries={}
with open(input_filename) as country_file:
    country_file.readline()
    for row in country_file:
        data=row.strip('\n').split('|')
# we did .strip('\n') because if we do just .split('|') as .split returns indivisudal elements in a list form and \n at last to tell new line 
# so by using .strip('\n') we can remove that \n 
        if len(data)==7:
            country, capital, code, code3 , dialing , timezone, currency = data
            #print(country, capital, code, code3 , dialing , timezone, currency , sep='\n\t')
        
            country_dict = {
                'name' : country,
                'capital' : capital,
                'country_code' : code,
                'cc3' : code3 , 
                'dialing_code' : dialing,
                'timezone' : timezone , 
                'currency' : currency
            }
            #print(country_dict) 
            countries[country.casefold()]=country_dict
        else:
            print(f"Skipping row due to incorrect number of fields: {row}")
            
#print(countries)
while(True):
    chosen_country= input("Please enter the name of a country: ").casefold()
    if chosen_country in countries:
        country_data=countries[chosen_country]
        print(f"The capital of {chosen_country} is {country_data['capital']}")
    elif chosen_country=='quit':
        break 
