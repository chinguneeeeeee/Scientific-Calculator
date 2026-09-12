#Chinguun Tuguldur
#Description: Scientific calculator
#Sources: None


# Asking the user's name for the introductory part
#name = input("Enter your name: ")

#print("Hello ", name, ", this is a scientific calculator.", sep='') # Introduction
conditionToUse = int(input("Press 1 if you want to use the calculator: ")) # Ask the user's consent to use the calculator
print() # New line

if conditionToUse == 1:
    print("=" * 30 + " CALCULATOR " + "=" * 30, end="\n")  # Header of the program

    # Print the lists of function that the user want to use
    print("Lists of functions:")
    print("1. Basic Calculation\n2. Combinatorics\n3. Calculus\n4. Others\n5. Exit the calculator\n")

    functionToUse = 0 # Set value to 0 to make the while loop work
    while functionToUse != 1 or functionToUse != 2 or functionToUse != 3 or functionToUse != 4 or functionToUse == 5: # While loop to check if the value is between 1 and 5
        functionToUse = int(input("Please enter the number that corresponds to the function that you want to use: "))
        if 1 <= functionToUse <= 4:
            print()
            break # If the value is between 1 and 4
        elif functionToUse == 5: # Always need the user's consent to exit the program
            print("Goodbye! Have a nice day!")
            break
        else:
            print("Wrong input! Try again!\n") # If the value is not between 1 and 5. Repeat.

    if functionToUse == 1: # The first function of the program
        algorithm = input("Please enter the instruction: ")
        for i in range(len(algorithm)):
            checkBracket = False # Must follow the rules of BIDMAS (Brackets, Indices, Division, Multiplication, Addition, Subtraction) and yes I learned my english from the Great Britain




    print("=" * 30 + " CALCULATOR " + "=" * 30, end="\n")  # Footer of the program
else: # If the user's input is not 1 then execute a goodbye statement
    print("Goodbye! Have a nice day!")