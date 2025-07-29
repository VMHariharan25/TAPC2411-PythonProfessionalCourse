# If the number is divisible by 2 and 3, then print it as factor of six
# If the number is divisible by 2 and 5, then print it as factor of ten 

number = input("Enter the number: ")
# Output datatype of the input function is STRING 
number = int(number)

if(number % 2 == 0):
    if(number % 3 == 0):
        print("The number is divisble by 6")
    elif(number % 5 == 0):
        print("The number is divisible by 10")