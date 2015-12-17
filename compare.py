import csv
speeding_cars = []
valid_number_plates = []
print ("Here is the list of speeding cars")
for i,x in zip (speeding_cars,valid_number_plates):
    print(i,x)
with open ("cars.csv","w")as f:
    f_csv = csv.writer(f)
    writer = csv.writer(f,delimiter = ",")
    writer.writerows(zip(speeding_cars,valid_number_plates))


f1 = ("data.csv", "r")
f2 = ("cars.csv","r")
f3 = ("results.csv","w")
c1 = csv.reader(f1)
c2 = csv.reader(f2)
c3 = csv.writer(f3)

if f1[3] == f2[2]:
    writer = csv.writer(f,delimiter = ",")
    writer.writerows(zip(f1 , f2))
