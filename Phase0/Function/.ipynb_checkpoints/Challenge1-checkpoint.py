# Create a program that takes students subjects,
# calculates their average score ,grades the score and gives a comment.
# Prints out the name, average scrore and comment.
# Prompts the user to parse the name, subjects.
# Use Functions Conditional Statements(if else) and input().
# Use a for loop

def std_grading(name, python,AI ,ML ):
    average_Score = (python + AI + ML)/3
    if average_Score >= 70:
        print("Student Name", name,"Average", average_Score , "\n" 
              , "Grade: A", "\n"
              , "Excellent")
    elif  60 <= average_Score < 70:
        print("Average", average_Score , "\n" 
              , "Grade: B", "\n"
              , "Perfect")
    elif  50 <= average_Score < 60:
        print("Average", average_Score , "\n" 
              , "Grade: C", "\n"
              , "Good")
    elif  40 <= average_Score < 50:
        print("Average", average_Score , "\n" 
              , "Grade: D", "\n"
              , "Fair")
    else:
        print("Average", average_Score , "\n" 
              , "Grade: E", "\n"
              , "Poor")
name = input("Enter Your Name:")
python = float(input("Enter Your Python Score:"))
AI = float(input("Enter Your AI Score:"))
ML = float(input("Enter Your ML Score:"))

std_grading(name, python,AI ,ML )