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
    print()
    
print("Thanks for driving with On The Road Again!")