fname = input("Enter file name: ")
if len(fname) == 0:
    fname = 'romeo.txt'
fh = open(fname)
lst = list()
# Iterates through each line in filehandle
for line in fh:
    #Iterates through each word on line
    for i in line.split():
        #Checks to see if word is already in list
        if not i in lst:
            #Appends words to list
            lst.append(i)

lst.sort()
print (lst)
