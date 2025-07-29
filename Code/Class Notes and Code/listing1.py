### Comments ### Not ba a part of an execution
# Single Line Comments #
## Multi line Comments Either '''   Comments '''  or """  Comments  """  ; docstrings 

"""
>>> 5/2 # Division operator
2.5

5 -> Integer 
2 -> Integer 
5 is not a multiple of 2 
Quotient --> Decimal 

>>> 2/1
2.0

2 -> Integer
1 -> Integer 
2 is a multiple of 1 
Quotient is expected as integer 
but received as float 

Output data type of an division operator is Float 

>>> 5 // 2
2

// is the integer division operator where the output will be always an integer iff the operands are integers 


>>> 5 % 2 # Gives the remainder on dividing 5 upon 2
1

Remainder(p/n) ==> {0, 1, 2, ... , n-1}

remainder(p/6) ==> {0, 1, 2, 3, 4, 5}

Power Operator 
"**" --> Power Op. 
>>> 5**2 
25

Complex Number: 
sqrt(-1) = i 
sqrt(-5) = sqrt(5) i 
general form of Complex Number: 
a + b i 
a is the real part 
b is the imaginary part 

Eg. 5+3i 

In Python, we would be using "j" instead of iota "i" which traditionally represents the sqrt{-1} 
>>> 5+3j 


Variables are used without declaration but the first operation is assignment operation 

>>> i = 5
--> Space is allocated for i 
    -> Memory Allocation ; via OS; Memory address 
    -> Python places an id for the mem space; memory id 
        > To print the memory id, "id(varible_name)" 

--> i is called as object of the data type 
    -> Data Type: int, float, double, string, complex, boolean
    -> To find the data type of data avaible in a variable 
        > type(varible_name)

--> Object: Instance of the class 

>>> type(i)
<class 'int'>  
--> i is an object of integer 

>>> i = 5
>>> type(i)
<class 'int'>
>>> j = 5
>>> k = 7
>>> id(i)
140724176161336
>>> id(k)
140724176161400
>>> id(j)
140724176161336

if values of the variables are same, the memory id of the variables are also same.
--> id(i) and id(j) are equal.

Multiple assignment operators 
>>> i = j = k = l = 7
>>> i, j, k = 1, 2, 3
>>> i, j, k = 9
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: cannot unpack non-iterable int object
>>> i, j, k = 1, 2, 3, 89
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: too many values to unpack (expected 3)


"""

