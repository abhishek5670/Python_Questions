'''A parking lot in a mall has RxC number of parking spaces. Each parking space will either be  empty(0) or full(1). The status (0/1) of a parking space is represented as the element of the matrix. The task is to find index of the prpeinzta row(R) in the parking lot that has the most of the parking spaces full(1).'''
r=int(input("enter row"))
c=int(input("enter column"))
sum=0
m=0
id=0
for i in range(r):
    for j in range(c):
        z=int(input("ENter either 0/1:"))
        print("Row:",i,"value:",z)
        sum+=z
    if sum>=m:
        m=sum
        id+=1
        print(m)
    sum=0
print("The Row which have most of the parking Spaces full is : ",id)
