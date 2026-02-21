#take input
number = int(input("Enter number : "))

#check even or odd
if number & 1 != 0:
    print(f"{number} is an Odd number")
else:
    print(f"{number} is an Even number")
