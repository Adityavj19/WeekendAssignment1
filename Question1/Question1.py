import csv

with open('FL_insurance_sample.csv', 'r') as data:
    reader = csv.reader(data)
    data_list = []
    for i in reader:
        data_list.append(i)

data.close()
with open('New_sample.csv','w') as data1:
    writer = csv.writer(data1)
    for h in data_list:
        writer.writerow(h[0:11:2])
data1.close()





