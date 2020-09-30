fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    romeo = line.split()
    romeo.sort()
    #need to figure out how to check if word is in the list already
    for word in romeo:
        if word in lst:
            continue
        else:
            lst.append(word)
lst.sort()
print(lst)
