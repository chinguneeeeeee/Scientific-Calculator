# Chinguun Tuguldur
# Description: Scientific calculator
# Sources: None
# GitHub Link: https://github.com/chinguneeeeeee/Scientific-Calculator/
__author__ = "Chinguun"
# TODO add content to the 2nd and settings function
# TODO FINAL Project is to implement calculus (d/dx, integration ∫).

# Default the decimal precision to 2 and subject to change from user
decimal_precision = 2

def listOfFunc(index):
    # Print the lists of function that the user want to use
    if index == 1:
        print("\nLists of functions:")
        print("1. Basic Equations\n"
              "2. Combinatorics\n"
              # "3. Calculus\n"
              "4. Settings\n"
              "5. Exit the calculator\n")
    elif index == 2:
        print("\nLists of combinatorics functions:")
        print("1. n!\n"
              "2. C (n, r)\n"
              "3. P (n, r)\n"
              "4. HCF (Highest Common Factor)\n"
              "5. LCD (Lowest Common Denominator)\n"
              "6. Help\n"
              "7. Go back to the main menu\n")
    elif index == 4:
        print("Settings")
        print()


def firstFunction(equations):
    # Return the value of the user's equation
    answer = eval(equations)
    print()
    try:
        # eval method is considered dangerous code
        # Because of user's input does not close the brackets
        # Or misinput could cause the program to fully stop
        print(f"{equations} = {answer:.{decimal_precision}f}")
    except ValueError:
        print("Invalid Input. Value Error.")
    except SyntaxError:
        print("Invalid Input. Syntax Error.")
    # This function is done


def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)


def nCr(n, r):
    down = n - r
    high = 1
    low = 1

    if down > r:
        temp = r
        r = down
        down = temp

    for i in range(n, r, -1):
        high = high * i
    for i in range(1, down + 1):
        low = low * i

    answer = high // low

    print(f"{n}C{r} is equal to {answer}")


def secondFunction():
    to_choose = 0

    while to_choose != 7:
        listOfFunc(2)
        to_choose = int(input("Select the method to use: "))

        if to_choose == 7:
            print("Going back.")

        if to_choose == 1:
            n = int(input("Enter the number (n): "))
            print(f"{n}! is equal to {factorial(n)}")
        elif to_choose == 2:
            n = int(input("Please enter the number (n): "))
            r = int(input("Please enter the number (r): "))
            if n < r:
                nCr(n, r)
            elif n == r:
                print(f"{n}C{r} is equal to 1")
            else:
                print("n is higher than r. Invalid.")

def settingsFunction():
    print("Work In Progress\n")


def exitFunction(name):
    print("Goodbye, " + name + "! Have a nice day!")

if __name__ == "__main__":
    # Asking the user's name for the introductory part
    # name = input("Enter your name: ") TODO remove #

    # Introduction
    # print("Hello ", name, ", this is a scientific calculator.", sep='') TODO remove #
    conditionToUse = int(input(
        "Press 1 if you want to use the calculator: "
    ))  # Ask the user's consent to use the calculator
    print()

    if conditionToUse == 1:
        # Header of the program
        print("=" * 30 + " CALCULATOR " + "=" * 30)

        # Initialize the variable
        functionToUse = 0

        # While loop to check if the value is between 1 and 5
        while functionToUse != 5:
            listOfFunc(1)  # Loop lists until exit

            # User input whether to choose which function to use
            functionToUse = int(input("Enter your choice: "))

            if functionToUse == 1:  # The first function of the program
                equation = input("Please enter the equation: ")
                firstFunction(equation)
            elif functionToUse == 2:
                secondFunction()
            # elif functionToUse == 3:
            #    thirdFunction()
            elif functionToUse == 4:
                settingsFunction()

            if functionToUse == 5:  # User's consent to exit the program
                exitFunction(name="Chinguun")  # TODO remove string

        # Footer of the program
        print("=" * 30 + " CALCULATOR " + "=" * 30, end="\n")
    else:
        # If the user's input is not 1 then execute a goodbye statement
        exitFunction(name="Chinguun")  # TODO remove string