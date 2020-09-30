file = input("Please enter a file name:")
try:
    ofile = open(file)
except:
    print("*", file, "*", "is not a recognized file name.")
    quit()
count = 0
total = 0
for line in ofile:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    count = count + 1
    end = line.find(":")
    length = len(line)
    num = line[end + 1:length]
    fnum = float(num)
    total = total + fnum

print("Average Spam Confidence:", total / count)
