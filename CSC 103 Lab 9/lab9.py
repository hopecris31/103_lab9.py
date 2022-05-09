#Hope Crisafi  
#Lab 9
#5/25/2021
#Sam Sotland

#NJW 9.5/10

import csv

#Part 1a

movie1 = ['Star Wars', 'George Lucas', 1977, 'sciFi',100]
movie2 = ['alvin and the chipmunks: the squeakual','some idiot', 2009, 'crap', -24]
movie3 = ['Empire Strikes Back', 'Irvin Kershner', 1980, 'SciFi', 101]
allMovies = [movie1, movie2, movie3]

def find_movie(movieList, movieTitle):
    end = len(movieList)
    index = 0
    movieBool = False
    while index < end and not movieBool:
        if movieTitle == movieList[index][0]:
            movieBool = True    
        index += 1

    return movieBool

print(find_movie(allMovies, 'Empire Strikes Bac'))

print(find_movie(allMovies, 'Star Wars'))


# #Part 1b

def return_movies():

    movie1 = ['Star Wars', 'George Lucas', 1977, 'sciFi',100]
    movie2 = ['alvin and the chipmunks: the squeakual','some idiot', 2009, 'crap', -24]
    movie3 = ['Empire Strikes Back', 'Irvin Kershner', 1980, 'SciFi', 101]
    allMovies = [movie1, movie2, movie3]


#NJW This function SHOULDN'T have parameters and doesn't return anything (-0.5)
def movie_in_list(movieTitle, movieList):
    
    #userMovie = input('enter a movie to search for: ')
    movieFound = find_movie(allMovies, movieTitle)

    if movieFound == True:
        movieMessage = 'your movie is in the collection'
    else:
        movieMessage = 'movie not in the collection'


    return movieMessage

    #search return_movies for the title, 

print(movie_in_list('Empire Strikes Back', allMovies))

#Problem 2a

#F1
def open_csv(fileName,index):
    filename = fileName
    myFile = open(filename, 'r')
    fileList = csv.reader(myFile)

    next(fileList)

    dataList = []

    for line in fileList:
        dataList.append(line[index])

    myFile.close()

    return dataList



#print(open_csv('GOOG.csv'))


#F2

randomList = [1,2,3,4,5,6,7,8,9,10]

def list_average(list):
    count = 0
    for value in list:
        count += float(value)
    
    return (count / len(list))

#print('average is: ',(list_average(randomList)))

#F3

#NJW Use better function names
def some_function(fileName):

    valuesList = open_csv(fileName,4)
    end = len(valuesList)
    avg = list_average(valuesList)

    print('days on market: ', end)
    print('average is: ',avg)
    print('start and end price:',valuesList[0],'and', valuesList[end-1])


#some_function('BTC-USD.csv')
#some_function('GOOG.csv')

#Problem 3

#NJW But you HAVE functions to READ a CSV file and return the data. Why not
#NJW CALL that function? 

def largest_magnitude(file):
    filename = file
    myFile = open(filename, 'r')
    fileList = csv.reader(myFile)
    lineFound = [0,0,0]

    next(fileList)
    for line in fileList:
        if float(line[2]) > float(lineFound[2]):
            lineFound = line
    #print(lineFound)

    data = open_csv(file,2)
    largestMagnitude = max(data)
    findDate = largestMagnitude
    print('Magnitude: ',largestMagnitude)
    print('largest magnitude occured in: ', lineFound[9])

def california_earthquakes(file):
    filename = file
    myFile = open(filename, 'r')
    fileList = csv.reader(myFile)
    lineFound = [0,0,0]
    caliCount = 0

    next(fileList)
    for line in fileList:
        if line[9] == 'California':
            caliCount += 1
    print('California Earthquakes:', caliCount)


#location[9]


#similar loop
#loop over all lines, check column 9, every time see that value = california, add 1 to a counter (number of earthquaKES IN THat palce)

largest_magnitude('earthquakes.csv')
california_earthquakes('earthquakes.csv')

#search for max value in column [2]
#? find date column[9]
#print magnitude


#search column [2] for every value thats not the same?
