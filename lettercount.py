def countletter():
    word = input("Please enter a word: ")
    fix = input("Select a letter you would like to count: ")
    count = 0
    for letter in word:
        if letter == fix:
            count = count + 1
    print(count)

countletter()

