import os
import csv

path = os.path.join("Resources", "budget_data.csv")

#Creating my variables
months = 0
total_change = 0
PL_list = []

#Variables for the profit increases and decreases
max_change = 0
min_change = 0
max_month = ''
min_month = ''

#Variable for the list of changes
change_list = []

#Reading the csv
with open(path) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    
    #Skips the first row
    csv_header = next(csv_reader)

    #Looping through all of the remaining rows
    for row in csv_reader:

        #Appends the current value to the change list
        PL_list.append(int(row[1]))

        #Calculates the current change starting with the second month
        if months > 0:

            #Calculates the current change
            current_change = PL_list[months] - PL_list[months-1]
            change_list.append(current_change)

            #Assigns the change to the greatest
            if current_change > max_change:
                max_change = current_change
                max_month = row[0]

            #Assigns the change to the min
            elif current_change < min_change:
                min_change = current_change
                min_month = row[0]

        #Adding one to the month total for row
        months = months + 1

        #Adding to the total
        total_change = total_change + int(row[1])




#calculate the average of the changes list
average = round(sum(change_list) / len(change_list), 2)



#Printing the results
print("Financial Analysis")
print("------------------")
print(f'Total Months: {months}')
print(f'Total: ${total_change}')
print(f'Average Change: ${average}')
print(f'Greatest Increase in Profits: {max_month} ({max_change})')
print(f'Greatest Decrease in Profits: {min_month} ({min_change})')


#Writing the output to a csv
#Writing the output to a csv
output_path = os.path.join("Output", "summary.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the first row tital
    csvwriter.writerow(['Financial Analysis'])

    # Write the rest of the data to rows
    csvwriter.writerow(['Total Months', months])
    csvwriter.writerow(['Total', total_change])
    csvwriter.writerow(['Average Change', average])
    csvwriter.writerow(['Greatest Increase in Profits', max_month, max_change])
    csvwriter.writerow(['Greatest Decrease in Profits', min_month, min_change])

