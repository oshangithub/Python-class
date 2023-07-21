class HumanBeing:  
    hello="welcome to my class"
    def __init__(self,name):#creating constructer    
        self.name=name
    def greeting(self):  #instance method   
          print(f"{self.hello}my name is {self.name}")
oshan_object=HumanBeing("Oshan")
oshan_object.greeting()




        