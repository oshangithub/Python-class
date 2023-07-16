
customer_name=input("enter your name")
print("hello welcome to our shop")
pizza={
   " chicken_pizza":550,
   "mushroom_pizza":600,
   "veg_pizza":400
} 
total_amt=0

while True:     
    
    customer_needs=input("enter your choice")
    if customer_needs=="no":
        break
    if customer_needs in pizza:    
        print(pizza[customer_needs])
        price=pizza[customer_needs]
        total_amt+=price
        print("total_amt is"+str(total_amt))
total_bill=0
toppings={
 "pepproine":550,
   "mushroom":600,
   "sasuage":400
} 

while True: 
    customer_needs=input("enter toopings chioce")
    if customer_needs=="no":
        break
    if customer_needs in toppings:    
        print(toppings[customer_needs])
        price=toppings[customer_needs]
        total_bill+=price
        print("total_amt is"+str(total_bill))
final_amt=(total_amt+total_bill)
print(final_amt)
