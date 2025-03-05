# store multiple items
ages = [16,28,79]
print(ages)

#List containing different things (strings,numbers and other lists)
student_Details =["Joy" , 25 , "Dekut" , [34,67,67]]
print(student_Details)

#Accessing an item in a list
print("Age at index 1 is:",ages[1])

#Add elements to a python List
ages.append(90)
print(ages)

#Add element at a specified index
ages.insert(2, 84)
print(ages)

# names = ["Githaiga", "Francis", "Abdi", "Jane"]
# nums = [0, 1, 2, 3, 4]
# char = ['a', 'b', 'c', 'd','e' ]

# for num in nums:
#     print(num)
#     # print(names[num])

names = ["Githaiga", "Francis", "Abdi", "Jane", "John", "Tim"]
for index , name in enumerate(names):
    print("index", index, "Name",name)

##Nested for loop 
for i in range(0,10):
    for j in range(0,i):
        print(i, j)