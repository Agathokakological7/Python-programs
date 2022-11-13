x,y,z,n=1,2,3,3
l=[]
for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            if(i+j+k!=n):
               l.append([i,j,k])
print(l)
