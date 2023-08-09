from person import person
class teacher(person):
    
    def __init__(self,tname, tage, eyear):
        super().__init__(tname, tage)
        self.experiance_year = eyear
        
    def say_hi(self):
        return f"Hi {self.name} as teacher"