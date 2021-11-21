# 1.One of the reasons why it's necessary to cast in python is that, it avoids loss of data
# 2. Write a script that calculates a person's age when he gives his date of birth
year_of_birth=input("What year were you born? ")
current_year=input("What year are we currently in? ")
age=int(current_year)-int(year_of_birth)
print(f"That means you are {age} years old")
print ("  ")
# 3. what data type is a facebook/twitter post stored in? They are stored as json files which returns in python as dictionary data type.
# 4. is it possible to cast from integer to boolean? show in example code
positive_num=2
answer=bool(positive_num)
print(type(answer))
print(answer)
print("  ")
one=0
answer=bool(one)
print(type(answer))
print(answer)