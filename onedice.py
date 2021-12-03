import random
roll=random.randint(1,6)
user_name=input("What is your name?: ")
print(" ")
print(f"Welcome {user_name} to Vienne's lucky lotto Your lucky number is {roll}")
print("  ")
if roll==(2):
    print("roll again")
elif roll==(3):
    print("roll again")
elif roll==(4):
    print("roll again")
elif roll==(5):
    print("roll again")
elif roll==(1):
    print("Move to the next step.")
elif roll==(6):
    print("Drop the dice.")