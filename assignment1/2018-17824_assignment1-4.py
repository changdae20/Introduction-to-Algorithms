######################
##    Merge Sort    ##
######################

data = list(map(int, open("input.txt","r").read().split(" ")))
n = len(data)
print(data)

def Merge(A,p,q,r):
    
    n1 = q-p+1
    n2 = r-q
    L = []
    R = []
    for i in range(1,n1+1):
        L.append(A[p+i-1])
    for j in range(1,n2+1):
        R.append(A[q+j])
    L.append(n+1)
    R.append(n+1)
    i=0
    j=0
    for k in range(p,r+1):
        if L[i]<=R[j]:
            A[k] = L[i]
            i = i+1
        else:
            A[k] = R[j]
            j = j+1

def MergeSort(A,p,r):
    if p<r:
        q=int((p+r)/2)
        MergeSort(A,p,q)
        MergeSort(A,q+1,r)
        Merge(A,p,q,r)

MergeSort(data,0,n-1)
print(data)
