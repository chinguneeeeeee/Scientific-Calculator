#Chinguun Tuguldur
#Description: Scientific calculator
#Sources: None
#GitHub Link: https://github.com/chinguneeeeeee/Scientific-Calculator/

def listOfFunc():
    # Print the lists of function that the user want to use
    print("Lists of functions:")
    print("1. Basic Equations\n"
          "2. Combinatorics\n"
          "3. Calculus\n"
          "4. Settings\n"
          "5. Exit the calculator\n")

def firstFunction(equations):
    # Return the value of the user's equation
    print()
    print(equations, "=", eval(equations))
    print()


def secondFunction():
    return None

def thirdFunction():
    return None

def settingsFunction():
    return None

def exitFunction():
    print() # New line
    print("Goodbye! Have a nice day!")
    print()

if __name__ == "__main__":
    # Asking the user's name for the introductory part
    #name = input("Enter your name: ")

    # Introduction
    #print("Hello ", name, ", this is a scientific calculator.", sep='')
    conditionToUse = int(input(
        "Press 1 if you want to use the calculator: "
    )) # Ask the user's consent to use the calculator

    if conditionToUse == 1:
        # Header of the program
        print("=" * 30 + " CALCULATOR " + "=" * 30, "\n")

        # Initialize the variable
        functionToUse = 0

        # While loop to check if the value is between 1 and 5
        while functionToUse != 5:
            if functionToUse == 1:  # The first function of the program
                equation = input("Please enter the equation: ")
                firstFunction(equation)
            elif functionToUse == 2:
                secondFunction()
            elif functionToUse == 3:
                thirdFunction()
            elif functionToUse == 4:
                settingsFunction()

            listOfFunc() # Loop lists until exit

            # User input whether to choose which function to use
            functionToUse = int(input("Enter your choice: "))

            if 1 <= functionToUse <= 3:
                print()
            elif functionToUse == 5: # User's consent to exit the program
                exitFunction()
            else:
                # If the value is not between 1 and 5. Repeat.
                print("Wrong input! Try again!\n")

        # Footer of the program
        print("=" * 30 + " CALCULATOR " + "=" * 30, end="\n")
    else:
        # If the user's input is not 1 then execute a goodbye statement
        exitFunction()