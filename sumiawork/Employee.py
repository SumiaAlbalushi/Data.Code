class Employee:
    
    
     #constructor
    def __init__(self,empname, empid, empsalary,empdepartment):
        self.empname = empname
        self.empid = empid
        self.empsalary = empsalary
        self.empdepartment = empdepartment
        
        
    def get_name(self):
         return self.empname
    
    def get_id(self):
         return self.empid
    
    def get_salary(self):
         return self.empsalary
    
    def get_department(self):
         return self.empdepartment
        
        
    def set_name(self, newName):
            self.empname = newName
    
    def set_id(self, newId):
            self.empid = newId
    
    def set_salary(self, newsalary):
            self.empsalary = newsalary
    
    def set_department(self, newdepartment):
            self.empdepartment = newdepartment
    
    
      
    def descrip(self):
            return f"employee name is {self.empname} id is {self.empid} the salary {self.empsalary} in {self.empdepartment} department"
