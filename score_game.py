"""2. The game() function in a program lets a user play a game and returns the score as an
integer. You need to read a file ‘Hi-score.txt’ which is either blank or contains the previous
Hi-score. You need to write a program to update the Hi-score whenever the game()
function breaks the Hi-score."""

def game():
    score = 20 
    return score

with open("Hi-score.txt", "r")as file:
    content = file.read()

if content != "":
    Hi_score = int(content)
else:
     Hi_score = 0 

score = game()

if score > Hi_score :
   with open("Hi-score.txt", "w")as file:
       file.write(str(f"Hi_Score is {score}"))
else:
    with open("Hi-score.txt", "w")as file:
        file.write(str(f"Hi_Score is {Hi_score}"))
   