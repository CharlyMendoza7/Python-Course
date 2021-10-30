"""7.2 Write a program that prompts for a file name, then opens that file
and reads through the file, looking for lines of the form:
X-DSPAM-Confidence:    0.8475
Count these lines and extract the floating point values from each of the
lines and compute the average of those values and produce an output as
shown below. Do not use the sum() function or a variable named sum in your solution."""

fname = input("Enter the file name: ")
file = open(fname)
count = 0
thesum = 0
for line in file:
    if line.startswith("X-DSPAM-Confidence:"):
        count += 1
        start = line.find(":")
        nstring = line[start+1:]
        sstring = nstring.lstrip()
        number = float(sstring)
        thesum = thesum + number
        avg = thesum/count

print("Average spam confidence: ",avg)
print("count = ",count)
