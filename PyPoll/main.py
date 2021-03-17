import os
import csv

electionCsvPath = os.path.join('election_data.csv')
with open(electionCsvPath) as csvfile:

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

    #variables
    vote = []
    county = []
    candidate = []
    khan = []
    correy = []
    li = []
    otooley = []

    for row in csvreader:
        vote.append(int(row[0]))
        county.append(row[1])
        candidate.append(row[2])

    total_count = (len(vote))
    print(total_count)

    for candidates in candidate:
        if candidates == "Khan":
            khan.append(candidate)
            kVotes = len(khan)
        elif candidates == "Correy":
            correy.append(candidate)
            cVotes = len(correy)
        elif candidates == "Li":
            li.append(candidate)
            lVotes = len(li)
        else:
            otooley.append(candidate)
            oVotes = len(otooley)
    print(kVotes)
    print(cVotes)
    print(lVotes)
    print(oVotes)

    kPercent = round(((kVotes / total_count) * 100),2)
    cPercent = round(((cVotes / total_count) * 100),2)
    lPercent = round(((lVotes / total_count) * 100),2)
    oPercent = round(((oVotes / total_count) * 100),2)
    print(kPercent)
    print(cPercent)
    print(lPercent)
    print(oPercent)

    if kPercent > max(cPercent, lPercent, oPercent):
        winner = "Khan"
    elif cPercent > max(kPercent, lPercent, oPercent):
        winner = "Correy"
    elif lPercent > max(cPercent, kPercent, oPercent):
        winner = "Li"
    else:
        winner = "O'Tooley"



#Print Election Results
print(f'Election Results')
print(f'____________________________')
print(f'Total Votes: {total_count}')
print(f'____________________________')
print(f'Khan: {kPercent:.2f}% ({kVotes})')
print(f'Correy: {cPercent:.2f}% ({cVotes})')
print(f'Li:  {lPercent:.2f}% ({cVotes})')
print(f'OTooley: {oPercent:.2f}% ({oVotes})')
print(f'____________________________')
print(f'Winner: {winner}')

with open('pypoll.txt', 'w') as text_file:
    print(f'Election Results', file=text_file)
    print(f'____________________________', file=text_file)
    print(f'Total Votes: {total_count}', file=text_file)
    print(f'____________________________', file=text_file)
    print(f'Khan: {kPercent:.2f}% ({kVotes})', file=text_file)
    print(f'Correy: {cPercent:.2f}% ({cVotes})', file=text_file)
    print(f'Li:  {lPercent:.2f}% ({cVotes})', file=text_file)
    print(f'OTooley: {oPercent:.2f}% ({oVotes})', file=text_file)
    print(f'____________________________', file=text_file)
    print(f'Winner: {winner}', file=text_file)
