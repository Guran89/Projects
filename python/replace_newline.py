#encoding: utf-8
"""Script for quickly replacing newlines.
All newlines will be replaced with a sign you choose"""

import os
import time

#Print welcome message and information what the script does.
print ("\n**************************************************************************")
print ("Script to replace newlines.")
print ("This script will replace every newline with a a sign of your choice.")
print ("Observe that the script only works with .txt files at the moment.")
print ("Instructions: Put the .txt file you want to convert on the desktop.\nFollow the steps below.")
print ("**************************************************************************\n")

#Create empty variables
sign = ""
old_ids = ""
new_ids = ""
replacement = ""

#Define function for user to enter information
def enter_info():
    global sign
    global old_ids
    global new_ids
    global replacement
    sign = input("Please enter your signature:\nSignature: ") #Let user enter signatur
    old_ids = input("\nThe name of the file you want to convert:\nFilename (without extension): ") #Let user choose which file to convert
    new_ids = input("\nWhat do you want the new file to be named?\nFilename (without extension): ") #Let user name the new file
    replacement = input("\nWhat do you want to replace the newline with?\nReplace with: ") #Let user choose a sign that will replace the newline

#Script for computers running OSX
if os.name == 'posix':
    enter_info()
    data = open("/Users/"+sign+"/Desktop/"+old_ids+".txt", "r").read() #Open file to be modified
    data_no_line = data.replace("\n", replacement) #Replace newlines with the chosen sign
    newfile = open("/Users/"+sign+"/Desktop/"+new_ids+".txt", "w") #Create new file called what the user choose .txt
    newfile.write(data_no_line) #Write to the new file
    newfile.close() #Close the file
    print("Working...")
    time.sleep(1) #Dramatic pause
    print ("\nTa-dah! File created.\nYou can find it at: /Users/"+sign+"/Desktop/"+new_ids+".txt") #Message that the convertion is correct

    #Ask if the user wants the results printed out in the terminal
    choice = input("\nDo you want to see the results?\n(Y/N) ")
    if choice == "Y" or choice == "y":
        print(open("/Users/"+sign+"/Desktop/"+new_ids+".txt", "r").read())

#Script for computers running Windows
if os.name == 'nt':
    enter_info()
    harddrive = input("\nWhat harddrive do you use?\nHarddrive (D or C, for example):") #Which harddrive is the desktop located in?
    data = open(harddrive+":\\Users\\"+sign+".NET\\Desktop\\"+old_ids+".txt", "r").read() #Open file to be modified
    data_no_line = data.replace("\n", replacement) #Replace newlines with the chosen sign
    newfile = open(harddrive+":\\Users\\"+sign+".NET\\Desktop\\"+new_ids+".txt", "w") #Create new file called what the user choose .txt
    newfile.write(data_no_line) #Write to the new file
    newfile.close() #Close the file
    print("Working...")
    time.sleep(1) #Dramatic pause
    print ("\nTa-dah! File created.\nYou can find it at: "+harddrive+":\\Users\\"+sign+".NET\\Desktop"+new_ids+".txt") #Message that the convertion is correct

    #Ask if the user wants the results printed out in the terminal
    choice = input("\nDo you want to see the results?\n(Y/N) ")
    if choice == "Y" or choice == "y":
        print(open(harddrive+":\\Users\\"+sign+".NET\\Desktop\\"+new_ids+".txt", "r").read())
