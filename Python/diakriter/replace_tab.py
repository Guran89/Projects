#coding: utf-8


cid = input("Please enter your CID:\nCID: ")
in_data = input("The name of the file you want to convert:\nFilename (with extension): ")
out_data = input("What do you want the new file to be named?\nFilename (with extension): ")
data = open("/Users/"+cid+"/Desktop/"+in_data, "r").read()

print("Counting occurrences of potential characters. Please wait.")

data = data.replace(" \t", "")
data = data.replace("\t ", "")
data = data.replace(" \n", "")
data = data.replace("\n ", "")

pipe_count = 0
hash_count = 0
pound_count = 0
dollar_count = 0
for i in data:
    if i == "|":
        pipe_count = pipe_count + 1
    elif i == "#":
        hash_count = hash_count + 1
    elif i == "£":
        pound_count = pound_count + 1
    elif i == "$":
        dollar_count = dollar_count + 1

print("Pipe (|): " + str(pipe_count))
print("Hash (#): " + str(hash_count))
print("Pound (£): " + str(pound_count))
print("Dollar ($): " + str(dollar_count))

new_char = input("What character would you like to replace with?\n>")
data_replaced = data.replace("\t", new_char)
newfile = open("/Users/"+cid+"/Desktop/"+out_data, "w")
newfile.write(data_replaced)
newfile.close()
