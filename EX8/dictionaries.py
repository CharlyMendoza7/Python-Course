"""Write a program to read through the mbox-short.txt and figure out who has sent
the greatest number of mail messages. The program looks for 'From ' lines and
takes the second word of those lines as the person who sent the mail. The program
creates a Python dictionary that maps the sender's mail address to a count of the
number of times they appear in the file. After the dictionary is produced, the
program reads through the dictionary using a maximum loop to find the most prolific
committer."""

fname = input("Enter file name: ")
file = open(fname)
counts = dict()
l = list()

for line in file:
    if(line.startswith('From ')):
        line = line.split()
        words = line[1]
        l.append(words)
for word in l:
    counts[word] = counts.get(word,0)+1
            #print(counts)

bigcount = None
bigword = None

for key,value in counts.items():
    if bigcount is None or value > bigcount:
        bigword = key
        bigcount = value

print(bigword,bigcount)
