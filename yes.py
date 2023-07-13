def opt(operator,num1,num2):    
    if operator=="+":   
        result=num1+num2
    elif operator=="-": 
        result=num1-num2
    elif operator=="*":
        result=num1*num2
    elif operator=="/":    
        result=num1/num2
    else:
        print("not required")
        return result
    operator=input("enter an operator(+,-,*,/):")
    print()
    number1=float(input('enter the first number:'))
    print()
    number2=float(input('enter the second number:'))
    print()
    result=opt(operator,number1,number2)
    if result is not None:  
        print("result:",result)
