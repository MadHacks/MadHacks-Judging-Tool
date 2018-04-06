import csv
from sys import argv

script,JudgesNumber = argv
with open('submissions.csv', 'r', encoding="utf8") as f:
    reader = csv.reader(f)
    l = list(reader)

for row in l: 
     del row[2] # Delete Plain Description
     del row[2] # Delete Video
     del row[2] # Delete Website
     del row[2] # Delete File Url
     for x in range(1,11):
         del row[3]
         
with open('output.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file, delimiter=',')
    writer.writerow(l[0]+['Table Number']+['Assigned Judges'])
    l.remove(l[0])
    print(len(l))
    a=1
    for line in l:
        writer.writerow(line+[a]+[int(((a-1)/int((len(l)/int(JudgesNumber)))+1))])
        a+=1