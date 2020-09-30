sum = 0
total = 0
while True:
    mage = input('Please input a number:')
    if mage == "done":
        break
    try:
        floatingmage = float(mage)
    except:
        print ('invalid input')
        continue
    sum = floatingmage + 1
    total = floatingmage + total
print ("Numbers input:", sum, "Sum of numbers input:", total, "Average of numbers input:", total/sum)
