a = [1,4,3,2,3,4,2]
SOP = 0
DP = [0]*len(a)

for i in range(len(a)):
    if i==0:
        DP[i]=a[i]
    elif i==1:
        DP[i]=max(DP[i-1]+a[i],a[i-1]*a[i])
    else:
        DP[i]=max(DP[i-2]+a[i-1]*a[i],DP[i-1]+a[i])

print(DP)
