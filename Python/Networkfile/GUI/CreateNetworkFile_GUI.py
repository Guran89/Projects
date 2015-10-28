from tkinter import *
import tkinter.filedialog as tkFileDialog
#import itertools
from itertools import chain, combinations
import os
from collections import Counter

# *** Functions ***
def askopenfile():
     global pubid_deptname_org
     pubid_deptname_org = tkFileDialog.askopenfile(mode='r')
     #pubid_deptname_org = pubid_deptname_org.read()
     print(pubid_deptname_org)

def askdirectory():
    global target_path
    target_path = tkFileDialog.askdirectory()
    os.chdir(target_path)
    print(target_path)

def converter():
    pubid = [] #Skapar tom för publikations-ID
    dept = [] #Skapar tom för institutions-ID

#Splittar varje rad i f på ; och lägger till institutionsnamnet i dept. ".strip()" returnerar en kopia av en textsträng där
#whitespace raderats i början och slutet av varje sträng.
    for i in pubid_deptname_org:
        list = [elt.strip() for elt in i.split(";")]
        pubid.append(list[0])
        dept.append(list[1])

    dept_set = set(dept) #Tar bort dubbletter ur dept
    dept_set = sorted(dept_set) #Sorterar institutionerna alfabetiskt

    verticecount = 0 #Skapar count för att räkna institutioner

    ids = [] #Tom lista för institutionernas ID-nummer

    #Räknar antalet institutioner och skapar ett ID-nummer för varje institution som läggs till i ids
    for i in dept_set:
        verticecount = verticecount + 1
        ids.append(verticecount)

    d = {dept_set[n]: ids[n] for n in range(len(ids))} #Dictionary för id-nummer samt institutionsnamn

    dept_ids = [] #Skapar lista för institution och institutions-ID

    #Fyller dept_ids med institutions-ID och institutionsnamn
    for i in dept:
        dept_ids.append(d.get(i))

    pubid_deptid = zip(pubid,dept_ids) #Skapar och fyller lista med publikations-ID och institutions-ID
    pubid_deptid_set = set(pubid_deptid) #Tar bort eventuella dubletter
    pubid_deptid_set = sorted(pubid_deptid_set) #Sorterar setet

    pubdict = {} #Skapar ett dictionary för publikations-ID och institutions-ID för varje publikation

    #Fyller pubdict med unika publikations-ID på varje rad, följt av samtliga institutions-ID som förekommer i publikationen
    for line in pubid_deptid_set:
        if line[0] in pubdict:
            pubdict[line[0]].append(str(line[1]))
        else:
            pubdict[line[0]] = [str(line[1])]

    element = [] #Skapar lista för institutions-ID grupperat efter publikation, men utan publikations-ID

    #Fyller listan element med institutions-ID
    for key in set(pubid):
        element.append(pubdict[key])

    output = Counter(chain.from_iterable(combinations(line, 2) for line in element)) #Skapar dictionary med institutionspar samt antal publikationer de samskrivit

    keylist = [] #Skapar lista med samtliga instutionspar som samskrivit

    #Fyller keylist med samtliga instutionspar som samskrivit
    for key1, key2 in output:
        keylist.append((int(key1), int(key2)))

    valuelist = [] #Skapar lista på antal samskrivna publikationer av varje institutionspar, men utan institutions-ID

    #Fyller valuelist med antal samskrivna publikationer av varje institutionspar, men utan instituions-ID
    for value in output.keys():
        valuelist.append(int("%s" % (output[value])))

    keyvalue_zip = zip(keylist, valuelist) #Kombinerar listorna keylist och valuelist

    edgecount = 0 #Skapar count för att räkna samarbeten mellan institutioner

    #Räknar antal samarbeten mellan institutioner
    for line in output:
        edgecount = edgecount + 1

    #Funktion som skriver en utfil med IDs samt institutionsnamn
    def print_file(filename):
        os.chdir(target_path) #Bestämmer directory för utfilen

        file = open(filename + '.net', 'w') #Skapar fil att skriva till

        file.write('*Vertices ' + str(verticecount) + '\n') #Skapar rubrik i filen samt räknar antal institutioner

        #Skriver institutions-ID samt institutionsnamn
        for keys, values in d.items():
            keys = str(keys)
            values = str(values)
            to_write = values + ' ' + keys
            file.write(to_write + '\n')

        file.write('*Edges ' + str(edgecount) + '\n') #Skapar rubrik i filen samt räknar antal samarbeten mellan varje institutionspar

        #Skriver institutionspar samt antal publikationer institutionerna samskrivit
        for line in output.items():
            file.write(str(line).replace('(', '').replace(')', '').replace("'", '').replace(',', '') + '\n')

    title = fld_output.get()
    print_file(title)


root = Tk() #Create main window

#Create frame
frame = Frame(root)
frame.pack()

#Create menu
mainMenu = Menu(frame)
root.config(menu = mainMenu)
fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label = "File", menu = fileMenu)
fileMenu.add_command(label = "Avsluta", command = quit)

#Create labels
lbl_input = Label(frame, text = "Input-fil:")
lbl_file = Label(frame, text = "Ingen fil vald")
lbl_target = Label(frame, text = "Målplats:")
lbl_file_target = Label(frame, text = "Ingen målplats vald")
lbl_output = Label(frame, text = "Namn på utfil:")

#Create fields
fld_input = Entry(frame)
fld_target = Entry(frame)
fld_output = Entry(frame)

#Create buttons
btn_input = Button(frame, text = "Välj fil...", command = askopenfile)
btn_target = Button(frame, text = "Välj mål...", command = askdirectory)
btn_convert = Button(frame, text = "Konvertera", command = converter)
btn_quit = Button(frame, text = "Avsluta", command = quit)

#Placera ut inputs
lbl_input.grid(row = 0, column = 0, sticky = W)
#fld_input.grid(row = 1, column = 0)
btn_input.grid(row = 1, column = 0, sticky = W)
lbl_file.grid(row = 0, column = 1, sticky = W)

#Placera ut targets
lbl_target.grid(row = 2, column = 0, sticky = W)
#fld_target.grid(row = 3, column = 0)
btn_target.grid(row = 3, column = 0, sticky = W)
lbl_file_target.grid(row = 2, column = 1, sticky = W)

#Placera ut outputs
lbl_output.grid(row = 4, column = 0, sticky = W)
fld_output.grid(row = 4, column = 1)

#Placera ut convert och Quit
btn_convert.grid(row = 6, column = 0, sticky = W, pady = 2)
btn_quit.grid(row = 6, column = 1, sticky = W, pady = 2)


status = Label(root, text = "Preparing to do nothing...", bd = 1, relief = SUNKEN, anchor = W)
status.pack(side = BOTTOM, fill = X, pady = 2)

root.title("Networkfile Converter, Beta")
root.mainloop() #Keeps the program running