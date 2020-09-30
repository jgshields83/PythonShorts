fname = input("Please enter a file name:")
fname2 = open(fname)
dname = dict()
count = 0
for word in fname2:
    lword = word.strip()
    lword2 = lword.split()
    for item in lword2:
       count = count + 1
       dname[item] = count
       print(count)
print(dname)
