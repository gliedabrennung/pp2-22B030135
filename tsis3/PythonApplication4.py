# Dictionary of movies

movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

# [1]

def isHigher(num):
    if(movies[int(num)]['imdb'] > 5.5):
        print(True)
        return True
num = input()
isHigher(num)

# [2]

def isHigherList(list1):
    for i in range(len(movies)):
        if(movies[i]['imdb'] > 5.5):
            list1.append(movies[i]['name'])
    print(', '.join(list1))
list1 = []
isHigherList(list1)

 # [3]

def category(name, list2):
    for i in range(len(movies)):
        if(movies[i]['category'] == name):
            list2.append(movies[i]['name'])
    print(', '.join(list2))
list2 = []
name = input()
category(name, list2)

# [4]

def mean(sum):
    for i in range(len(movies)):
        sum += movies[i]['imdb']
    sum = sum / float(len(movies))
    print(sum)
sum = 0
mean(sum)

# [5]

def categoryMean(sum2, name2, amountOfmc):
    for i in range(len(movies)):
        if(movies[i]['category'] == name2):
            amountOfmc+=1
            sum2 += movies[i]['imdb']
    sum2 = sum2 / float(amountOfmc)
    print(sum2)
name2 = input()
sum2 = 0
amountOfmc = 0
categoryMean(sum2, name2, amountOfmc)
