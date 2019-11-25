# Use words.txt as the file name
fname = input("words.txt")
# write file name in black prompit for read the code

fh = open(fname)
for i in fh :
	i = i.rstrip()
	print (i.upper())
