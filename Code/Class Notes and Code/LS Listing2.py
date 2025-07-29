# Sum of first n odd numbers 

n = int(input("Enter the value n: "))
odd = 1  # Trace the odd number 
sum = 0   # To store the result 
for _ in range(n): # _ => Nullify the storing of range 
    sum = sum + odd 
    odd += 2 

print("The sum of first %d odd numbers is %d" %(n, sum))