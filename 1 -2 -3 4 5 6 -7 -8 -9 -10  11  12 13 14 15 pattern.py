/* question : printing a sequence of number 1 -2 -3 4 5 6 -7 -8 -9 -10  11  12 13 14 15

   This can also be printed in form of triangle
   1 
   -2 -3 
   4 5 6 
   -7 -8 -9 -10 
   11 12 13 14 15

   
 */
c=1
for i in range(6):
    for j in range(i):
        if(i%2!=0):
            print(c)
        else:
            print(c*-1)
        c+=1    
    
    
