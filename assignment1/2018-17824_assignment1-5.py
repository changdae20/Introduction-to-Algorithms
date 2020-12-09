######################
##    Quick Sort    ##
######################

def Partition(A,p,r):
    x=A[r]
    i=p-1
    for j in range(p,r):
        if A[j]<=x:
            i=i+1
            temp = A[j]
            A[j]=A[i]
            A[i]=temp
            
    temp = A[i+1]
    A[i+1] = A[r]
    A[r] = temp
    print(data)
    return i+1

def QuickSort(A,p,r):
    if p<r:
        q=Partition(A,p,r)
        QuickSort(A,p,q-1)
        QuickSort(A,q+1,r)

data = list(map(int, open("input.txt","r").read().split(" ")))
n = len(data)
print(data)

QuickSort(data,0,n-1)
