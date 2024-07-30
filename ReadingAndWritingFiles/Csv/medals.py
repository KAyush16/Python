import csv

with open("OlympicMedals_2020.csv",encoding='utf-8',newline='')as csv_file:
    headers=csv_file.readline().strip("\n").split(",")
    print(f"column headers: {headers}")
    reader= csv.reader(csv_file,  quoting=csv.QUOTE_NONNUMERIC )#After reading the headers, a csv.reader object is created to read the rest of the lines (data rows) in the file
    for row in reader:
        print(row) 
        