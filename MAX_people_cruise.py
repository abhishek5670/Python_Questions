''' A party has been organised on cruise. The party is organised for a limited time(T). The number of guests entering (E[i]) and leaving (L[i]) the party at every hour is represented as elements of the array. The task is to find the maximum number of guests present on the cruise at any given instance within T hours. '''
t=int(input("Enter thr instance time : "))
E=[]
L=[]
S=[]
sum=0
for i in range(t):
    enter=int(input("No. of guest enter : "))
    E.append(enter)
for j in range(t):
    live=int(input("No. of guestlive : "))
    L.append(live)
for k in range(t):
    sum=sum+E[k]-L[k]
    S.append(sum)
print(max(S))
