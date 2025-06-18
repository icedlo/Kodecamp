# #list
# #is basically an ordered mutable collection of items

# age=[10, 13, 45,50]
# print(age[0])

# #changing items  in a list

# age[1]=200
# print(age)

# #len()

# item_count=len(age)
# print(item_count)

# print(len(age))

# #Copy method
# new_ages=age.copy()
# new_ages.append("hello")
# print (new_ages)

# for ahe in age:
#     print(ahe)

#TUPPLES
#its basically an ordered immutable collection of items, enclosed in a parantheses
#we cannot modify or delete items in a tupple

# gender= ("male", "female", "female", "male")
# print(gender[1])

# print (gender.count("male"))


#DICTIONARY
#its just an unordered collection of key value pair
#keys are unique and immutable...keys cannot be changed..... values are mutable amd can be of any type

age={"student1":13, "student2":16,"student3":14}
print(len(age))

#Accessing an item

print(age["student1"])

#changing a value in a dict

age["student2"]=30

print(age["student2"])

#Adding a value
age["student4"]=100
print(age)



