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
fhand = open('mbox-short.txt')

for line in fhand:
    words = line.rstrip()
    x = re.findall('^New Revision: ([0-9]+)', words)
    if len(x) > 0:
        #lst = lst + x
        lst.append(x)

print(lst)
#“print(sum(nums)/len(nums))'''
