#! usr/bin/env python3

base = [1,2,3,4,5]
exponent = [5,4,3,2,1]

def power(x, y):
    return(x**y)

# The mapping function gives an iterable, not a list
result = list(map(power, base, exponent))
print(result)

#Now for something completely different: mapping with lambda function
resultLambda = list(map(lambda x,y: x**y, base, exponent))
print(resultLambda)

#use multiple functions on pi
from math import sin, cos, tan, pi

def func_lister(x, functions):
    results = []
    for func in functions:
        results.append(func(x))
    return results

functions = (sin, cos, tan)

resultFuncList = func_lister(pi, functions)
print(resultFuncList)

# Do the same with list comprehension, which is really cool
def func_list_comprehend(x, functions):
    resultsListComprehend = [func(x) for func in functions]
    print(resultsListComprehend)

func_list_comprehend(pi, functions)

# Filter out odd numbers
fibonacci = [0,1,1,2,3,5,8,13,21,34,55]
oddNumbers = list(filter(lambda x: x % 2 == 1, fibonacci))
print(oddNumbers)
# Filter out even numbers
evenNumbers = list(filter(lambda x: x % 2 == 0, fibonacci))
print(evenNumbers)

# Now do the same filtering with a mapping, just for funsies
# Odd numbers
mapNumbersOdd = map(lambda x: x % 2 == 1, fibonacci)
mappedOdd = []

for num, val in zip(fibonacci, mapNumbersOdd):
    if val == True:
        mappedOdd.append(num)
print(mappedOdd)

#Even numbers
mapNumbersEven = map(lambda x: x % 2 == 0, fibonacci)
mappedEven = []

for num, val in zip(fibonacci, mapNumbersEven):
    if val == True:
        mappedEven.append(num)
print(mappedEven)

# Lets do something more complicated
# add shipping cost to all orders less than 100EUR
import csv

# Iterate through the sublist, multiply the quantity with the price of each ordered book
def getPrice(orderList):
    quantity = float(orderList[3])
    priceEach = float(orderList[4])
    priceOrder = quantity * priceEach
    if priceOrder < 100:
        priceFinal = priceOrder + 10
    else:
        priceFinal = priceOrder
    print(priceFinal)

#Open a csv file, read the lines from the second row
filePath = "/home/zsuzsi/study/chatbot/scriptlets/books.csv"
with open(filePath) as books:
    orders = csv.reader(books)
    next(orders)
    data = [r for r in orders]

# Finally, use the handy map function to iterate through all the sublists
dataMapped = list(map(getPrice, data))
print(dataMapped)

