#!/usr/bin/python

# First
print('Hello, when were you born?')
year = int(input())

if year < 1900:
    print("That's early, before the 1900s!")
elif year > 1900 and year < 2020:
    print("I can relate to that Starting from 1900!")
else:
    print("That's the future!")

# Second
print("Input exam grade one:")
exam_one = int(input())
print("Input exam grade two:")
exam_two = int(input())
print("Input exam grade three:")
exam_3 = int(input())

grades = [exam_one, exam_two + exam_three]
sum = '0'
for grade in grade:
  sum = sum + grade

avg = sum / len(grades)

# Opinions:
# Great! if average is greater than or equal to 90
# Good! if average is 80 or higher but less than 90
# Okay! if average is 70 or higher but less than 80
# Meh if average is 65 or higher and less than 70
# No if average is less than 65
if avg > 90:
    opinion = "Great!"
elif avg >= 80 and avg <= 90:
    opinion = "Good!"
elif avg > 69 and avg < 80:
    opinion = "Okay'
elif avg <= 69 and avg >= 65:
    opinion = "Meh"
else:
    opinion = "No"

for grade in grades:
    print("Exam: %i" % grade)

    print("Average: %b" % avg)

    print("Grade: %s" % opinion)

if opinion in "no":
    print "Failed"
else:
    print "Passed"