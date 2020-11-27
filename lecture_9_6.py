import csv

with open("data.csv","w") as file:
    writer = csv.writer(file)
    writer.writerow(["transaction_id","product_id", "price"])
    writer.writerow([1500, 14, 10])
    writer.writerow([1501, 15, 11])

with open("data.csv","r") as file:
    reader = csv.reader(file)
    #print(list(reader))
    #or
    for row in reader:
        print(row)