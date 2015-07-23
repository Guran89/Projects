__author__ = 'sushan'

"""Scriptet används för att hitta pubid där BÅDE instance 1 och 2 förekommer, 
utifrån en metriutsökning av ALLA publikationer och deras instanceid. Exempel på hur
in-fil ska se ut:

165748; 1, 2, 1, 1, 2
196423; 2, 1, 
201569; 1, 1, 1, 
"""


def getPubID(input_file):
    import os
    #Ändra till ditt CID
    os.chdir('D:/Users/sushan.NET/Desktop')
    f = open(input_file)
    pubids = open('pubids.txt', 'w')
    for line in f:
        #Splitar varje rad i filen på ","
        list = [elt.strip() for elt in line.split(";")]

        pubid = []

        #Söker efter substrängarna '2; 1' eller '1; 2' i strängen list[1]
        if '2, 1' in list[1]:
            #lägger rätt id i pubid
            pubid.append(list[0])

        elif '1, 2' in list[1]:
            pubid.append(list[0])

        #Splitar strängen pubid och printar tecken 1-6
        for i in pubid:
            i.split(";")
            pubids.write(i + ',')

#Ändra till rätt directory och filnamn för utfilen från metri
getPubID('D:/Users/sushan.NET/Desktop/samarbeten.txt')


