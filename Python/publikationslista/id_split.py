#encoding: utf8
#Import necessary packages
import os, sys, time


###STAGE 1###
try:
    #Check the version of Python to make sure that it is at least Python 3. Otherwise, let the user know and abort script
    py_version = sys.version_info.major
    if py_version < 3:
        print("You need a newer version of Python. You are running version " + str(py_version) + ".")
        print("Please install Python version 3.x and try again.\nYou can find the latest version on www.python.org.")
        quit()

    #Make sure there is a correct directory for input files, otherwise create one and inform user to put input files in new directory
    if os.name == 'posix': #MacOS
        if not os.path.exists("input_files/"):
            os.makedirs("input_files/")
            print("There wasn't any input directory, so I created one for you.")
            print("Please put the input files in the input_files directory and run the script again.")
            quit()
    elif os.name == 'nt': #Windows
        if not os.path.exists("input_files\\"):
            os.makedirs("input_files\\")
            print("There wasn't any input directory, so I created one for you.")
            print("Please put the input files in the input_files directory and run the script again.")
            quit()

    #If there is not a directory for the output files, create one
    if os.name == 'posix': #MacOS
        if not os.path.exists("output_files/"):
            os.makedirs("output_files/")
    elif os.name == 'nt': #Windows
        if not os.path.exists("output_files\\"):
            os.makedirs("output_files\\")

    #Print welcome message and instructions
    print("\n*****************************************************************\n")
    print("This script takes one or more files and separates the\ndata regarding to some kind of ID.\n")
    print("Make sure that the first column in every file is the ID\nyou want to use to separate the files.\n")
    print("You can exit the program at any time by pressing 'Ctrl+c'\n")
    if os.name =='posix': #MacOS
        print("We will use the files found in the directory\n" + os.getcwd() + "/input_files")
    elif os.name == 'nt': #Windows
        print("We will use the files found in the directory\n" + os.getcwd() + "\\input_files")
    print("\n*****************************************************************\n")

    #Get the delimiter used in the files
    delimiter = input("What delimiter is used in the input files?\n> ")
    time.sleep(0.2)
    #Check if the files have headers
    ifHeader = input("\nAre there headers in the input files? (y/n)\n> ")
    time.sleep(0.2)
    #Get the delimiter to use in the output files
    outDelimiter = input("\nWhat delimiter do you want to use in the output files?\n> ")


    ###STAGE 2###

    #Read and prepare all the input files
    all_files = []
    if os.name == 'posix': #MacOS
        for post in os.listdir("input_files/"):
            if post.endswith(".txt") or post.endswith(".csv"):
                all_files.append(open("input_files/" + post, "r").read().replace(".", ",").split("\n"))
    elif os.name == 'nt': #Windows
        for post in os.listdir("input_files\\"):
            if post.endswith(".txt") or post.endswith(".csv"):
                all_files.append(open("input_files\\" + post, "r", encoding="utf8").read().replace(".", ",").split("\n"))

    #Create empty array to store the headers from the input files
    headers = []

    #Get headers from the input files and store in headers array
    for row in all_files:
        headers.append(row[0].split(delimiter))

    #Delete the headers row from the files (they are now available in the headers array)
    if ifHeader == 'y' or ifHeader == 'Y' or ifHeader == 'yes' or ifHeader == 'Yes':
        for row in all_files:
            del(row[0])

    #Create empty set to store the IDs from the files
    ids = set()

    #Access the IDs and save in ids set
    for post in all_files:
        for i in post:
            temp_split = i.split(delimiter)
            ids.add(temp_split[0])


    ###STAGE 3###

    #Create dictionary to store headers
    headerDict = dict()

    #Add headers to headers dictionary
    dictcount = 0
    for h in headers:
        headerDict[dictcount] = h
        dictcount += 1

    #Create dictionary to store input files
    fileDict = dict()

    #Add files to files dictionary
    fileDictCount = 0
    for f in all_files:
        fileDict[fileDictCount] = f
        fileDictCount += 1

    #Create documents in the output directory to write to
    newfile = ""
    for i in ids:
        if os.name == 'posix': #MacOS
            newfile = open("output_files/" + i + ".txt", "w")
        elif os.name == 'nt': #Windows
            newfile = open("output_files\\" + i + ".txt", "w")
        newfile.write(outDelimiter.join(headerDict[0]))
        newfile.write("\n")
        newfile.close()

    #Function to write to the documents
    def printFile(instID):
        headcount = 1
        for i, j in fileDict.items():
            for k in j:
                tempsplit = k.split(delimiter)
                if str(instID) == tempsplit[0]:
                    if os.name == 'posix': #MacOS
                        newfile = open("output_files/" + instID + ".txt", "a")
                    elif os.name == 'nt': #Windows
                        newfile = open("output_files\\" + instID + ".txt", "a")
                    newfile.write(outDelimiter.join(tempsplit))
                    newfile.write("\n")
            if headcount <= len(headerDict)-1:
                newfile.write("\n")
                newfile.write(outDelimiter.join(headerDict[headcount]))
                newfile.write("\n")
            headcount += 1

        newfile.close()

    #Run function for every ID
    for i in ids:
        printFile(i)

    time.sleep(0.2)
    #Print end message
    print("\n*****************************************************************\n")
    print("Success! You can find the finished files in: ")
    if os.name == 'posix': #MacOS
        print(os.getcwd() + "/output_files/")
    elif os.name == 'nt': #Windows
        print(os.getcwd() + "\\output_files\\")
    print("\n*****************************************************************\n")

except KeyboardInterrupt:
    print("\nProgram exited")
