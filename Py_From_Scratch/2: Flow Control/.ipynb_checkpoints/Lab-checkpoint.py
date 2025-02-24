#Let's use our knowledge of variables and conditionals to assign values based on different conditions. Follow the instructions below to properly assign the values.

#With the given code in the cell below, use what you know about numbers and conditionals to assign a value to my_number and follow the directions given in the comments below. Use this as a guide to structuring the rest of the problems in this lab.

number_50 = 50
my_number = None
if number_50 > 100:
    # if number_50 is greater than 100, assign the `my_number` variable to the number 100
    my_number = 100
elif number_50 > 50:
    # if number_50 is greater than 50, assign the `my_number` variable to the number 50
     my_number = 50
else:
    # else assign the `my_number` variable to 0
     my_number = 0

print(my_number)

#Below, use conditionals to tell whether it is hot outside or not. If it is hot, assign the string "It is so hot out!" to the variable is_it_hot. If it is not hot, assign the string "This is nothing! Bring on the heat.". For our purposes, anything over 80 degrees is considered hot.
temperature = 85
is_it_hot = None
temp=0
# conditionals go here
if temp >80:
  is_it_hot = "It is so hot out!"

else:
  is_it_hot = "This is nothing! Bring on the heat."

print(is_it_hot)

#Next, let's see what day of the week it is. There are 7 days in the week starting with Sunday at day 1 and ending with Saturday at day 7. Use conditional statements to assign the day of the week to the variable day_of_the_week based on the number below assigned to the variable today_is. For example, if the day is 2, we would assign day_of_the_week the value "Monday".
today_is = 4
day_of_the_week = None
# conditionals go here
if today_is == 1:
  day_of_the_week = "Sunday"
elif today_is == 2:
  day_of_the_week = "Monday"
elif today_is == 3:
  day_of_the_week = "Tuesday"
elif today_is == 4:
  day_of_the_week = "Wednesday"
elif today_is == 5:
  day_of_the_week = "Thurday"
elif today_is == 6:
  day_of_the_week = "Friday"
elif today_is == 7:
  day_of_the_week = "Saturday"

print(day_of_the_week)

#Finally, let's take a string and see if it ends with a certain substring. If it does, assign the variable ends_with to True, and if it does not, assign it to False. For example, if have the string "School" and we want to know if it ends with the sub-string "cool". In this case it does not, so, we would assign False to the variable ends_with.
string = "Python"
sub_string = "on"
ends_with = None
# conditionals go here
if string.endswith(sub_string):
  ends_with = True
else:
  ends_with = False

print(ends_with)