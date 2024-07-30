import csv

csv_filename='cereal_grains.csv'
# quoting in csv file 

with open(csv_filename,encoding='utf-8',newline='')as csv_file:
    reader=csv.reader(csv_file , quoting=csv.QUOTE_NONNUMERIC)#Quote_nonnumeric: is used to quote all numeric value 
    for row in reader:
        print(row)
        