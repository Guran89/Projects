import os, sys

###STAGE 1###
#Check the version of Python to make sure that it is at least Python 3
py_version = sys.version_info.major
if py_version < 3:
    print("You need a newer version of Python. You are running version " + str(py_version) + ".")
    print("Please install version 3.x and try again.")
    quit()

#Make sure there is a correct dir for input files
if not os.path.exists("input_files"):
    os.makedirs("input_files")
    print("There wasn't any input directory, so I made one for you.")
    print("Please put the input files in the input directory and run the script again.")
    quit()

#If there is not a directory for the output files, create one
if not os.path.exists("output_files"):
    os.makedirs("output_files")


###STAGE 2###

#Read and prepare all the input files
all_files = []
for post in os.listdir("input_files/"):
    if post.endswith(".txt"):
        all_files.append(open("input_files/" + post, "r").read().replace(".", ",").split("\n"))


###STAGE 3###

#Create empty array to store the headers from the input files
headers = []

#Get headers from the input files and store in headers array
for row in all_files:
    headers.append(row[0].split(";"))

for row in all_files:
    del(row[0])

#Create empty array to store the IDs from the files
ids = set()

#Access the IDs and save in ids array
for post in all_files:
    for i in post:
        temp_split = i.split(";")
        ids.add(temp_split[0])

###TEMP!###

headerDict = dict()
dictcount = 0
for h in headers:
    headerDict[dictcount] = h
    dictcount += 1

fileDict = dict()
fileDictCount = 0
for f in all_files:
    fileDict[fileDictCount] = f
    fileDictCount += 1

newfile = ""
for i in ids:
    newfile = open("output_files/" + i + ".txt", "w")
    newfile.write(";".join(headerDict[0]))
    newfile.write("\n")
    newfile.close()

def printHeader(count):
    for key, header in headerDict.items():
        if key == count:
            newfile.write(";".join(header))

def printFile(instID):
    headcount = 1
    for i, j in fileDict.items():
        for k in j:
            tempsplit = k.split(";")
            if str(instID) == tempsplit[0]:
                newfile = open("output_files/" + instID + ".txt", "a")
                print(";".join(tempsplit))
                newfile.write(";".join(tempsplit))
                newfile.write("\n")
        if headcount <= len(headerDict)-1:
            newfile.write(";".join(headerDict[headcount]))
            newfile.write("\n")
        headcount += 1

    newfile.close()

for i in ids:
    printFile(i)

for i in ids:
    print(i)
