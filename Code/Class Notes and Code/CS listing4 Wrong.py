# If the lowest factor (other than 1) of a given number is 2 then print "Twilight"
# If the lowest factor (other than 1) of a given number is 2 then print "SQL"
# If others is the lowest factor, print "PYTHON"

number = input("Enter the number: ")
# Output datatype of the input function is STRING 
number = int(number)

if(number % 2 == 0):
    print("Twilight")

if(number % 3 == 0):
    print("SQL")
else: 
    print("PYTHON")