'''
Due the outstanding performance of the Customer Service Represetatives (CSRs) in the marketing department, management
has decided to reward them with a 10% increase in their salary. To evaluate the impact on the budget, you have been
asked to run a report on the employee file and display the results of BEFORE AND AFTER the salary increase.

You will create a dictionary that has the full employee name as the key and ONLY their new salary as the value.

Iternate through the dictionary to print out their name and thier new salary (as in image)
'''

import csv


# open the file
infile = open('employee_data.csv', 'r')
outfile = open('ProcessedEmployees.csv', 'a')

reader = csv.reader(infile)
next(reader)

# create an empty dictionary
updated_dict = {}

# use a loop to iterate through the csv file
for row in reader:
    department = row[3]
    fname = row[1]
    lname = row[2]
    full_name = fname + '' + lname
    salary = row[5]
    new_salary = salary
    # check if the employee fits the search criteria
    if department == 'Marketing':
        print(f"Manager Name:", fname, lname,
              "Current Salary:$", salary)

updated_dict['First Name'] = fname
updated_dict['Last Name'] = lname
updated_dict['Full Name'] = fname + ' ' + lname
updated_dict['Salary'] = salary
updated_dict['New Salary'] += salary * .1


print()
print('=========================================')
print()

# iternate through the dictionary and print out the key and value as per printout
updated_dict[full_name] = salary
print(updated_dict)
