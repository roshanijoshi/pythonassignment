from random import randint
computer_generated_number=randint(1,10)
attempts= 5
ATTEMPTS_TO_SCORE_MAPPING = {
    "1": 100,
    "2": 90,
    "3": 70,
    "4": 50,
    "5": 32,
}

print(f'The computer generated number is: {computer_generated_number}')
print("You have 5 chances to guess the number:")
for attempt in range(1,attempts+1): # the loop will execute 5 times
    user_choice=int(input('Enter your number:'))
    print(user_choice)
    if user_choice==computer_generated_number:
    
        print(f"Congrats! you won and Your score is:{ATTEMPTS_TO_SCORE_MAPPING[str(attempt)]}")
        break
   
   
    else:

        print("Wrong Guess. Try again")
        


