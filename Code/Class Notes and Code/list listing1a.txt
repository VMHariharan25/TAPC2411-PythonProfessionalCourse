# Creating a list of even numbers till n 

# Receive n 
n = int(input("Please Enter n: "))
list_even = [i for i in range(0, n+1, 2)]
print(list_even)
