import sqlite3

connection=sqlite3.connect('student.db')

cursor=connection.cursor()

table_info="""CREATE TABLE student(Name Varchat(24),class varchar(10),section varchar(5),marks int)""" 
cursor.execute(table_info)

cursor.execute(''' Insert into student values('Rahul','Data Science','A',90)''')
cursor.execute(''' Insert into student values('Raj','Data Science','B',80)''')    
cursor.execute(''' Insert into student values('Ravi','Devops','C',70)''')
cursor.execute(''' Insert into student values('Raju','Devops','A',90)''')

print('Inserted records successfully')

data = cursor.execute('''Select * from student''')
for row in data:
    print(row)



connection.commit()
connection.close()