# Factorial of a Number

def facto(n):
    if n == 1:
        return 1 
    else:
        return n * facto(n-1)

if __name__ == "__main__":
    i = int(input("Enter n: "))
    print(facto(i))