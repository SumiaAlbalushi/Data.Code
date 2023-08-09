from person import person
class student(person):
    
     #constructor
    def __init__(self,sname, sage, year):
        super().__init__(sname, sage)
        self.acadmic_year = year
        
    def say_hi(self):
        return f"Hello {self.name} as student"
    