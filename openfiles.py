file = input("Please enter file name:")
try:
    ofile = open(file)
except:
    print("*", file, "*", "is not a recognized file")
    quit()
count = 0
inp = ofile.read()
print(inp.upper())
