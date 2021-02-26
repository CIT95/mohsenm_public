# learnTogether Week 7

# The one-month costs list in my family.
# - Fixed costs: Rent, Insurance car, Cell phone plan, Internet/WiFi.
# - Variable costs: PG_E, Utilities(water, trash, sewer), Groceries, Gas_and_Services.

# List of Variable costs
variable_costs = ['PG_E', 'Utilities', 'Groceries', 'Gas_and_Services']

# Create and initialized dicitonary (Just Variable costs)
costs_one_month = {
    'PG_E': 115.07,
    'Utilities': 45.24,
    'Groceries': 500,
    'Gas_and_Services': 120,
}

# Displaying dd
print('\nDisplaying dd:')
print(' - costs_one_month = ', costs_one_month)

# Adding a key to the dd
print('\nAdding a key to the dd:')
costs_one_month.setdefault('Month', 1)
print(' - costs_one_month = ', costs_one_month)

# Sorting the data in ascending order by the key.
print('\nSorting the data in ascending order by the key:')
sorted1_costs_one_month = sorted(costs_one_month.items())
print(' - sorted1_costs_one_month = ', sorted1_costs_one_month)


# Sorting the data in descending order by the value.
print('\nSorting the data in descending order by the value.')
sorted2_costs_one_month = sorted(costs_one_month.items(), key=lambda item: item[1])
print(' - sorted2_costs_one_month = ', sorted2_costs_one_month)

# Check whether a given key already exists in the dd
print('\nCheck whether a given key already exists in the dd')
print(" - costs_one_month.get('Groceries', 0) = ", costs_one_month.get('Groceries', 0))
print(" - costs_one_month.get('Tranportation', 0) = ", costs_one_month.get('Tranportation', 0))

# Iterate over dd using for loops.
print('\nIterate over dd using for loops.')
for k, v in sorted1_costs_one_month:
    print(' - ', k, ':', v)

# List of dd for one year (2020).
list_costs = []
list_costs.append({'Month': 1, 'PG_E': 115.07, 'Utilities': 45.24, 'Groceries': 500, 'Gas_and_Services': 120})
list_costs.append({'Month': 2, 'PG_E': 110.13, 'Utilities': 39.78, 'Groceries': 455, 'Gas_and_Services': 105})
list_costs.append({'Month': 3, 'PG_E': 90.00, 'Utilities': 43.16, 'Groceries': 525, 'Gas_and_Services': 115})
list_costs.append({'Month': 4, 'PG_E': 22.67, 'Utilities': 46.50, 'Groceries': 490, 'Gas_and_Services': 111})
list_costs.append({'Month': 5, 'PG_E': 64.82, 'Utilities': 47.63, 'Groceries': 460, 'Gas_and_Services': 117})
list_costs.append({'Month': 6, 'PG_E': 91.32, 'Utilities': 50.77, 'Groceries': 435, 'Gas_and_Services': 99})
list_costs.append({'Month': 7, 'PG_E': 100.47, 'Utilities': 47.23, 'Groceries': 467, 'Gas_and_Services': 119})
list_costs.append({'Month': 8, 'PG_E': 38.42, 'Utilities': 42.45, 'Groceries': 496, 'Gas_and_Services': 103})
list_costs.append({'Month': 9, 'PG_E': 143.22, 'Utilities': 54.19, 'Groceries': 530, 'Gas_and_Services': 125})
list_costs.append({'Month': 10, 'PG_E': 110.64, 'Utilities': 49.05, 'Groceries': 449, 'Gas_and_Services': 113})
list_costs.append({'Month': 11, 'PG_E': 87.42, 'Utilities': 44.85, 'Groceries': 472, 'Gas_and_Services': 107})
list_costs.append({'Month': 12, 'PG_E': 130.72, 'Utilities': 51.32, 'Groceries': 506, 'Gas_and_Services': 140})

print('\nList of dd for one year (2020).')
for i in range(len(list_costs)):
    print(' - ', list_costs[i])

# Filter the dd based on values.
print("\nFilter the dd based on values. (value['PG_E'] <= 100 and value['Groceries'] <= 460)")
filter_by_Month = [value for value in list_costs if value['PG_E'] <= 100 and value['Groceries'] <= 460]
for i in range(len(filter_by_Month)):
    print(' - ', filter_by_Month[i])

# Iterate over the list of dd and output summary data (total, average, min, max etc)
# Minimum in dd
print('\nMinimum in dd')
for i in range(len(variable_costs)):
    print(' - min_' + variable_costs[i], ' = ', min(list_costs, key=lambda x:x[variable_costs[i]]))

# Maximum in dd
print('\nMaximum in dd')
for i in range(len(variable_costs)):
    print(' - max_' + variable_costs[i], ' = ', max(list_costs, key=lambda x:x[variable_costs[i]]))

# Average in dd
print('\nAvarage in dd')
total = [0, 0, 0, 0]
for i in range(len(variable_costs)):
    total[i] = round(sum(x.get(variable_costs[i]) for x in list_costs), 2)

for i in range(len(variable_costs)):
    print(' - The avarage costs of', variable_costs[i], 'in one month = ', round(total[i]/12, 2))

# Total in dd
print('\nTotal in dd')
for i in range(len(variable_costs)):
    print(' - The total costs of', variable_costs[i], 'in one year = ', total[i])

# Total all variable costs in one year.
print('\nThe total costs of', variable_costs[0], ',', variable_costs[1], ',', variable_costs[2], 
        ',', variable_costs[3], 'in one year = ', total[0] + total[1] + total[2] + total[3])
