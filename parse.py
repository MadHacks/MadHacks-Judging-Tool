import csv
with open('/Users/apple/Desktop/submissions.csv', 'r') as f:
    reader = csv.reader(f)
    l = list(reader)

for row in l: 
     del row[2]
     del row[2]
     del row[2]
     del row[2]
     for x in range(1,11):
         del row[3]
with open('/Users/apple/Desktop/output.csv', 'wb') as csv_file:
    writer = csv.writer(csv_file, delimiter=',')
    writer.writerow(l[0]+['Table Number']+['Assigned Judges'])
    l.remove(l[0])
    a=1
    for line in l:
        writer.writerow(line+[a])
        a+=1
