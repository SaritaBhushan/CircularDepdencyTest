'''
Problem Statement

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000. (Answer: 233168) (solution code attached: problem_1_solution_code.py)
'''
# print("Enter Number: ")
# n=input()
n=1000

# Find list all the natural numbers below n that are multiples of 3 or 5
l=[x for x in range(1, n) if x%3 ==0 or x%5 ==0]
sum=0
for ele in l:
    sum +=ele

print("Sum is ",sum)