capitals = {
  "Germany": "Berlin",
  "Canada": "Ottawa",
  "England": "London"
}
print(capitals)

print(capitals.values())

#Accessing a dictionary item
print(capitals["Germany"])

#Adding an item to a Dictionary
capitals["Ghana"] = "Accra"
print(capitals)

#Remove Items from a dictionary
del capitals["England"]
print(capitals)

#Change details of a dictionary
capitals["Canada"] = "Switzerland"
print(capitals)

###More on Dictionary Practice
dictionary_1 ={"students": ["Gerald","Ever"]}
print(dictionary_1)


#Iterating Through a dictionary
for key in dictionary_1:
    print("These is the key:" ,key)

for value in dictionary_1:
    values = dictionary_1.values()
    print("These is the value" ,values)

# Intergrated list
students = [{"name": "Joy", "age": 22, "classroom": "DataScience"},
            {"name": "Lilian", "age": 18, "classroom": "Software Dev"},
            {"name": "David", "age": 7, "classroom": "Aviation"}]
stud_keys = students[-2].keys()
print(stud_keys)

stud_values = students[-2].values()
print(stud_values)

for x in students[-1]:
    print(x)

for y in students:
    studentValues= students[0].values()
print(studentValues)