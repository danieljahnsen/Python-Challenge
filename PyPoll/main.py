import os
import csv

path = os.path.join("Resources", "election_data.csv")

#Creating my counting variables
total_votes = 0
khan_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0

#Reading the csv
with open(path) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    
    #Skips the first row
    csv_header = next(csv_reader)

    #Loops through the remaining rows
    for row in csv_reader:

        #Adds one to the total vote count
        total_votes = total_votes + 1

        #Conditional for counting a vote for each candidate
        if row[2] == "Khan":
            khan_votes = khan_votes + 1
        elif row[2] == "Correy":
            correy_votes = correy_votes + 1
        elif row[2] =="Li":
            li_votes = li_votes + 1
        elif row[2] == "O'Tooley":
            otooley_votes = otooley_votes + 1

#Calculate the vote percentages after elction
kvote = round((khan_votes/total_votes)*100, 3)
cvote = round((correy_votes/total_votes)*100, 3)
lvote = round((li_votes/total_votes)*100, 3)
o_vote = round((otooley_votes/total_votes)*100, 3)

#Gets the winner of the election
candidates = ["Khan", "Correy", "Li", "O'Tooley"]
votes = [kvote, cvote, lvote, o_vote]

#Gets the max of the votes
winner = max(votes)

#gets the vote index
i = votes.index(winner)

#Stores the winning candidate
winning_candidate = candidates[i]

#Printing the results
print('Election Results')
print('-------------------------------')
print(f'Total Votes: {total_votes}')
print('-------------------------------')
print(f'Khan: {kvote}% ({khan_votes})')
print(f'Correy: {cvote}% ({correy_votes})')
print(f'Li: {lvote}% ({li_votes})')
print(f"O'Tooley: {o_vote}% ({otooley_votes})")
print('-------------------------------')
print(f'Winner: {winning_candidate}')
print('-------------------------------')

#Writing the output to a csv
output_path = os.path.join("Output", "results.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the first row total votes
    csvwriter.writerow(['Total Votes', total_votes])

    # Write a row for each candidate
    csvwriter.writerow(['Khan', kvote, khan_votes])
    csvwriter.writerow(['Correy', cvote, correy_votes])
    csvwriter.writerow(['Li', lvote, li_votes])
    csvwriter.writerow(["O'Tooley", o_vote, otooley_votes])

    #Write a winning row
    csvwriter.writerow(['Winner', winning_candidate])
