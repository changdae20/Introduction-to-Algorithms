######################
##  Selection Sort  ##
######################

def SelectionSort(A):
    for j in range(0,len(A)-1):
        min_idx = j
        for i in range(j+1,n):
            if A[i]<A[min_idx]:
                min_idx = i
        temp = A[min_idx]
        A[min_idx] = A[j]
        A[j]=temp
        print(A)

data = list(map(int, open("input.txt","r").read().split(" ")))
n = len(data)
print(data)

SelectionSort(data)
