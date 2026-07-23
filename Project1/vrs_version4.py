choice = ""

while choice != "stop!":

    print("Welcome to On The Road Again Vehicle Rental Calculator.")

    choice = input('Please enter "Go!" to continue or "Stop!" to exit:\n')
    choice = choice.lower()

    while choice != "go!" and choice != "stop!":
        print('Invalid. Please enter "Go!" to rent a vehicle or "Stop!" to exit.')
        choice = input()
        choice = choice.lower()

    if choice == "go!":

        rewards = input("Are you a member of our Road Warriors rewards club? Enter Y/N:\n")
        rewards = rewards.upper()

        while rewards != "Y" and rewards != "N":
            print("Invalid. Please enter Y if in Road Warriors, N if not.")
            rewards = input()
            rewards = rewards.upper()

        print("Please choose from the following menu to rent a vehicle:")

        if rewards == "Y":
            print("E for Economy at $50.00 per day.")
            print("S for SUV at $75.00 per day.")
            print("M for Minivan at $200.00 per day.")

        else:
            print("E for Economy at $55.00 per day.")
            print("S for SUV at $85.00 per day.")
            print("M for Minivan at $220.00 per day.")

        vehicle = input("Enter your vehicle choice (E, S, or M):\n")
        vehicle = vehicle.upper()

        while vehicle != "E" and vehicle != "S" and vehicle != "M":
            print("Invalid. Please enter E, S, or M:")
            vehicle = input("Enter your vehicle choice (E, S, or M):\n")
            vehicle = vehicle.upper()

        age = int(input("Enter your age. 65 and over get 10% Senior Citizen discount:\n"))

        # Determine the rental cost

        if rewards == "Y":

            if vehicle == "E":
                cost = 50.00

            elif vehicle == "S":
                cost = 75.00

            else:
                cost = 200.00

        else:

            if vehicle == "E":
                cost = 55.00

            elif vehicle == "S":
                cost = 85.00

            else:
                cost = 220.00

        # Determine the senior discount

        if age >= 65:
            discount = cost * 0.10

        else:
            discount = 0

        # Calculate final cost

        final_cost = cost - discount

        # Display results

        print("Cost Before Discount", cost)
        print("Age Discount", discount)
        print("Cost After Discount", final_cost)

print("Thanks for driving with On The Road Again!")