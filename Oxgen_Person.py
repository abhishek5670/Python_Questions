''' Selection of MPCS exams include a fitness test which is conducted on ground. There will be a batch of 3 trainees, appearing for running test in track for 3 rounds. You need to record their oxygen level after every round. After trainee are finished with all rounds, calculate for each trainee his average oxygen level over the 3 rounds and select one with highest oxygen level as the most fit trainee. If more than one trainee attains the same highest average level, they all need to be selected.'''

n=3
m=[]
j=[]
k=[]
ma=0
for i in range(n):
    for j in range(n):
        print("For athelet :",i)
        k=int(input("Enter the value of oxyegen level :"))
        if k in range(1,100):
            m.append(k)
        else:
            print("invalid")
for n in range(len(m)):
    a=float((m[n]+m[n+1]+m[n+2])/3)
    j.append(float((m[n]+m[n+1]+m[n+2])/3))
    n+=3
ma=max(j)
for h in range(len(j)):
    if j[h]== ma:
        k.append(h)
print(k)
