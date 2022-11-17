# This program takes the user's inputted grades and displays the lowest grade, a mdified list without the lowest grade, the average of the grades, and their letter grade
# 11/15/2022
# CTI-110 P4HW1 - Score List
# Alexander Brinson

# Ask user how many grades they want to enter
# Ask user for each of the grades
# User inputs grades
# Put the grades in the list
# Modify the list
# Calculate the average of the grades
# Calculate the letter grade
# Display the lowest grade
# Display the modified list
# Display the average of the grades
# Display their letter grade

list_grades = [ ]

numOfGrades = int(input("How many grades do you want to enter? "))
print()
for i in range(numOfGrades):
    gradeScore = float(input("Enter grade #" + str(i + 1) + ": "))
    if gradeScore > 100 or gradeScore < 0:
        print()
        print("INVALID SCORE ENTERED!!!")
        print("Score should be between 0 and 100")
        gradeScore = float(input("Enter grade #" + str(i + 1) + " again: "))
        list_grades.append(gradeScore)
    else:
        list_grades.append(gradeScore)

minGrade = min(list_grades)
list_grades.remove(minGrade)
average_grade = sum(list_grades) / len(list_grades)
letterGrade = 'Z'
if average_grade >= 90:
    letterGrade = 'A'
else:
    if average_grade >= 80:
        letterGrade = 'B'
    else:
        if average_grade >= 70:
            letterGrade = 'C'
        else:
            if average_grade >= 60:
                letterGrade = 'D'
            else:
                letterGrade = 'F'
    
print()
print('----------Results----------')
print('Lowest Score:      ', minGrade)
print('Modified List:     ', list_grades)
print('Scores Average:    ', f'{average_grade:.2f}')
print("Grade:             ", letterGrade)
print('---------------------------')
