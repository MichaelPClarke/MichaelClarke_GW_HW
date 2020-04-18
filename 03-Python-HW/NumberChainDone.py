# Initial variable to track game play
user_play = "y"
last_number=0
# While we are still playing...
while user_play == "y":

    # Ask the user how many numbers to loop through
    user_number = int(input("How many numbers? "))
    user_number+=last_number
    
    for x in range(last_number, user_number):
        print(x)
        last_number = last_number + 1
    user_play = input("Continue the chain: (y)es or (n)o? ")
    
    if user_play == "n":
        break

    
