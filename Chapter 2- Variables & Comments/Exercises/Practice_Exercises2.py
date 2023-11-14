'''Instructions for practice exercise 2.2
Write a python program that takes courses marks as input and then calculates average of all the courses. 
After calculating the average, calculate the percentage of a student using total marks. 
Assume the total of all the courses marks is 500 or take the total marks from the user as input.'''


# Get input from the user for marks in five subjects
Cybersecurity = float(input("Please enter the marks for Cybersecurity: "))
Psychology = float(input("Please enter the marks for Psychology : "))
Computing = float(input("Please enter the marks for Computing: "))
Accounting = float(input("Please enter the marks for Accounting: "))
Mathematics = float(input("Please enter the marks for Mathematics: "))
 
# Calculates the total, average, and percentage
total = Cybersecurity + Psychology + Computing + Accounting + Mathematics
average = total / 5
percentage = (total / 500) * 100    

# Prints the results
print ("\nThe Total marks is:", total, "/ 500.00")
print ("\nThe Average marks is:", average)
print ("\nThe Percentage is:", percentage, "%")
