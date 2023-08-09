from person import person
from studentclass import student
from teacher import teacher
def main():
    Hanna = person("Hanna Al-zadgali", 23)
    person2 = person("Hamza", 17)
    
    std1 = student("latifa", 18, 2021)
    std2 = student("Harith", 21, 2022)
    teach1 = teacher("sumia", 30, 10)
    print(teach1.say_hi())
    print(std1.say_hi())
    print(student.say_hi(std2))
    #print(person.say_hi())

    print(person2.descrip())
    print(Hanna.get_name())
    
    Hanna.set_name("Hanna AbdulWahab Al-zadgali")
    print(Hanna.get_name())
    print(Hanna.descrip())
    Hanna.run()
    Hanna.laugh()
    person2.laugh()


main()