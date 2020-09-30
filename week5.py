hours = input('Please Enter Hours Worked:')
rate = input('Please Enter Current Rate:')
fhour = float(hours)
frate = float(rate)
if fhour <= 40:
    pay = fhour * frate
else:
    pay = (40 * frate) + ((fhour - 40) * (frate * 1.5))
print(pay)
