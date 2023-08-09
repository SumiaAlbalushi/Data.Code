import pandas as pd

student=pd.read_csv('GPA.csv')
print(student)

df = pd.DataFrame(student)

gpa_list = df['Gpa'].tolist()
print(gpa_list)

average = sum(gpa_list) / len(gpa_list)
print(average)

newgpa = input("enter new gpa")
print(newgpa)

gpa_list.insert(3,newgpa)
print(gpa_list)