largest = None
smallest = None
while True:
    uinput = input('Please input a number:')
    if uinput == "done":
        break
    try:
        fuinput = float(uinput)
    except:
        print ('invalid input')
        continue
    if largest is None:
        largest = fuinput
        smallest = fuinput
    elif fuinput > largest:
        largest = fuinput
    elif fuinput < smallest:
        smallest = fuinput
    continue

print ("Maximum is", largest)
print ("Minimum is", smallest)
