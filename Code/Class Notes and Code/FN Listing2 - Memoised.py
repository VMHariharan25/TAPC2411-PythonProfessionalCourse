# Factorial of a Number
# With Memoisation 
fact={0:1, 1:1}
def iskey(d, element):
    list_of_keys = list(d.keys())
    if element in list_of_keys:
        return True
    return False 

def facto(n):
    if iskey(fact, n): 
        return fact[n] 
    else: 
        t = n * facto(n-1)
        fact[n] = t 
        return t 

if __name__ == "__main__":
    i = int(input("Enter n: "))
    print(facto(i))