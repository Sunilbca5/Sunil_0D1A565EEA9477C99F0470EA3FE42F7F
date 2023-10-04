#Implement a recursive function to calculate the factorial of a given number

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

num = int(input("Enter a number: "))
result = factorial(num)
print("The factorial of {} ! is {} ".format (num,result))