score = input('Please enter a value between 0.0 and 1.0:') #calculates letter grade from percentage
try: #checking if it's an integer
    x = float(score)
except:
    print('Error: a non numerical value was entered.')
    quit()
if x < 0 or x > 1: # checking if it's within range
    print('Error: value not within range')
    quit()
if x >= 0.9: # calculating grade
    print('A')
elif x >= 0.8:
    print('B')
elif x >= 0.7:
    print('C')
elif x >= 0.6:
    print('D')
elif x < 0.6:
    print('F')
