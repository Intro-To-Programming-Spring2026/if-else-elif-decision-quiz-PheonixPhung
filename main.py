# Mini Project — Decision Quiz
#Student Name: 
# Topic: If / Elif / Else
# Goal: Create a quiz that gives different feedback based on the user's answer

print("Welcome to the Decision Quiz!")
print("-----------------------------")

print("What is the fastest speed, in mph, an F1 car has reached?")
answer = input("Enter your answer: ")

if answer == "231.4":
  print("You're correct! It was set by Valtteri Bottas in a Williams.")
        
elif answer < "231.4":
  print("You're incorrect. This was Max's fastest average speed for a lap in the Monza Grand Prix!")

else:
  print("You may or may not be slow! This is NOT a speed.")
# TODO 4: Print a closing message
print("Thanks for taking the quiz!")
