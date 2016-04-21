"""Script for quickly replacing newlines.
All newlines will be replaced with a sign you choose"""

import os

#Print welcome message and information what the script does.
print ("***************************")
print ("Script to replace whitelines.")
print ("This script will replace every single whiteline with a a sign of your choice.")
print ("***************************")
if os.name == 'posix':
    cid = input("Please enter your CID:\nCID: ") #Let user enter CID
    old_ids = input("The name of the file you want to convert:\nFilename (without extension): ") #Let user choose which file to convert
    new_ids = input("What do you want the new file to be named?\nFilename (without extension): ") #Let user name the new file
    replacement = input("What do you want to replace the newline with?\nReplace with: ")
    data = open("/Users/"+cid+"/Desktop/"+old_ids+".txt", "r").read() #Open file with IDs
    data_no_line = data.replace("\n", replacement) #Replace newlines with commas
    newfile = open("/Users/"+cid+"/Desktop/"+new_ids+".txt", "w") #Create new file called what the user choose .txt
    newfile.write(data_no_line) #Write IDs to the new file
    newfile.close() #Close the file
    print ("Ta-dah! File created.") #Message that the convertion is correct

    #Ask if the user wants the results printed out in the terminal
    choice = input("Do you want to open the new file?\n(Y/N) ")
    if choice == "Y" or choice == "y":
        print(open("/Users/"+cid+"/Desktop/"+new_ids+".txt", "r").read())

if os.name == 'nt':
    cid = input("Please enter your CID:\nCID: ") #Let user enter CID
    old_ids = input("The name of the file you want to convert:\nFilename (without extension): ") #Let user choose which file to convert
    new_ids = input("What do you want the new file to be named?\nFilename (without extension): ") #Let user name the new file
    replacement = input("What do you want to replace the newline with?\nReplace with: ")
    data = open("D:\\Users\\"+cid+".NET\\Desktop\\"+old_ids+".txt", "r").read()
    data_no_line = data.replace("\n", replacement) #Replace newlines with commas
    newfile = open("\\Users\\"+cid+"\\Desktop\\"+new_ids+".txt", "w") #Create new file called what the user choose .txt
    newfile.write(data_no_line) #Write IDs to the new file
    newfile.close() #Close the file
    print ("Ta-dah! File created.") #Message that the convertion is correct

    #Ask if the user wants the results printed out in the terminal
    choice = input("Do you want to open the new file?\n(Y/N) ")
    if choice == "Y" or choice == "y":
        print(open("D:\\Users\\"+cid+".NET\\Desktop\\"+new_ids+".txt", "r").read())
