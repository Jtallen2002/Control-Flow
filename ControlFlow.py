"""
Programmer: Jake Allen
Date: 1-6-20
Program: Running Total

This program asks users for five numbers. It then sums up the given numbers
"""
sum = 0
for i in range(5):
    sum=int(input("Please enter a number: "))+sum
print("\nThe sum of those numbers is: "+str(sum))
