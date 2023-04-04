class Dog:

    def _init_(self, name, age, coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color
    
    def description(self):
        print(f"{self.name} is {self.age} years old.")
    
    def get_info(self):
        print(f"The coat color of {self.name} is {self.coat_color}.")
        

class Labradog(Dog):
    def _init_(self, name, age, coat_color):
        super()._init_(name, age, coat_color)
        
    def guard_duty(self):
        print(f"{self.name} is a good guard dog.")
        

class Bulldog(Dog):
    def _init_(self, name, age, coat_color):
        super()._init_(name, age, coat_color)
        
    def snore(self):
        print(f"{self.name} snores loudly.")



dog1 = Dog("Husky", 3, "brown")
dog1.description()  
dog1.get_info() 

dog2 =Labradog("Max", 5, "white")
dog2.description()  
dog2.get_info()  
dog2.guard_duty()  

dog3 = Bulldog("Bruno", 2, "brindle")
dog3.description()  
dog3.get_info()  
dog3.snore()  

