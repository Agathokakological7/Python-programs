/* 

x- Representing the dimensions of a cuboid  -- i
y- Representing the dimensions of a cuboid  -- j
z- Representing the dimensions of a cuboid  -- k
n- Is an integer where i+j+k not equal to n(i+j+k != n) then we are going to print it

Constraints :  0 <= i <= X; 0 <= j <= Y; 0 <= k <= Z

sample input: 1 2 3 3
sample output:
    [[0, 0, 0], [0, 0, 1], [0, 0, 2], [0, 1, 0], [0, 1, 1], [0, 1, 3], [0, 2, 0], [0, 2, 2], [0, 2, 3],
    [1, 0, 0],[1, 0, 1], [1, 0, 3], [1, 1, 0], [1, 1, 2], [1, 1, 3], [1, 2, 1], [1, 2, 2], [1, 2, 3]]
    
*/

x,y,z,n=map(int,input("Enter values :").split())[:4]
l=[]
for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            if(i+j+k!=n):
               l.append([i,j,k])
print(l)
