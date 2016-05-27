#encoding: utf-8
"""Script to ready files for import to the persons_cid and cross_persons_cid tables in metri.
The script replaces all tabs with commas, and saves the file as .csv.
"""
import os

cid = input("Please enter your CID:\n> ")
filename = input("File to transform? (Without extension)\n> ")
filechoice = input("1: persons_cid\n2: cross_persons_cid\n> ")

data = open("/Users/"+cid+"/Desktop/"+filename+".txt", "r").read()
data_r = data.replace("\t", ";")

newfilename = ""

if filechoice == "1":
    newfilename = "persons_cid_import.csv"
elif filechoice == "2":
    newfilename = "cross_persons_cid_import.csv"
else:
    newfilename = "default.csv"

newfile = open("/Users/"+cid+"/Desktop/"+newfilename, "w")
newfile.write(data_r)
newfile.close()
