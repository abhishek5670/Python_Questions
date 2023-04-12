"""Given an integer array Arr of size N the task is to find the count of elements whose value is greater than all of its prior elements.

Note : 1st element of the array should be considered in the count of the result."""


L=[3,4,5,8,9,47,8,4,2,4,67,4,6,4,6,4,5,4,2,3,4,5,6,5,5,3,2,4,54,65,5,7,5,4,6,534,5,56,456,4564,6,56,45,546,456,45,56,453,2,43,4534,6634,7] # This is Input for list
N=len(L)
C=1
for i in range(N-1):
    if(L[i]<L[i+1]):
        C+=1
print(C)
