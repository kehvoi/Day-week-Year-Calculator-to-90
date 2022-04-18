# Please note this does not include Leap Years
age = input("what's your current age?")
myage = int(age)
myageindays = myage * 365
myageinweeks = myage * 52
myageinyears = myage
ninetyindays = int(32850)
ninetyinweeks = int(4680)
ninetyinyears = int(90)
daysleft = ninetyindays - myageindays
weeksleft = ninetyinweeks - myageinweeks
yearsleft = ninetyinyears - myageinyears
print(f"You have {daysleft} days, {weeksleft} weeks and {yearsleft} years left until you are 90")