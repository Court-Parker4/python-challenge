import os
import csv

# cwd = os.getcwd()  # Get the current working directory (cwd)
# files = os.listdir(cwd)  # Get all the files in that directory
# print("Files in %r: %s" % (cwd, files))

# with open('C:\\Resources\\budget_data.csv', 'r') as f:
#     reader = csv.reader(f)
#     for row in reader:
#         print(row)
#Path to collect data from the reources folder
# budgetCsvPath = os.path.join('Resources','budget_data.csv')
budgetCsvPath = os.path.join('budget_data.csv')
with open(budgetCsvPath) as csvfile:

    #need to specify the delimiter
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first
    csv_header = next(csvreader)
    print(f"CSV Header: [csv_header]")

    # read each row of data
    for row in csvreader:
        print(row)

#Define the function and have it accept the 'budget_data' as sole parameter
def print_financial(budget_data):
    #assigning values to variables
    date = str(budget_data[0])
    profit/losses = int(budget_data[1])
    