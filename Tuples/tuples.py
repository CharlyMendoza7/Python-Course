"""Write a program to read through the mbox-short.txt and figure out the distribution
 by hour of the day for each of the messages. You can pull the hour out from the
 'From ' line by finding the time and then splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts, sorted
 by hour as shown below."""

fname = input("Enter name: ")
if(len(fname) < 1):
    fname = "mbox-short.txt"
file = open(fname)
hourList = list()
counts = dict()

for line in file:
    if(line.startswith('From ')):
        line = line.split()
        h = line[5]
        hour = h.split(":")
        hourList.append(hour[0])

for h in hourList:
    counts[h] = counts.get(h,0)+1
hSorted = sorted(((k,v) for k,v in counts.items()))
for k,v in hSorted:
    print(k,v)
