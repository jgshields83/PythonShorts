name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
count = None
newlist = []
for line in handle: #reading doc line by line, getting rid of extra spaces
    line = line.strip()
    if not line.startswith('From '): continue #putting desired words in a list
    words = line.split()
    newlist.append(words[1])
histo = dict()
for item in newlist: #adding item and number of time it appears in list in dict
    histo[item] = histo.get(item, 0) + 1
bigcount = None
bigword = None
for word,count in histo.items(): # getting largest count and word
    if bigcount is None or count > bigcount:
        bigcount = count
        bigword = word
print(bigword, bigcount)
