import os, time

if not os.path.exists("docs"):
    os.makedirs("docs")
print("\n*****************************************************")
print("Make sure the department's ID is in the first column,\nand that all the IDs are in the ids.txt file.")
print("*****************************************************\n")


filename = input("What's the name of the file you want to convert? (including extension)\n> ")

data = open(filename, "r").read().split("\n")
ids_open = open("ids.txt", "r").read().split("\n")

ids = [] #List to store the IDs

#Split the IDs and store in the list
for i in ids_open:
    temp = i.split(";")
    ids.append(temp)

depts = [] #List to store the data to split by department

delimiter = input("What's the delimiter of the file?\n> ") #Ask user what delimiter the file uses

#Split att append data to the depts list
for row in data:
    temp = row.split(delimiter)
    depts.append(temp)

#Main loop
for num in ids:
    #Create documents to store the manipulated data
    newfile = open("docs/" + str(num[0]) + "_" + num[1] + ".txt", "w")
    for row in depts:
        if row[0] == num[0]:
            for post in row:
                newfile.write(str(post + "|"))
            newfile.write("\n")
    newfile.close()
print("Working...")
time.sleep(1)
print("Done!")
