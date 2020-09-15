# Write a method to compute the `factorial` of a number.
# Given a whole number n, a factorial is the product of all
# whole numbers from 1 to n.
# 5! = 5 * 4 * 3 * 2 * 1
#
# Example method call
#
# factorial(5)
#
# > 120

def factorial(num):
    result = 1
    for i in range(1, int(num)+1):
        result = result * i
    print(result)

factorial(5)