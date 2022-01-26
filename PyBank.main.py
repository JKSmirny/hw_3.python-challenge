import csv
# first, create variables for all the things we need
months  = []   # list of months
profits = []   # list of profits/losses
changes = []   # list of changes for each month
total_amount = 0

with open("Resources/budget_data.csv", "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    line_number = 0 # to keep track of line numbers. We start the count at 0
    for line in csvreader:
        months.append(line[0])
        current_profit = float(line[1])
        profits.append(current_profit)
        total_amount += current_profit
        # now, compute change
        if (line_number == 0):
            # this is first month, no previous data
            changes.append(current_profit)
        else:
            # compute change from previous month
            previous_profit = profits[line_number - 1]
            changes.append(current_profit-previous_profit)
        #increase line number
        line_number +=1
    csvfile.close()
# now we have all the data
number_months = len(months)
# average change
average_change = sum(changes)/number_months
max_increase = max(changes)
# number of the month in which max  happened
max_increase_index = changes.index(max_increase)
# same for minimal change (i.e. maximal decrease)
max_decrease = min(changes)
# number of the month in which max  happened
max_decrease_index = changes.index(max_decrease)
print(changes)
#now print it all
print("Financial analysis")
print("Total months: ", number_months)
print("Total: $", total_amount)
print("Average change: $", average_change)
print("Maximal increase: {} (${})".format(months[max_increase_index], max_increase))
print("Maximal decrease: {} (${})".format(months[max_decrease_index], max_decrease))
# now save it to file

with open("analysis/results.txt", "w") as results:
    results.write("Financial analysis\n")
    results.write("Total months: {}\n".format(number_months))
    results.write("Total: $ {}\n".format(total_amount))
    results.write("Average change: $ {}\n".format(average_change))
    results.write("Maximal increase: {} (${})\n".format(months[max_increase_index], max_increase))
    results.write("Maximal decrease: {} (${})\n".format(months[max_decrease_index], max_decrease))
    results.close()

