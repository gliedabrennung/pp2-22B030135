def multiplier(list):
    mul = 1;
    for i in list:
         mul *= i
    print(mul)
list = [1, 2, 3, 4, 5, 6, 7, 8]
multiplier(list)

def stringer(string):
    upp = low = 0
    for j in string:
        if(j >= 'A' and j <= 'Z'):
            upp += 1
        elif(j >= 'a' and j <= 'z'):
            low += 1
    print(upp, low)
string = "Here Is Six Upper Case Letters"
stringer(string)

def palindromer(string):
    if string == string[::-1]:
        print("True")
    else:
        print("False")
string1 = "pp2pp"
string2 = "CoCucKa_B_TecTe"
palindromer(string1)
palindromer(string2)

from time import sleep
def mili(num, time):
    sleep(time * pow(10, -3))
    print(pow(num, 0.5))
num = float(input())
time = float(input())
mili(num, time)

def tupler(tuple):
    for k in tuple:
        if k is False:
            return False
        else:
            return True
tuple = (True, True, True, True)
print(tupler(tuple))

