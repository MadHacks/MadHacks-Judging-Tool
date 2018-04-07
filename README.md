# MadHacks-Judging-Tool

# MadHacks Judging Tool for Devpost Submission CSV files

Parses the submission CSV files from devpost.com for quick assignment of judges during your hackathon.

Latest build uses Python 3.6.5 (64bit).

## Installation

Clone or download the repository.

## Downloading the Submission CSV on DevPost

1. On devpost.com, login and click on your user profile
2. Click on Manage Hackathons
3. Click on the Hackathon you want to download the CSV file from
4. Click on the Matrics tab
5. Under the "Export submission and registrant data" section:
    * Select "Submission data" under Type of Report
    * Select "Do not include" under Personally identifiable information
    * Select "Sort the export by opt-in prize" under Opt-in prize
6. Click the "Generate .csv report" button
7. Click on "Download report"

## Usage

1. Follow the "Downloading the Submission CSV on Devpost" instructions above, and put the CSV in the project folder
2. Rename the file from step 1 into "submissions.csv"
3. Open the project folder in the terminal of your choice
4. Run the command: python parse.py #OfJudges
    * Example. If you want 3 judges, run: python parse.py 3
    * You may need to delete existing output CSV files, before running this script
5. The output CSV files will assign projects to judges, so that each submission will be viewed by at least 2 judges (This number can be reconfigured in the Python script).

Note: Specific Sponsor Prize Judges functionality will need to be coded for your hackathon. This project is a good template, if you desire this functionality.

## Contributing

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D