def prime():    
    num=int(input("enter a number"))
    f=0
    for i in range(2,int(num/2)+1):
        if num%1==0:    
            f=1
            break
    if f==0:
        print("it is a prime number")
    else:   
        print("its is not a prime nuber")
prime()
    