"""
Programmer: Jake Allen
Date: 1-6-20
Program: Running Total, Part II

This program asks users for five numbers. It then sums up the given numbers
"""
sum = 0
howManyNumbers=int(input("How many numbers would you like to sum up: "))
for i in range(howManyNumbers):
    sum=int(input("Please enter a number: "))+sum
print("\nThe sum of those numbers is: "+str(sum))

"""
Programmer: Jake Allen
Date: 1-8-20
Program: Running Total, Part II

This program asks users for how many tests they want to average, and then it takes their inputs for the test grades and then it spits out the average.
"""

average = 0
howManyTests = int(input("How many tests would you like to average: "))
for i in range(howManyTests):
    average=int(input("Please enter the grade for test "+str(i+1)+": "))+average
print("The average of those tests is "+str(float(average/howManyTests))+"%")
