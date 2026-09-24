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
    if index == 1:  # Main menu
        print("\nLists of functions:")
        print("1. Basic Equations\n"
              "2. Combinatorics\n"
              # "3. Calculus\n"
              "4. Settings\n"
              "5. Exit the calculator\n")
    elif index == 2:  # Combination menu
        print("\nLists of combinatorics functions:")
        print("1. Factorial (n!)\n"
              "2. Combination (nCr)\n"
              "3. Permutation (nPr)\n"
              "4. Help\n"
              "5. Go back to the main menu\n")
    elif index == 4:  # Settings menu
        print("Settings")
        print()


def firstFunction(equations):
    # Return the value of the user's equation
    print()
    try:
        # eval method is considered dangerous code
        # Because of user's input does not close the brackets
        # Or misinput could cause the program to fully stop
        answer = eval(equations)
        print(f"{equations} = {answer:.{decimal_precision}f}")
    except ValueError:
        print("Invalid Input. Value Error.")
    except SyntaxError:
        print("Invalid Input. Syntax Error.")
    # This function is done


def factorial(n):  # A simple recursive factorial function
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)


def nCr(n, r):
    # Initializing the variables
    high = 1
    low = 1
    down = n - r

    # Check which one is the highest
    # And change its positions
    if down > r:
        temp = r
        r = down
        down = temp
    # Calculations using for loop
    for i in range(n, r, -1):
        high = high * i
    for i in range(1, down + 1):
        low = low * i
    # Use floor division for integer data type
    answer = high // low
    # print with formatting
    print(f"{n}C{r} is equal to {answer}")


def nPr(n, r):
    if n == r:  # n - r = 0, 0! = 1
        answer = factorial(n)
        print(f"{n}P{r} is equal to {answer}")
    else:
        down = n - r
        answer = factorial(n) // factorial(down)
        print(f"{n}P{r} is equal to {answer}")


def secondFunction():
    to_choose = 0

    while to_choose != 5:
        listOfFunc(2)
        # User input to choose the method
        to_choose = int(input("Select the method to use: "))

        if to_choose == 1:  # n! - Factorial
            n = int(input("Enter the number (n): "))
            print(f"{n}! is equal to {factorial(n)}")
        elif to_choose == 2:  # nCr - Combination
            n = int(input("Please enter the number (n): "))
            r = int(input("Please enter the number (r): "))
            print()

            if n > r:  # n should be higher than r
                nCr(n, r)
            elif n == r:  # theoretically if n is equal to r it will always be 1
                print(f"{n}C{r} is equal to 1")
            else:
                print("r is higher than n. Invalid input.")
        elif to_choose == 3:  # nPr - Permutation
            n = int(input("Please enter the number (n): "))
            r = int(input("Please enter the number (r): "))
            print()

            if n > r:  # n should be higher than r
                nCr(n, r)
            else:
                print("r is higher than n. Invalid input.")
        elif to_choose == 4:  # Instructions for the user
            print("\n1. The factorial (n! = n! * (n-1))\n"
                  "Example: 5! = 5*4*3*2*1 = 120\n"
                  "2. Combination of 2 natural numbers (nCr = n!/r!*(n-r)!)\n"
                  "Example: 3C2 = 3!/2!*1! = 3\n"
                  "3. Permutation of 2 natural numbers (nPr = n!/(n-r)!)\n"
                  "Example: 7P7 = 7!/(7-7)! = 5040.\n"
                  "Keep in note that, 0! = 1, n should always be higher than r")
        if to_choose == 5:  # Going back to the main menu
            print("\nGoing back.")


def settingsFunction():
    # TODO add adjustable decimal pointer
    to_choose = 0


def exitFunction(name):
    # Function that prints goodbye statement
    print("\nGoodbye, " + name + "! Have a nice day!")


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

            if functionToUse == 1:  # Equation function
                equation = input("Please enter the equation: ")
                firstFunction(equation)
            elif functionToUse == 2:  # Combination function
                secondFunction()
            # elif functionToUse == 3: # Calculus function
            #    thirdFunction()
            elif functionToUse == 4:  # Settings function
                settingsFunction()

            if functionToUse == 5:  # User's consent to exit the program
                exitFunction(name="Chinguun")  # TODO remove string

        # Footer of the program
        print("=" * 30 + " CALCULATOR " + "=" * 30, end="\n")
    else:
        # If the user's input is not 1 then execute a goodbye statement
        exitFunction(name="Chinguun")  # TODO remove string
