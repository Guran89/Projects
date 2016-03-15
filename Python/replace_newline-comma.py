"""Script for quickly replacing newlines with commas.
All newlines will be replaced with a comma"""

#Print welcome message and information what the script does.
print("***************************")
print("Script to replace whitelines with commas.")
print("This script will replace every single whiteline with a comma.")
print("***************************")

cid = input("Please enter your CID:\nCID: ") #Let user enter CID
old_ids = input("The name of the file you want to convert:\nFilename (without extension): ") #Let user choose which file to convert
new_ids = input("What do you want the new file to be named?\nFilename (without extension): ") #Let user name the new file
data = open("/Users/"+cid+"/Desktop/"+old_ids+".txt", "r").read() #Open file with IDs
data_no_line = data.replace("\n", ", ") #Replace newlines with commas
newfile = open(new_ids+".txt", "w") #Create new file called what the user choose .txt
newfile.write(data_no_line) #Write IDs to the new file
newfile.close() #Close the file
print("Ta-dah! File created.") #Message that the convertion is correct
