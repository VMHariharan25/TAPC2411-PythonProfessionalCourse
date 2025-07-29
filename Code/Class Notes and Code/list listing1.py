# Creating a list of even numbers till n 

# Receive n 
n = int(input("Please Enter n: "))

list_even = []
for i in range(0,n+1, 2): 
    list_even.append(i)

print(list_even)