#Exercise 1
myString = "This is my string."
print(myString)
print(type(myString))
print(myString + " is of the data type " + str(type(myString)))

#Exercise 2: String Concatenation
firstString = "water"
secondString = "fall"
thirdString = firstString + secondString
print(thirdString)

#Exercise3: Working with input strings
name = input("What is your name? ")
print(name)

#Exercise 4: Formatting output strings
color= input("What is your favorite color? ")
animal= input("What is your favorite animal? ")
print("{}, you like a {} {}!".format(name, color, animal))
