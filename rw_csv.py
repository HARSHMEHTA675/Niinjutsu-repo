import csv

with open("data.csv","w+") as csvfile:
    writer=csv.writer(csvfile)
    writer.writerow(["Row 1","some Description","Another"])
    writer.writerow(["Title","Description","col 3"])
    writer.writerow(["Row 1","some Description","Another"])
    

with open("data.csv","r") as csvfile:
    reader=csv.reader(csvfile)
    for row in reader:
        print(row)
        
with open("data.csv","a") as csvfile:
    writer=csv.writer(csvfile)
    writer.writerow(["Data 3", "Data 4"])
    

with open("data.csv","r") as csvfile:
    reader=csv.DictReader(csvfile)
    for row in reader:
        print(row)
