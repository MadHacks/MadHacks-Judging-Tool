import csv
from sys import argv

script,JudgesNumber = argv

with open('submissions.csv', 'r', encoding="utf8") as f:
    reader = csv.reader(f)
    submissionsRowList = list(reader)

for row in submissionsRowList: 
     del row[2] # Delete Plain Description
     del row[2] # Delete Video
     del row[2] # Delete Website
     del row[2] # Delete File Url
     for x in range(1,11):
         del row[3]
         
with open('output.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file, delimiter=',')
    writer.writerow(submissionsRowList[0]+['Table Number']+['Assigned Judges'])
    submissionsRowList.remove(submissionsRowList[0]) # Remove first row for parsing, projects
    tableNumber = 1
    for line in submissionsRowList:
        assignedJudgeNumber = int(((tableNumber-1)/int((len(submissionsRowList)/int(JudgesNumber)))+1))
        writer.writerow(line+[tableNumber]+[assignedJudgeNumber])
        tableNumber += 1