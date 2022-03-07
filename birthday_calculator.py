#This script calculates your birthday
import datetime
import math
current_date=datetime.date.today().strftime('%Y-%m-%d')
splitted_date=current_date.split('-')
birthdate=input("Please input your birthday in yyyy-mm-dd format:  ")
splt_birthday=birthdate.split('-')
for i in range(3):
    splt_birthday[i]=int(splt_birthday[i])
    splitted_date[i]=int(splitted_date[i])
print(splitted_date)
if splitted_date[2]<splt_birthday[2]:
    splitted_date[2]+=30
    splitted_date[1]-=1
if splitted_date[1]<splt_birthday[1]:
    splitted_date[1]+=12
    splitted_date[0]-=1
result=[]
for m in range(len(splt_birthday)):
    x=splitted_date[m]-splt_birthday[m]
    result.append(x)
print(f"your age is {result[0]} years and {result[1]} mounth and {result[2]} days!")

