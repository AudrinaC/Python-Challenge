import os
import csv

csvpath = os.path.join('..', 'PythonStuff', 'election_data.csv')

# Challenge Questions

# 1. Total number of votes cast 
# 2. Complete list of candidates who received votes
# 3. Percentage of votes each candidate won 
# 4. Total number of votes each candidate won 
# 5. Popular vote winner

# Variables 

totalvotes = 0
candidates = []
votesPerCandidates = []

with open(csvpath, 'r') as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=",") 

    csv_header = next(csvreader) 

    print(csv_header)
    print("-----")

    for row in csvreader:

        totalvotes += 1
        if totalvotes == 1:
            candidates.append(row[2])
            votesPerCandidates.append(1)
        else:
            try:
                icandidate = candidates.index(row[2])
                votesPerCandidates[icandidate] += 1
            except:
                candidates.append(row[2])
                votesPerCandidates.append(1)
results = []
results.append("Election Results\n-------------------------")
results.append(f"Total Votes: {totalvotes}\n-------------------------")
winner = candidates[0]
maxvotes = votesPerCandidates[0]
for i in range(len(candidates)):
    if votesPerCandidates[i] > maxvotes:
        winner = candidates[i]
        maxvotes = votesPerCandidates[i]
    percent = 100 * votesPerCandidates[i] / totalvotes
    results.append(f"{candidates[i]}: {round(percent,3)} % ({votesPerCandidates[i]})")
results.append(f"-------------------------\nWinner: {winner}\n-------------------------")
filename = 'Results.txt'
with open(filename, 'w') as file:
    for result in results:
        print(result)
        file.write(result + '\n')







