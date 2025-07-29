# Sum of first odd numbers till n 

n = int(input("Enter the value n: "))
sum = 0 
for i in range(1, n+1, 2):
    sum += i 

# 1 + 3 + 5 + 7 + 9 = 25 
# 1 + 3 + 5 + 7 + 9 + 11 + 13 + 15 + 17 + 19 = 100
print("Sum of odd numbers is %d"%sum)