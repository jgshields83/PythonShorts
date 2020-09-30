def ttys():
    while True:
        prompt = input('>')
        if prompt == 'all done':
            ttysp()
        print(prompt)
def ttysp():
    print("Would you like to continue talking to yourself? y/n")
    x = input('>')
    if x == 'y':
        ttys()
    elif x == 'n':
        print("Thanks for playing, have a nice day")
        quit()
    else:
        print("Thanks for playing, have a nice day")
        quit()

print ("Hello, welcome to talking to yourself:")
ttys()
