import csv

with open("data.csv","w+") as csvfile:
    writer=csv.writer(csvfile)
    writer.writerow(["Row 1","some Description","Another"])
    writer.writerow(["Title","Description","col 3"])
    writer.writerow(["Row 1","some Description","Another"])
    

with open("data.csv","a") as csvfile:
    writer=csv.writer(csvfile)
    writer.writerow(["Append row","some Description","Another"])
    
