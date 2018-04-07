import csv
from sys import argv

script, JudgesNumber = argv

with open('submissions.csv', 'r', encoding="utf8") as f:
    reader = csv.reader(f)
    submissionsRowList = list(reader)

'''
Removes unneeded columns for the submissions.csv file. Keeps the following columns (in order):
Submission Title
Submission URL
Desired Prizes
'''
for row in submissionsRowList:
    del row[2]  # Delete Plain Description
    del row[2]  # Delete Video
    del row[2]  # Delete Website
    del row[2]  # Delete File Url
    '''
     Deletes the following columns:
     Built With
     Mlh points
     Mlh Hardware Lab
     Mlh Submitter Screen Name
     College/Universities Of Team Members
     Additional Team Member Count
     Team Members (Deletes up to 3 Members. May need to change depending on max # of members per team) 
     '''
    for x in range(1, 11):
        del row[3]

with open('Parsed_File_For_Teams.csv', 'w', newline='') as team_file, \
        open('Parsed_File_For_Judges.csv', 'w', newline='') as judges_file:
    teamWriter = csv.writer(team_file, delimiter=',')
    judgeWriter = csv.writer(judges_file, delimiter=',')

    # Print First Row for 'Parsed_File_For_Judges.csv'
    judgeList = []
    for judgeNumber in range(0, int(JudgesNumber)):
        judgeList.append('Judge ' + str(judgeNumber+1))
    judgeWriter.writerow(['Submission'] + ['Table Number'] + judgeList)

    # Print first row for 'Parsed_File_For_Teams.csv'
    teamWriter.writerow(submissionsRowList[0] + ['Table Number'])
    
    # Remove first row for parsing projects
    submissionsRowList.remove(submissionsRowList[0])

    # Print the rest of the rows for 'Parsed_File_For_Judges.csv' and 'Parsed_File_For_Teams.csv'
    tableNumber = 1

    for line in submissionsRowList:
        # Used to split judges evenly among all projects
        assignedJudgeNumber = int(((tableNumber-1)/int((len(submissionsRowList)/int(JudgesNumber)))+1))

        # Writes Row for 'Parsed_File_For_Judges.csv'
        markedJudges = [""] * int(JudgesNumber)
        markedJudges[int(assignedJudgeNumber)-1] = 'x'
        judgeWriter.writerow([str(line[0])] + [tableNumber] + markedJudges)

        # Writes Row for 'Parsed_File_For_Teams.csv'
        teamWriter.writerow(line + [tableNumber])

        tableNumber += 1