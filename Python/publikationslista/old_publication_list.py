#encoding: utf-8
import os, time, sys

#Check the Python version and quit if version is lower than 3.
py_version = sys.version_info.major
if py_version < 3:
    print("You need a newer version of Python. You are running version " + str(py_version) + ".")
    print("Please install version 3.x and try again.")
    quit()

if not os.path.exists("docs"):
    os.makedirs("docs")

#Import department names
ids = open("dept_names.txt", "r").read().split("\n")

#Create empty list for splitted departments
ids_splitted = []

#Split departments and IDs and save in the list
for i in ids:
    splitted = i.split(";")
    ids_splitted.append(splitted)

print("\n*****************************************************")
print("INSTRUCTIONS")
print("The documents should be in .txt format, and without header.")
print("There should be XX number of .txt files, and they should all be found in\nthe same directory as this code (" + os.getcwd() + ").")
print("\nThe files you will need: ")
print("- Overview\n- Overview per year\n- Overview per journal category")

print("\nEDIT DEPARTMENT NAMES")
print("If you want to edit the department names, open the file 'dept_names.txt'.")
print("Make sure that the is formated like this:\n[deptID];[dept name]\n[deptID];[dept name]")

print("\nYou can exit the program anytime by pressing 'ctrl+c'.")
print("*****************************************************\n")
try:
    time.sleep(0.5)
    #Get the delimiter used in the files
    delimiter = input("What's the delimiter used in the files?\n> ")

    time.sleep(0.2)
    print("\nSTEP 1: Overview")
    time.sleep(0.2)
    #Get the names of the files to include
    while True:
            overview = input("\nName of the file with overviews (without extension):\n> ")
            try:
                data_overview = open(overview + ".txt", "r").read().replace(".", ",").split("\n")
                overview_depts = []
                for row in data_overview:
                    row_split = row.split(delimiter)
                    overview_depts.append(row_split)
                break
            except FileNotFoundError:
                print("\n" + overview + ".txt is not a valid file.\nPlease try again, or press 'ctrl+c' to exit the program.")

    time.sleep(0.2)
    print("\nSTEP 2: Overview per year")
    time.sleep(0.2)
    while True:
            per_year = input("\nName of the file with overviews per year (without extension):\n> ")
            try:
                data_per_year = open(per_year + ".txt", "r").read().replace(".", ",").split("\n")
                per_year_depts = []
                for row in data_per_year:
                    row_split = row.split(delimiter)
                    per_year_depts.append(row_split)
                break
            except FileNotFoundError:
                print("\n" + per_year + ".txt is not a valid file.\nPlease try again, or press 'ctrl+c' to exit the program.")
                time.sleep(0.2)

    time.sleep(0.2)
    print("\nSTEP 3: Overview per category")
    time.sleep(0.2)
    while True:
            per_category = input("\nName of the file with overviews per category (without extension):\n> ")
            try:
                data_per_category = open(per_category + ".txt", "r").read().replace(".", ",").split("\n")
                per_category_depts = []
                for row in data_per_category:
                    row_split = row.split(delimiter)
                    per_category_depts.append(row_split)
                break
            except FileNotFoundError:
                print("\n" + per_category + ".txt is not a valid file.\nPlease try again, or press 'ctrl+c' to exit the program.")

    output_delimiter = input("\nWhat delimiter do you want to use in the output file?\n> ")

    for num in ids_splitted:
        newfile = open("docs/" + str(num[0]) + "_" + num[1] + ".txt", "w")
    #Overview
        newfile.write("Number of journals|Number of publications|jf|jf x number of publications\n")
        for row in overview_depts:
            if row[0] == num[0]:
                for post in row[2:]:
                    newfile.write(str(post + output_delimiter))
                newfile.write("\n")
    #Per year
        newfile.write("\n\nPublication year|Number of journals|Number of publications|jf|jf x number of publications\n")
        for row in per_year_depts:
            if row[0] == num[0]:
                for post in row[1:]:
                    newfile.write(str(post + output_delimiter))
                newfile.write("\n")
    #Per category
        newfile.write("\n\nCategories|Numbers of journals in category|Number of publications in category|jf|jf x number of publications\n")
        for row in per_category_depts:
            if row[0] == num[0]:
                for post in row[2:]:
                    newfile.write(str(post + output_delimiter))
                newfile.write("\n")
    time.sleep(0.5)
    print("\nSuccess! The files can be found in " + os.getcwd() + "/docs")
except KeyboardInterrupt:
    print("\nExit the program.")
