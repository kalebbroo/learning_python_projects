"""
Project 3: Data Structures

In this project, you will write a program that prompts the user to enter a list of numbers, and then uses a loop to calculate and display the sum, product, minimum, and maximum of those numbers. You will then use a set to determine the unique numbers in the list, and a dictionary to count the number of occurrences of each number in the list.

Here are the requirements for the project:

1. Your program should prompt the user to enter a list of numbers, with each number separated by a space.

2. Your program should use a loop to calculate and display the sum, product, minimum, and maximum of the numbers in the list.

3. Your program should use a set to determine the unique numbers in the list, and print them in ascending order.

4. Your program should use a dictionary to count the number of occurrences of each number in the list, and print the results in ascending order by key.

5. Your program should use appropriate data structures to store and manipulate the data.

6. Your program should handle any errors gracefully and display informative error messages to the user.
"""

# Data Structures #


# 1. Prompt the user to enter a list of numbers, with each number separated by a space.
print("Welcome to the Data Structures program!")
print("please enter a list of numbers, with each number separated by a space.")
print("")
print("Example: 1 2 3 4 5 6 7 8 9 10")
print("")

# 4. Use a dictionary to count the number of occurrences of each number in the list, and print the results in ascending order by key.
def get_count(numbers):
    try:
        count = {}
        for x in numbers:
            if x in count:
                count[x] += 1
            else:
                count[x] = 1
        print("The number of occurrences of each number in the list is:", count)
    except TypeError as error:
        print(error)
        print("Something went wrong calculating the number of occurrences of each number in the list.")


# 3. Use a set to determine the unique numbers in the list, and print them in ascending order.
def get_unique(numbers):
    try:
        unique = set(numbers)
        unique = sorted(unique)
        print("The unique numbers in the list are:", unique)
    except TypeError as error:
        print(error)
        print("Something went wrong calculating the unique numbers in the list.")


def get_max(numbers):
    try:
        maximum = max(numbers)
        print("The maximum number in the list is:", maximum)
    except TypeError as error:
        print(error)
        print("Something went wrong calculating the mix number in the list.")
    get_unique(numbers)


def get_min(numbers):
    try:
        minimum = min(numbers)
        print("The minimum number in the list is:", minimum)
    except TypeError as error:
        print(error)
        print("Something went wrong calculating the minimum number in the list.")
    get_max(numbers)



def get_product(numbers):
    product = 1
    for x in numbers:
        product *= x
        print("The product of the numbers in the list is:", product)
    get_min(numbers)


def get_sum(numbers):
    try:
        total = sum(numbers)
        print("The sum of the numbers in the list is:", total)
    except TypeError as error:
        print(error)
        print("Something went wrong calculating the sum of the numbers in the list.")
    get_product(numbers)


# 2. Use a loop to calculate and display the sum, product, minimum, and maximum of the numbers in the list.
def get_numbers():
    while True:
        try:
            numbers = input("Enter a list of numbers: ")
            numbers = numbers.split()
            numbers = [int(i) for i in numbers]
            get_sum(numbers)
        except ValueError as error:
            print(error)
            print("Please enter a list of numbers, with each number separated by a space.")

get_numbers()