import os, time

if not os.path.exists("docs"):
    os.makedirs("docs")

print("\n*****************************************************")
print("Make sure the department's ID is in the first column,\nand that all the IDs are in the ids.txt file.")
print("*****************************************************\n")

#Get the names of the files to include
overview = input("Name of the file with overviews (without extension):\n> ")
per_year = input("Name of the file with overview per year (without extension):\n> ")
per_category = input("Name of the file with overview per category (without extension):\n> ")
#publist = input("Name of the file with publications (without extension):\n> ")

#Get the delimiter used in the files
delimiter = input("What's the delimiter used in the files?\n> ")

#Load and split the files
data_overview = open(overview + ".txt", "r").read().replace(".", ",").split("\n")
overview_depts = []
for row in data_overview:
    row_split = row.split(delimiter)
    overview_depts.append(row_split)


data_per_year = open(per_year + ".txt", "r").read().replace(".", ",").split("\n")
per_year_depts = []
for row in data_per_year:
    row_split = row.split(delimiter)
    per_year_depts.append(row_split)

data_per_category = open(per_category + ".txt", "r").read().replace(".", ",").split("\n")
per_category_depts = []
for row in data_per_category:
    row_split = row.split(delimiter)
    per_category_depts.append(row_split)
"""
data_publist = open(publist + ".txt", "r").read().replace(".", ",").split("\n")
publist_depts = []
for row in data_publist:
    row_split = row.split(delimiter)
    publist_depts.append(row_split)
"""
#Load IDs, split them, and store them in a list
ids_open = open("ids.txt", "r").read().split("\n")
ids = [] #List to store the IDs
#Split the IDs and store in the list
for i in ids_open:
    temp = i.split(";")
    ids.append(temp)

for num in ids:
    newfile = open("docs/" + str(num[0]) + "_" + num[1] + ".txt", "w")
#Overview
    newfile.write("Number of journals|Number of publications|jf|jf x number of publications\n")
    for row in overview_depts:
        if row[0] == num[0]:
            for post in row[2:]:
                newfile.write(str(post + "|"))
            newfile.write("\n")
#Per year
    newfile.write("\n\nPublication year||Number of journals|Number of publications|jf|jf x number of publications\n")
    for row in per_year_depts:
        if row[0] == num[0]:
            for post in row[1:]:
                newfile.write(str(post + "|"))
            newfile.write("\n")
#Per category
    newfile.write("\n\nCategories|Numbers of journals in category|Number of publications in category|jf|jf x number of publications\n")
    for row in per_category_depts:
        if row[0] == num[0]:
            for post in row[2:]:
                newfile.write(str(post + "|"))
            newfile.write("\n")
"""
#Publication list
    newfile.write("\n\nPublication list\n")
    for row in publist_depts:
        if row[0] == num[0]:
            for post in row[1:]:
                newfile.write(str(post + "|"))
            newfile.write("\n")
    newfile.close()
"""
