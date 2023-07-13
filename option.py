operator=input("enter the operation")
a=int(input("enter first number"))
b=int(input("enter second number"))

def add(num_1,num_2):
    sum=num_1+num_2
    return sum
def subtract(num_1,num_2): 
    sub=num_1-num_2
    return sub
def multiply(num_1,num_2):  
    mult=num_1*num_2
    return mult
def division(num_1, num_2): 
    div=num_1/num_2
    return div

if operator=="+":
    print(add(a,b))
elif operator=="-": 
    print(subtract(a,b))
elif operator=="*": 
    print(multiply(a,b))
elif operator=="/": 
    print(division(a,b))
else:   
    print("not required")