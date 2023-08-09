class person :
    #constructor to creat objects
    def __init__(self,name, p_age):
        self.name = name
        self.age = p_age
      
      
    def say_hi(self):
        return f"Hi you {self.name} as person"
    
        
    #use term of encapsulation
        #accsesor method
    def get_name(self):
         return self.name
    def get_age(self):
         return self.age
        
    #setter / mutotur methods
    def set_name(self, newName):
            self.name = newName
    
    def set_age(self, newAge):
            self.age = newAge
    
    def run(self):
        print(self.name, "is running")
            
    
    def descrip(self):
            return f"person name {self.name} is {self.age} years old"
    
    def laugh(self):
        print(self.name,"say hahahahah")
        






