# Fibanocci Memoised 
f = [1, 1]
def fibo(n):
    for _ in range(len(f), n):
        f.append(f[-1]+ f[-2])
    return f[n-1]

