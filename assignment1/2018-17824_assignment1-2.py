######################
##    Bubble Sort   ##
######################

def BubbleSort(A):
    for i in range(0,len(A)-1):
        for j in range(len(A)-1,i,-1):
            if A[j]<A[j-1]:
                temp = A[j]
                A[j] = A[j-1]
                A[j-1] = temp

        print(A)



data = list(map(int, open("input.txt","r").read().split(" ")))
print(data)
BubbleSort(data)
