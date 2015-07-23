__author__ = ('sushan', 'kristoka')

#Importerar nödvändiga paket
import itertools
from itertools import chain, combinations
import os
from collections import Counter

pubid_deptname_org = open('C:\Progs\Python34\Pythonfiles\g_c_12_14.txt', 'r', encoding='utf8') #Öppnar fil som ska konverteras

pubid = [] #Skapar tom lista för publikations-ID
dept = [] #Skapar tom för lista institutions-ID

#Splittar varje rad i f på ; och lägger till institutionsnamnet i dept. ".strip()" returnerar en kopia av en textsträng där 
#whitespace raderats i början och slutet av varje sträng.
for i in pubid_deptname_org:
    list = [elt.strip() for elt in i.split(";")]
    pubid.append(list[0])
    dept.append(list[1])

dept_set = set(dept) #Tar bort dubbletter ur dept
dept_set = sorted(dept_set) #Sorterar institutionerna alfabetiskt

count = 0 #Skapar count för att räkna institutioner
ids = [] #Tom lista för institutionernas id-nummer

#Räknar antalet institutioner och skapar ett ID-nummer för varje institution som läggs till i ids
for i in dept_set:
    count = count+1
    ids.append(count)

id_dept_dict = {dept_set[n]: ids[n] for n in range(len(ids))} #Dictionary för id-nummer samt institutionsnamn

dept_ids = [] #Skapar lista för institution och institutions-ID

#Fyller dept_ids med institutions-ID och institutionsnamn
for i in dept:
    dept_ids.append(id_dept_dict.get(i))

pubid_deptid = zip(pubid,dept_ids) #Skapar och fyller lista med publikations-ID och institutions-ID
pubid_deptid_set = set(pubid_deptid) #Tar bort eventuella dubletter
pubid_deptid_set = sorted(pubid_deptid_set) #Sorterar setet

pubid_deptid_dict = {} #Skapar ett tomt dictionary för publikations-ID och institutions-ID för varje publikation

#Fyller pubid_deptid_dict med unika publikations-ID på varje rad, följt av samtliga institutions-ID som förekommer i publikationen
for line in pubid_deptid_set:
    if line[0] in pubid_deptid_dict:
        pubid_deptid_dict[line[0]].append(str(line[1]))
    else:
        pubid_deptid_dict[line[0]] = [str(line[1])]


dept_id_elements = [] #Skapar tom lista för institutions-ID grupperat efter publikation, men utan publikations-ID

#Fyller listan dept_id_elements med institutions-ID
for key in set(pubid):
    dept_id_elements.append(pubid_deptid_dict[key])

output = Counter(chain.from_iterable(combinations(line, 2) for line in dept_id_elements)) #Skapar dictionary med institutionspar samt antal publikationer de samskrivit

keylist = [] #Skapar tom lista för samtliga instutionspar som samskrivit

#Fyller keylist med samtliga instutionspar som samskrivit
for key1, key2 in output:
    keylist.append((int(key1), int(key2)))

valuelist = [] #Skapar tom lista för antal samskrivna publikationer av varje institutionspar, men utan institutions-ID

#Fyller valuelist med antal samskrivna publikationer av varje institutionspar, men utan instituions-ID
for value in output.keys():
    valuelist.append(int("%s" % (output[value])))

keyvalue_zip = zip(keylist, valuelist) #Kombinerar listorna keylist och valuelist

edgecount = 0 #Skapar count för att räkna samarbeten mellan institutioner

#Räknar antal samarbeten mellan institutioner
for line in output:
    edgecount = edgecount + 1

#Funktion som skriver en utfil med id samt institutionsnamn
def print_file(filename):
    os.chdir('C:\Progs\Python34\Pythonfiles') #Bestämmer directory för utfilen

    file = open(filename, 'w') #Skapar fil att skriva till
	
    file.write('*Vertices ' + str(count) + '\n') #Skapar rubrik i filen samt räknar antal institutioner

	#Skriver institutions-ID samt institutionsnamn
    for keys, values in id_dept_dict.items():
        keys = str(keys)
        values = str(values)
        to_write = values + ' ' + keys
        file.write(to_write + '\n')

    file.write('*Edges ' + str(edgecount)) #Skapar rubrik i filen samt räknar antal samarbeten mellan varje institutionspar

	#Skriver institutionspar samt antal publikationer institutionerna samskrivit
    for line in output.items():
        file.write(str(line).replace('(', '').replace(')', '').replace("'", '').replace(',', '') + '\n')

    file.close()

print_file('network.net') #Kör funktionen print_file


