# Simple CLI Calculator 
print ("Ewan test runs Simple CLI Calculator")

is_running = True

while is_running:
    # Processing Calculations...
    print("Starting Calcultor Process")

    user_operation = input("What operation would you like to perform?\nPick any of ['+', '-', '*', '/', '%']")

    # Get user numbers
    try: # Try to get user numbers, if they're valid integers/floats, continue

        no1 = float(input("First number: "))
        no2 = float(input("Second number: "))
        
        except: # We get an error when running it
        print("Failed, invalid numbers...")
        continue 

    if user_operation == "*":
        # perform multiplication
        pass

    elif user_operation == "+":
        # perform addition
        pass

    elif user_operation == "/":
        # perform division
        pass

    elif user_operation == "-":
        # perform substraction
        pass

    elif user_operation == "%":
        # perform modulus
        pass

    else:
        # Invalid operation 
        print("Invalid operation entered, try again")


# Ctrl + C to exit any Python program...!