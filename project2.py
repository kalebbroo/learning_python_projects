# Multiplication Table Generator #

while True:
    print("Welcome to the multiplication table generator!")
    print("")
    print("Enter an intiger between 1 and 10 to display the table.")


    while True:
        try:
            num = int(input("Enter a number between 1 and 10: "))

            if num < 1 or num > 10:
                raise ValueError("Invalid input: Please enter a number between 1 and 10.")
            break
        except ValueError as error:
            print(error)

    for i in range(1, 11):
        product = num * i
        print(num, "x", i, "=", product)

    response = input("Generate another multiplication table? (yes/no): ")
    if response.lower() != "yes":
        break
            
