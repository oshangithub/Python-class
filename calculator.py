for c in range(1,10,1): 
    choice=(input("enter your choice"))
    a=int(input("enter first number"))
    b=int(input("enter second number"))
    if choice=="+":
        c=a+b
        print(c)
    elif choice=="-":
        c=a-b
        print(c)
    elif choice=="*":
        c=(a*b)
        print(c)
    elif choice=="/":
        c=(a/b)
        print(c)
    elif choice=="**":
        c= (a**b)
        print(c)
    else:
        print("its is not required")
        



