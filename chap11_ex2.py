'''Exercise 2: Write a program to look for lines of the form:

New Revision: 39772

Extract the number from each of the lines using a regular expression and 
the findall() method. Compute the average of the numbers and print out the
 average as an integer.
Enter file:mbox.txt
38549

Enter file:mbox-short.txt
39756'''

lst = list()
count = 0
import re
file_name = input('Enter the name of the file that you would like to work with: ')
try:
    fhand = open(file_name)

except FileNotFoundError:
    print('The file could not be opened. Please try again!')
    exit()

for line in fhand:
    words = line.rstrip()
    #Extract the number from each of the lines using a regular expression and the findall() method
    x = re.findall('^New Revision: ([0-9]+)', words)
    if len(x) > 0:                          #tracting only strings
        for val in x:
            val = int(val)                  #converting strings into intergers
            lst.append(val)                 #adding the intergers to the list


# print(lst)
average = sum(lst)/len(lst)
print('The average is:', average)                    #calculating the average
