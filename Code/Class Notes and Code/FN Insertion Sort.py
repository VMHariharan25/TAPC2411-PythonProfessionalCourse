# Insertion Sort 

def InsertionSort(A): 
    n = len(A) # Total Number of Elements in A 
    for i in range(1, n):
        key = A[i]
        j = i - 1 
        while(j >= 0 and A[j] > key):
            A[j+1] = A[j]
            j = j - 1
        A[j+1] = key 
        print(f"{i}th Iteration: {A}")
    return A 



