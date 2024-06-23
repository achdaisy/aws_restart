"""
Creating a list with different types and print the values.
"""
myMixedTypeList = [45, 290578, 1.02, True, "My dog is on the bed", "45"]

#using a for loop to traverse teh list and print the values
for item in myMixedTypeList:
    print("{} item is of type {}".format(item, type(item)))
