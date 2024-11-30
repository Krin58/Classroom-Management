import mysql.connector as a
con=a.connect(host="localhost", user="root", passwd="zxcIE0-=")
c=con.cursor()

c.execute("create database class_database")
c.execute('use class_database')
c.execute("create table monitor(Roll int,Name varchar(50),Month varchar(20))")
c.execute("create table marks(Roll int,name varchar(50),Mathematics int,Physics int,Chemistry int,`Computer Science` int,English int,Total int,Percetage float,Term varchar(20))")
c.execute("create table attdance(Date varchar(10),Abs varchar(500))")
c.execute("create table students(Roll int,Name varchar(50),Phone int,Address varchar(50))")
c.execute("create table inventory(Benches int,Teachers_Table int,Fans int,Lights int,Display_Board int,Black_Board int,Cupboard int,Date varchar(10))")

con.commit()
print("Database Created")
