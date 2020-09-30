name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
count = 0
dictp = {}
for line in handle:
    if line.startswith("From "):
        count = count + 1
        email = line.split()
        time = email[5]
        hour = time.split(':')[0]
        dictp[hour] = dictp.get(hour, 0) + 1
listhour = dictp.items()
list2 = list()
for key, val in dictp.items():
	   list2.append( (key, val) )
	   list2.sort()
for key, val in list2:
    print(key, val)
