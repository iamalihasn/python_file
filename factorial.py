# recursion approach

def factorial(num):

    # Base code
    if num == 0:
        return 1
    return num * factorial(num-1)

# loop approach
def factorials(num):
    fact =  1
    for i in range(1,num+1):
        fact *= i

    return fact

number = int(input("Enter a number : "))
print(f"Factorial of {number} is : {factorial(number)}")
print(f"Factorial of {number} is : {factorials(number)}")