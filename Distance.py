import math
cigarettes = [7,7,3,1]
weight = [70,40,40,40]
Heart= ["bad","bad","good","good"]
D=[]
c = int(input("enter numbers of cegarettes smoke i a day!"))
w = int(input("Enter the weight!"))

for i in range(len(cigarettes)):
    
    d = math.sqrt((c-cigarettes[i])**2)+((w-weight[i])**2)
    D.append(d)
m=min(D)
ind=D.index(m)
print("you belong to",Heart[ind])
    

    