hand = input("Please input a file:")
ohand = open(hand)
import re
summ = list()
for line in ohand:
    y = line.strip('')
    x = re.findall('[0-9]+', y)
    for item in x:
        z = float(item)
        summ.append(z)
print(sum(summ))
if len(hand) < 1 : hand = "regex_sum_42.txt"
