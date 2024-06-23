"""
Working with Lists, Tuples, and Dictionaries
"""
##Exercise 1: Lists

#defining a list
myFruitList = ["apple", "banana", "cherry"]
print(myFruitList)
print(type(myFruitList))

#Accessing a list by position
print(myFruitList[0])
print(myFruitList[1])
print(myFruitList[2])

#changing the values in the list
myFruitList[2]="orange"
print(myFruitList)

#Exercise 2: Tuples - tuple is just like a list, but it is immutable and uses paranthesis() instead of square brackets[]
myFinalAnswerTuple = ("apple", "banana", "pineapple")
print(myFinalAnswerTuple)
print(type(myFinalAnswerTuple))

#accessing a tuple by position
print(myFinalAnswerTuple[0])
print(myFinalAnswerTuple[1])
print(myFinalAnswerTuple[2])


#Exercise 3: Dictionary
myFavoriteFruitDictionary = {
    "Akua":"Apple",
    "Saanvi": "banana",
    "Paulo" : "pineapple"
}
print(myFavoriteFruitDictionary)
print(type(myFavoriteFruitDictionary))

#accessing a dictionary by name
print(myFavoriteFruitDictionary["Akua"])
print(myFavoriteFruitDictionary["Saanvi"])
print(myFavoriteFruitDictionary["Paulo"])




