import datetime
x = datetime.datetime.now()
print(str(x.year) + "/" + str(x.month) + "/" + str(x.day - 5) + "/" + str(x.second) + "." + str(x.microsecond))
print(x.day - 1, x.day, x.day + 1)
print(x.microsecond)

z = []
for i in range (0, 4):
    if i % 2 == 0:
        y = input(("enter the day - "))
        z.append(y)
    else:
        y = input(("enter the month - "))
        z.append(y)
print(((int(z[3]) - int(z[1])) * 30 * 86400) + (int(z[2]) - int(z[0])) * 86400, "seconds")


