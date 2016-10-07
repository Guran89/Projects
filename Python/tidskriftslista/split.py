#utf-8

#Import data for the names of the departments
department_data = open("departments.txt", "r").read().split("\n")

#Import data
data1_import = open("data1.txt", "r").read().split("\n")

query1 = []

for line in data1_import:
    splitted = line.split("|")
    query1.append(splitted)

#Create empty array where to store the department names
departments = []

#Split the departments and save them in the depts array
for line in department_data:
    splitted = line.split(";")
    departments.append(splitted)

#Create empty array to store the filenames
dept_names = []

#Get the name of the departments and create filenames to store in the dept_name array
for dept in departments:
    temp_name = str(dept[0]) + "_" + str(dept[1]) + ".txt"
    dept_names.append(temp_name)

#Create new empty documents with the department names
for name in dept_names:
    open(name, "w")
