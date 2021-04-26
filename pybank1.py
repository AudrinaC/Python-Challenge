import os
import csv

# Variables 

months = [] 
profit_loss = []

csvpath = os.path.join('..', 'PythonStuff', 'budget_data.csv')

with open(csvpath, 'r') as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=",") 

    csv_header = next(csvreader) 

    print(csv_header)
    print("-----")

    for row in csvreader:

        months.append(row[0])
        profit_loss.append(int(row[1]))

# Challenge Questions: 

# 1. Total number of months included in the dataset 

#Calculate the total months included in the data set
total_months = (len(months))

# 2. Net Total amount of "Profit/Losses" over the entire period

#Calculate the net amount of Profit/Losses over the period of time
net_amount = sum(profit_loss) 

# 3. Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes

#Calculate the average change per month
avg_change = net_amount / total_months 

# 4. Greatest increase in profits (date and amount) over the entire period

#Calculate the greatest increase in profits (date and amount)
max_profit = max(profit_loss)

#Using the index of the greatest increase to find the date
index_max = profit_loss.index(max_profit)
max_month = months[index_max] 

# 5. Greatest decrease in losses (date and amount) over the entire period  

#Calculate the greatest decrease in loss (date and amount)
min_profit = min(profit_loss) 

#Using the index of the greatest decrease to find the date
index_min = profit_loss.index(min_profit)
min_month = months[index_min]

# Print out analysis  

financial_analysis = (f"""Financial Analysis
-------------------------------
Total Months: {total_months} 
Total: ${net_amount:.2f} 
Average Change: {avg_change:.2f} 
Greatest Profit Increase: {max_month} {max_profit:.2f} 
Greatest Profit Decrease: {min_month} {min_profit:.2f}""")

print (financial_analysis) 

# adding text file

analysis = open('financial_analysis.txt', 'w')

analysis.write('Financial Analysis\n')
analysis.write('----------------------------------\n')
analysis.write(f'Total Months: {total_months}\n')
analysis.write(f'Total: ${net_amount:.2f}\n')
analysis.write(f'Average Change: {avg_change:.2f}\n')
analysis.write(f'Greatest Increase in Profits: {max_month} {max_profit:.2f}\n')
analysis.write(f'Greatest Decrease in Profits: {min_month} {min_profit:.2f}\n')
analysis.write(financial_analysis)



 












