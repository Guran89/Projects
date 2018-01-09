# encoding: utf8

# Import necessary packages
import os, sys, time
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
        if os.name == 'posix': #MacOS
            data = open(cwd + "/../input_files/publications_wos.txt", encoding='utf-8').read() # Import publication data
            path = "wos"
        elif os.name == 'nt': #Windows
            data = open(cwd + "\\..\\input_files\\publications_wos.txt", encoding='utf-8').read() # Import publication data
            path = "wos"
    elif database == "sco":
        if os.name == 'posix': #MacOS
            data = open(cwd + "/../input_files/publications_scopus.txt", encoding='utf-8').read() # Import publication datase
            path = "scopus"
        elif os.name == 'nt': #Windows
            data = open(cwd + "\\..\\input_files\\publications_scopus.txt", encoding='utf-8').read() # Import publication datase
            path = "scopus"
    else:
        print("Wrong input. Try again.")
        quit()

    if os.name == 'posix': #MacOS
        list_of_countries = open(cwd + "/../input_files/countries.txt").read() # Import data of existing countries
    elif os.name == 'nt': #Windows
        list_of_countries = open(cwd + "\\..\\input_files\\countries.txt").read() # Import data of existing countries

    # Split data
    list_of_countries = list_of_countries.split('\n')
    data = data.split('\n')

    data_year = [] # Create empty array to store the publication years

    # Get publication years from the data and add them to the array
    for row in data:
        splitted_row = row.split("\t")
        data_year.append(splitted_row)

        years_in_data = set()

        for aff, year in data_year:
            years_in_data.add(year)

    print("The following years are available in the data:\n")
    for year in sorted(years_in_data):
        print(year)

    found_countries = [] # Create empty array to store all the countries in the publication data
    found_countries_no_swe = [] # Create empty array to store all countries except Sweden

    set_year = input("\nWhich year do you want data for?\n> ") # Get the year you want to export

    # Function to extract countries from the data file and put them in the found_countries array
    for row in data:
        for country in list_of_countries: # Identify which countries are relevant to look for in the data
            if country in row and set_year in row:
                found_countries.append(country) # Add found countries to the found_countries array

    for country in found_countries:
        if country != "Sweden":
            found_countries_no_swe.append(country) # Add found countries to the found_countries_no_swe array

    cooperation_counter = 0 # Count the number of cooperations

    found_countries_no_swe = set(found_countries_no_swe)

    for row in data:
        for country in found_countries_no_swe:
            if country in row and set_year in row:
                cooperation_counter += 1
                break

    counted_countries = Counter(found_countries) # Count number of occurrences of each country
    counted_countries_no_swe = Counter(found_countries_no_swe) # Count number of occurrences of each country
    if os.name == 'posix': #MacOS
        newfile = open(cwd + "/../output_files/" + path + "/output_" + set_year + "_" + database + ".csv", "w") # Create a new file
    elif os.name == 'nt': #Windows
        newfile = open(cwd + "\\..\\output_files\\" + path + "\\output_" + set_year + "_" + database + ".csv", "w") # Create a new file

    # Loop for getting info to write to file
    for i, j in counted_countries.items():
        to_write = i + ";" + str(j) + "\n"
        newfile.write(to_write)
    newfile.write("Totalt antal samarbeten;" + str(cooperation_counter))
    newfile.close()

    time.sleep(0.2)
    #Print end message
    print("\n*****************************************************************\n")
    print("Success! You can find the finished files in the directory: ")
    if database == "wos":
        print("output_files/wos")
    elif database == "sco":
        print("output_files/scopus")
    print("\n*****************************************************************\n")

except KeyboardInterrupt:
    print("\nProgram exited")
