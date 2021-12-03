# iterate through every number in a list to separate out even and odd numbers.
my_list=[1,2,3,4,5,6,7,21,33,32,2,4]
even=[]
odd=[]
for n in my_list:
    if n % 2==0:
        even.append(n)
    else:
        odd.append(n)     
print(" ")
print(even)
print(" ")
print(odd)

