""" 5.2 Write a program that repeatedly prompts a user for integer numbers until
the user enters 'done'. Once 'done' is entered, print out the largest and
smallest of the numbers. If the user enters anything other than a valid number
catch it with a try/except and put out an appropriate message and ignore the
number. Enter 7, 2, bob, 10, and 4 and match the output below."""

inum = 0
largest = None
smallest = None

#tot = 0.0
while True:
    inum = input ("Enter a number: ")
    if inum == 'done': #write this done string on output concol to finish process.
        break
    try:
        xinum = int(inum) #converted into integer not float
    except:
        print('Invalid input')
        continue

    if smallest is None:
        smallest = xinum
    elif xinum < smallest:
        smallest = xinum
    if largest is None:
        largest = xinum
    elif xinum > largest:
        largest =xinum

    #print(fval)
    # num = num + 1
    # tot = tot + fval

print ('Maximum is',largest)
print ('Minimum is',smallest)
