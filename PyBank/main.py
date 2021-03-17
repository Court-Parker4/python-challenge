import os
import csv

budgetCsvPath = os.path.join('budget_data.csv')
with open(budgetCsvPath) as csvfile:

    #need to specify the delimiter
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first
    csv_header = next(csvreader)
    month = []
    revenue = []
    revenue_delta = []
    before = 0

    print(f"CSV Header: [csv_header]")

    #The Total number of months included in the dataset
    for row in csvreader:
        month.append(row[0])
        revenue.append(row[1])
        # print(len(month))

    #The net total amount pf "Profit/Losses" over the entire period
        revenue_start = int(row[1])- int(before)
        before = row[1]
        revenue_delta.append(revenue_start)
        # print(revenue_delta)

correct = zip(month, revenue)
correctBegin = list(correct)
revenue_delta.remove(revenue_delta[0])
correctBegin.remove(correctBegin[0])

months = len(month)
total = sum(map(int, revenue))
avg_delta = sum(revenue_delta) / len(revenue_delta)
positive = max(revenue_delta)
negative = min(revenue_delta)

date_decrease = 0
date_increase = 0

for row in correctBegin:
    if row[1] == positive:
        date_increase = row[0]
    if row[1] == negative:
        date_decrease = row[0]

#Print financial Analysis
print(f'Financial Analysis')
print(f'____________________________')
print(f'Total Months: {months}')
print(f'Total: ${total}')
print(f'Average Change: ${avg_delta:.2f}')
print(f'Greatest Increase In Profits: ({positive})')
print(f'Greatest Decreasae In Profits: ({negative})')

with open('pybank.txt', 'w') as text_file:
    print(f'Financial Analysis', file=text_file)
    print(f'____________________________', file=text_file)
    print(f'Total Months: {months}', file=text_file)
    print(f'Total: ${total}', file=text_file)
    print(f'Average Change: ${avg_delta:.2f}', file=text_file)
    print(f'Greatest Increase In Profits:  ({positive})', file=text_file)
    print(f'Greatest Decreasae In Profits: ({negative})', file=text_file)
