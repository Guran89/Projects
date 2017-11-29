# encoding: utf8

# Import necessary packages
import os, sys
from collections import Counter

cwd = os.getcwd() # Get the current working directory

try:
    # Check the version of Python to make sure that it is at least Python 3. Otherwise, let the user know and abort script
    py_version = sys.version_info.major
    if py_version < 3:
        print("\nYou need a later version of Python. You are running version " + str(py_version) + ".\n")
        print("Please install Python version 3.x and try again.\nYou can find the latest version on www.python.org.\n")
        quit()

    database = input("What database is the data downloaded from?\nEnter 'wos' for Web of Science or 'sco' for Scopus\n> ")
    # Open the relevant documents and import data
    if database == "wos":
        data = open(cwd + "/publications_wos.txt").read() # Import publication data
    elif database == "sco":
        data = open(cwd + "/publications_scopus.txt").read() # Import publication datase
    else:
        print("Wrong input. Try again.")
        quit()

    list_of_countries = open(cwd + "/countries.txt").read() # Import data of existing countries

    # Split data
    list_of_countries = list_of_countries.split('\n')
    data = data.split('\n')

    data_year = [] # Create empty array to store the publication years

    # Get publication years from the data and add them to the array
    for row in data:
        splitted_row = row.split("|")
        data_year.append(splitted_row)

        years_in_data = set()

        for aff, year in data_year:
            years_in_data.add(year)

    print("The following years are available in the data:")
    for year in sorted(years_in_data):
        print(year)

    found_countries = [] # Create empty array to store all the countries in the publication data

    set_year = input("Which year do you want data for?\n> ") # Get the year you want to export

    # Main function of the script
    for row in data:
        #choose_year = min(years_in_data)
        #set_year = int(choose_year)
        for country in list_of_countries: # Identify which countries are relevant to look for in the data
            if country in row and set_year in row:
                found_countries.append(country) # Add found countries to the found_countries array
                #set_year += 1

    counted_countries = Counter(found_countries) # Count number of occurrences of each country

    newfile = open(cwd + "/output" + set_year + "_" + database + ".csv", "w") # Create a new file

    # Loop for getting info to write to file
    for i, j in counted_countries.items():
        to_write = i + "," + str(j) + "\n"
        newfile.write(to_write)

    newfile.close()

except KeyboardInterrupt:
    print("\nProgram exited")
