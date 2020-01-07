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
