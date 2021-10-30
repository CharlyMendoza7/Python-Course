text = "X-DSPAM-Confidence:    0.8475"
where = text.find("0.8475")
length = len(text)
ntext = text[where:length+1]
print(ntext)
