import random
roll=random.randint(1,6)
user_name=input("What is your name?: ")
print(f"Welcome {user_name} to Vienne's lucky lotto Your lucky number is {roll}")
print("  ")
if roll<=(5):
    print("Roll again.")
if roll==(6):
    print("Move to the next step.")
if roll==(1):
     print("Drop the dice.")
