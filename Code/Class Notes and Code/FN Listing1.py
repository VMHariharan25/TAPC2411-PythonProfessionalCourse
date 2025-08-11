# Recieve 2 Numbers 
# if both are even, you have to multiply each and then return 
# if either of them is odd, you have to divide 

def two_input(): 
    """Recieve two inputs from the user and convert it to int and return""" # Doc String 
    # Doc String should be given in triple double quotes or triple single quotes 
    a = input("Enter a: ")
    b = input("Enter b: ")
    return int(a), int(b) # Only place where you would not use iterator to combine multiple output 

def even_check(n):
    if(n%2 == 0):
        return True 
    else: 
        return False 

def core_function(a, b):
    if(even_check(a) and even_check(b)): 
        return a*b 
    else:
        return a/b 

if __name__ == "__main__":
    p ,q = two_input() 
    print(core_function(p,q))
