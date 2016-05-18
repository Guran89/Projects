"""Script for quickly replacing newlines.
All newlines will be replaced with a sign you choose"""

import os

#Print welcome message and information what the script does.
print ("\n***************************")
print ("Script to replace newlines.")
print ("This script will replace every single newline with a a sign of your choice.")
print ("Observe that the script only works with .txt files at the moment.")
print ("Instructions: Put the .txt file you want to convert on the desktop. Follow the steps below.")
print ("***************************\n")

#Script for computers running OSX
if os.name == 'posix':
    cid = input("Please enter your CID:\nCID: ") #Let user enter CID
    old_ids = input("\nThe name of the file you want to convert:\nFilename (without extension): ") #Let user choose which file to convert
    new_ids = input("\nWhat do you want the new file to be named?\nFilename (without extension): ") #Let user name the new file
    replacement = input("\nWhat do you want to replace the newline with?\nReplace with: ") #Let user choose a sign that will replace the newline
    data = open("/Users/"+cid+"/Desktop/"+old_ids+".txt", "r").read() #Open file to be modified
    data_no_line = data.replace("\n", replacement) #Replace newlines with the chosen sign
    newfile = open("/Users/"+cid+"/Desktop/"+new_ids+".txt", "w") #Create new file called what the user choose .txt
    newfile.write(data_no_line) #Write to the new file
    newfile.close() #Close the file
    print ("\nTa-dah! File created.\nYou can find at: /Users/"+cid+"/Desktop/") #Message that the convertion is correct

    #Ask if the user wants the results printed out in the terminal
    choice = input("\nDo you want to open the new file?\n(Y/N) ")
    if choice == "Y" or choice == "y":
        print(open("/Users/"+cid+"/Desktop/"+new_ids+".txt", "r").read())

#Script for computers running Windows
if os.name == 'nt':
    cid = input("\nPlease enter your CID:\nCID: ") #Let user enter CID
    harddrive = input("\nWhat harddrive do you use?\nHarddrive (D or C, for example):") #Which harddrive is the desktop located in?
    old_ids = input("\nThe name of the file you want to convert:\nFilename (without extension): ") #Let user choose which file to convert
    new_ids = input("\nWhat do you want the new file to be named?\nFilename (without extension): ") #Let user name the new file
    replacement = input("\nWhat do you want to replace the newline with?\nReplace with: ") #Let user choose a sign that will replace the newline
    data = open(harddrive+":\\Users\\"+cid+".NET\\Desktop\\"+old_ids+".txt", "r").read() #Open file to be modified
    data_no_line = data.replace("\n", replacement) #Replace newlines with the chosen sign
    newfile = open(harddrive+":\\Users\\"+cid+".NET\\Desktop\\"+new_ids+".txt", "w") #Create new file called what the user choose .txt
    newfile.write(data_no_line) #Write to the new file
    newfile.close() #Close the file
    print ("\nTa-dah! File created.\nYou can find at: "+harddrive+":\\Users\\"+cid+".NET\\Desktop") #Message that the convertion is correct

    #Ask if the user wants the results printed out in the terminal
    choice = input("\nDo you want to open the new file?\n(Y/N) ")
    if choice == "Y" or choice == "y":
        print(open(harddrive+":\\Users\\"+cid+".NET\\Desktop\\"+new_ids+".txt", "r").read())
