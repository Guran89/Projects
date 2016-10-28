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
    print("Please put the input files in the input directory and run this script again.")
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

all_files_temp = []

#Create empty array to store the IDs from the files
ids = []

#Access the IDs and save in ids array
for post in all_files:
    for i in post:
        ids.append(i[0])

for post in all_files:
    for i in post:
        split = i.split(";")
        all_files_temp.append(split)

headcount = 0

for i in ids:
    newfile = open("output_files/" + i + ".txt", "w")
    for header in headers:
        newfile.write(";".join(header))
        newfile.write("\n")
    for j in all_files_temp:
        if int(j[0]) == int(i):
            newfile.write(";".join(j))
            newfile.write("\n")
    headcount += 1


###TILLFÄLLIGT!###

myDict = []
headercount = 0
for h in headers:
    header = {headercount: h}
    myDict.append(header)
    headercount += 1
print(myDict)
