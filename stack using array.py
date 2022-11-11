import numpy as np
def push(arr,top,size):
    s=size
    if(top!=s):
        top=top+1
        num=int(input("Enter number to append : "))
        arr[top]=num
        print("top =",top)
        print("arr =",arr)
    else:
        print("stack overflow")
        
    return top
def pop(arr,top):
    if(top==-1):
        print("Stack underflow")
    else:
        top-=1
    return top
def display(arr,top):
    for i in range(top+1):
        print(arr[i],end=" ")
    return arr
    

top=-1
size=int(input("Enter size of stack :"))
arr=np.zeros(size,dtype=int)
print(arr)
condition=True
while(condition==True):
    print("\n----------------------------------------------")
    print("\n1.push()\n2.pop()\n3.display()\n4.exit")
    print(top,"------",arr)
    n=int(input())
    if(n==1):
        top=push(arr,top,size)
    elif(n==2):
        top=pop(arr,top)
    elif(n==3):
        display(arr,top)
    elif(n==4):
        print("--------- program has been killed -------")
        condition=False
    else:
        print("Enter valid Choice")
