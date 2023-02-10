print("3ada4a 1")
def grams_to_ounces(gram):
    ounce = 28.3495231 * float(gram)
    print(ounce)
gram = input()
grams_to_ounces(gram)

#####################################

print("3ada4a 2")
def fahreinheit_to_celsius(far):
    celsius = (5/9)*(float(far) - 32)
    print(celsius)
far = input()
fahreinheit_to_celsius(far)

####################################

print("3ada4a 3")
def solve(numheads, numlegs):
    for chickens in range(int(numheads) + 1):
        rabbits = int(numheads) - chickens 
        if (2 * chickens + 4 * rabbits == int(numlegs)):
            print("Chickens:", chickens, "Rabbits:", rabbits)
numheads = input()
numlegs = input()
solve(numheads, numlegs)

####################################

print("3ada4a 4")
def filter_prime(num):
    for i in range(2,int(int(num) ** 0.5) + 1):
        if (int(num) % i == 0):
            return False
    return True
listok = []
for j in range(0, 5):
    a = 0;
    a = input()
    if(filter_prime(a) == True):
        listok.append(a)
print(listok)

####################################

print("3ada4a 5")
#      x3 KaK 3To HaIIucaTb

####################################

print("3ada4a 6")
def stringReverser(string):
    x = string.split(" ")
    x.reverse()
    print(' '.join(x))
string = input()
stringReverser(string)

####################################

print("3ada4a 7")
def has_33(num1, num2):
    n = 0
    if (num1 == '3' and num2 == '3'):
        print(True)
myArray = []
for i in range(0, 5):
    y = input()
    myArray.append(y)
for i in range(0, 5):
    has_33(myArray[i -1], myArray[i])

####################################

print("3ada4a 8")
def has_007(num1, num2, num3):
    n = 0
    if (num1 == '0' and num2 == '0' and num3 == '7'):
        print(True)
myArray = []
for i in range(0, 5):
    y = input()
    myArray.append(y)
for i in range(0, 5):
    has_007(myArray[i - 2], myArray[i - 1], myArray[i])

####################################

print("3ada4a 9")
def volume(radius):
    pi = 3.14
    v = (4/3)*(float(pi))*(float(radius) ** 3)
    print(v)
radius = input()
volume(radius)

####################################

print("3ada4a 10")
def unique(myList, anotherList):
    x = len(myList)
    for i in range(x):
        if myList[int(i)] not in anotherList:
            anotherList.append(myList[int(i)])
    print(anotherList)
myList = []
anotherList = []
for i in range(10):
    m = input()
    myList.append(m)
unique(myList, anotherList)


####################################

print("3ada4a 11")
def palindrome(string):
    string_copy = []
    for i in range(0, len(string)):
        string_copy.append(string[len(string) - i - 1])
    string_copy = "".join(string_copy)
    if string_copy == string:
        print(True)
    else:
        print(False)
string = input()
palindrome(string)

###################################

print("3ada4a 12")
def histogram(lengthList):
    for i in range(len(lengthList)):
        print("*" * int(lengthList[i]))
lengthList = []
for i in range(5):
    c = input()
    lengthList.append(c)
histogram(lengthList)

###################################

print("3ada4a 13")
import random
def isTrueNumber(guess, w, myName, numOfGuess):
    numOfGuess = numOfGuess + 1
    if (int(guess) == int(w)):
        text2 = "Good job, {}! You guessed my number in {} guesses!"
        print(text2.format(myName, numOfGuess - 1))
    else:
        print("Your guess is too low.")
        guess = input("Take a guess. ")
        return isTrueNumber(guess, w, myName, numOfGuess)
        
myName = input("Hello! What is your name? ")
text1 = "Well, {}, I am thinking of a number between 1 and 20."
print(text1.format(myName))
w = random.randint(1, 20)
guess = input("Take a guess. ")
numOfGuess = 1;
isTrueNumber(guess, w, myName, numOfGuess)
