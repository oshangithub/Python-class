total_amt=0
d={
    "tv":20000,
    "computer":30000,
    "mobile":10000
} 
for key,value in d.items(): 
    print(key,value)
while True: 
    customer_needs=input('enter your choice')
    if customer_needs=="no":    
        break
    if customer_needs in d: 
        print(d[customer_needs])
        price=d[customer_needs]
        total_amt+=price
print("total_amt is"+str(total_amt))

