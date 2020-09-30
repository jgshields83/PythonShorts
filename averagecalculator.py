items = list()
while True:
    inp = input('Please enter a number:')
    if inp == 'done' : break
    finp = float(inp)
    items.append(finp)
print(sum(items) / len(items))
