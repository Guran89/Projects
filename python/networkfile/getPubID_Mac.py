
"""Scriptet används för att hitta pubid där BÅDE instance 1 och 2 förekommer, 
utifrån en metriutsökning av ALLA publikationer och deras instanceid. Exempel på hur
in-fil ska se ut:

165748; 1, 2, 1, 1, 2
196423; 2, 1, 
201569; 1, 1, 1, 
"""

def getPubID(input_file):
   #Importerar nödvändiga moduler och sätter varifrån filer läses in och hamnar efter scriptet är färdigt
   import os
   os.chdir('/Users/kristoka/Desktop') #Fyll i ditt CID där det står ”CID” till vänster
   
   #Funktionen för att läsa in och förbereda filen från SQL för vidare användning
   f = open(input_file)
   pubids = open('pubids.txt', 'w')
   for line in f:
        #Splittar varje rad i filen på ";"
        list = i.split(";")
        pubid = []
        #Söker efter substrängarna '2, 1' eller '1, 2' i strängen list[1]
        if '2, 1' in list[1]:
            #Lägger rätt id i pubid
            pubid.append(list[0])
        elif '1, 2' in list[1]:
            pubid.append(list[0])
        #Splittar strängen pubid och sparar sedan till filen pubids.txt på skrivbordet
        for i in pubid:
            i.split(";")
            pubids.write(i + ',')


getPubID('pubids_input.txt')

