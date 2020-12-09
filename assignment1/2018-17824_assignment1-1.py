######################
##  Insertion Sort  ##
######################

def InsertionSort(A):
    for j in range(1,len(A)):
        key = A[j]
        i = j-1
        while i>=0 and A[i]>key:
            A[i+1] = A[i]
            i=i-1
        A[i+1] = key
        print(A)


data = list(map(int, open("input.txt","r").read().split(" ")))
InsertionSort(data)
