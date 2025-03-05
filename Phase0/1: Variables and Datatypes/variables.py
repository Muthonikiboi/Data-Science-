# A variable is a container to hold data

numbers = 10
print(numbers)

# Sometimes you can declare a variable without assigning any data
address = None
print(address)

# Reassigning Variables
address =11098
print(address)

#Strings ,boolean , float
First_Name = "Joy"
IsRaining = True
My_Age = 29
pI = 3.147
print(
type(IsRaining),
type(My_Age),
type(pI))

#Upper Case

name = "Joy Kiboi".upper()
print(name)

# LAB 1
 #Below, we have a sentence whose cases are all over the place. Let's normalize the cases and make everything lower case except the first letter in the sentence. hint: there is a string method that does this
sentence = "woW WE LOVE cOdInG and strINGS!"
sentence = sentence.capitalize()
print(sentence)

# 2. Next, we have our Flatiron mantra, but it's not in title case like it should be! Let's fix that and use another string method that makes all strings first letter capitalized.
flatiron_mantra = "learn. love. code."
flatiron_mantra = flatiron_mantra.title()
print(flatiron_mantra)

# 3. The next thing we want to do is practice turning other data types into strings. Below, we have a number 1234, which happens to be our street number in our address, which is a string. So, let's turn the number into a string so we can eventually add it to our address. The process of linking different strings together is called concatenation.
num_to_string = str(1234)
print(num_to_string)

#4. Let's take the num_to_string and add it to the beginning of our street address below. We need to concatenate the variable to the beginning of our string so that we have our full address all in one string and assigned to the variable full_address. hint: None is a placeholder in the below code for you to edit
full_address = num_to_string + " Abc street, Hometown USA"
print(full_address)

# 5. Finally, let's replace some of the characters in a string. Let's say Bart is upset with his family and wants to be adopted by the Flanders family. How would you replace his last name?
# Hint: We did not directly cover this method in the lesson. Check out the string helper docstring for a list of available methods.
name = "Bart Simpson"
name = name.replace("Simpson", "Flanders")
print(name)

##Lab 2
