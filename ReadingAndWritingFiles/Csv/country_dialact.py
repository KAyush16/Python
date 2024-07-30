import csv

input_filename = 'country_info.txt'

with open(input_filename, encoding='utf-8', newline='') as countries_data:
    sample= countries_data.read()#This line reads the entire content of the file into the variable "sample".
    country_dialect=csv.Sniffer().sniff(sample)#it is detecting the file dialact 
    '''The "Sniffer" class in the csv module analyzes the sample data to detect the dialect.
    The "sniff" method returns a Dialect object that describes the detected dialect of the CSV file (e.g., delimiter, quote characters).'''
    country_reader = csv.reader(countries_data,dialect=country_dialect)
    for row in country_reader:
        print(row)
        
        
print('*'*80)
attributes=['delimiter',
            'doublequote',
            'escapechar',
            'lineterminator',
            'quotechar',
            'quoting',
            'skipinitialspace'
        ]
for attribute in attributes:
    print(f"{attribute}: {getattr(country_dialect,attribute)}")

 