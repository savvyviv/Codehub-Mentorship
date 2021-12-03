import random
draw=random.randint(1,4)
guess=input("Guess what number the computer generated: ")
print(draw)
while guess!=draw:
    input("Try again: ")
    print(draw)
    if guess==draw:
     continue
     print("Good Job!")
 



