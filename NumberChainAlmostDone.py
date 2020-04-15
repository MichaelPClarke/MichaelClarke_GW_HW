# Initial variable to track game play
user_play = "y"
user_play2 = "y"

# While we are still playing...
while user_play == "y":

    # Ask the user how many numbers to loop through
    user_number = int(input("How many numbers? "))

    for x in range(user_number):
        print(x)
    user_play2 = input("Continue the chain: (y)es or (n)o? ")
    
    while user_play2 =="y":
        
        user_number2 = int(input("How many numbers? "))
                
        for x in range(user_number, user_number2 + user_number, 1):
                print(x)
                  
        user_play2 = input("Continue the chain: (y)es or (n)o? ")
    else: break
          
