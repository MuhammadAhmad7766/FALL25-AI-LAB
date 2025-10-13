player = input("Enter your name:")
total = 0
prev_number = 0
import random
while True:

    number = random.randint(1, 20)
    total = prev_number + number    
    prev_number = number            
    

    if total % 3 == 0 and total % 5 == 0:
        correct = "fizzbuzz"
    elif total % 3 == 0:
        correct = "fizz"
    elif total % 5 == 0:
        correct = "buzz"
    else:
        correct = str(total)
    

    print(number)  
    guess = input("Your answer: ").lower()
        
    if guess != correct:
        print(f"Wrong! The correct answer was {correct}. Game Over!")
        break
else:
    print("Congratulations! You survived all 100 rounds of FizzBuzz!")

