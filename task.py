

# List of numbers
listOfStuff = [21, 33, 77, 2, 4, 10, 3, 17]

# This while loop starts listing the odd and even from index 0 which is number from 21
count = len(listOfStuff)
n=0
print('while loop')
print(count)
while n<count:
     if listOfStuff[n] % 2 == 0:
        print(f"even - {listOfStuff[n]}")
     else:
        print(f"odd - {listOfStuff[n]}")
     n+=1
        
    
    
    
print('-----------------------------------------------------------------')

#this for loop starts listing the odd and even number from index 0 which is 21
print('for loop')
listOfStuff = [21, 33, 77, 2, 4, 10, 3, 17]
for x in listOfStuff:
    if x % 2 == 0:
        print(f"even - {x}")
    else:
        print(f"odd - {x}")

