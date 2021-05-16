import csv

#with open('height-weight.csv',newline='') as f:
with open('hw.csv',newline='') as f: 
    reader = csv.reader(f)
    file_data = list(reader)
   
file_data.pop(0)
print(type(file_data))
