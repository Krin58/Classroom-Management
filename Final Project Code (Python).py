# Importing The Required Modules

import mysql.connector as a
import matplotlib.pyplot as pt
import numpy as np
import sys

# Establishing Connection Between Python And MySQL
try:
    con=a.connect(host="localhost", user="root", passwd="zxcIE0-=",database='class_database')
except:
    print("Connection Error !!!")
    sys.exit(0)

# Creating Cursor Object

c=con.cursor()

# User Defined Function For Enterting/Updating Monitor And Checking Monitor

def monitor():

    i=int(input("1.Update Monitor [1] \t2.Check Monitor [2] \n"))               # Taking Input For Condition

    # Condition For Enterting/Updating Monitor 

    if i==1:
        q=input("Enter Student Roll : ")
        w=input("Enter Student Name : ")
        e=input("Enter Month")
        data=(q,w,e)
        s='insert into monitor values(%s,%s,%s)'
        c=con.cursor()                                                          # Creating Cursor Object
        c.execute(s,data)                                                       # To Execute SQL Statement
        con.commit()                                                            # To Save Data In Database
        print("Data Entered Successfully")
        main()

    # Condition For Checking Monitor

    else:
        c=con.cursor()                                                          # Creating Cursor Object
        c.execute("select * from monitor")                                      # To Execute SQL Statement
        d=c.fetchall()
        for i in d:
            print(i)
        main()

# User Defined Function For Enterting Marks And Checking Marks

def marks():
    i=int(input("1.Update Marks [1] \t2.Check Marks [2] \n"))                   # Taking Input For Condition
    # Condtion For Entering Marks
    if i==1:
        q=input("Enter Student Roll: ")                                         #---|
        w=input("Enter Student Name: ")                                         #   |
        s1=float(input("Mathematics: "))                                        #   |
        s2=float(input("Physics: "))                                            #   |------ To Enter The Student Data For Marks
        s3=float(input("Chemistry: "))                                          #   |-----^
        s4=float(input("Computer Science: "))                                   #   |
        s5=float(input("English: "))                                            #   |
        Ter=input("Enter Term: ")                                               #---|
        T=s1+s2+s3+s4+s5                                                        # Total Marks
        p_cent=(T/370)*100                                                      # Total Percentage
        data=(q,w,s1,s2,s3,s4,s5,T,p_cent,Ter)                                  # To Create A Data Object To Insert Into The Database
        sql='insert into marks values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'           # SQL Statement To Insert Into Database
        c=con.cursor()                                                          # Creating Cursor Object
        c.execute(sql,data)                                                     # To Execute SQL Statement
        con.commit()                                                            # To Save Data In Database
        print("Data Entered Successfully")
        main()
    # Condition for Checking Marks
    elif i==2:
        f=input("Enter how do you want to see the mark\nNumerical [1]\nPictorial [2]\n :")        # Taking Input For Condition
        # Condition for Viewing Numerically
        if f=='1':
            r=input("Enter Roll: ")
            t=input("Enter Term: ")
            sql = "select * from marks where roll = %s and term =%s"
            c=con.cursor()                                                      # Creating Cursor Object
            c.execute(sql,(r,t))                                                # To Execute SQL Statement
            r=c.fetchall()
            e=['Student Roll:\t\t','Student Name:\t\t','Mathematics:\t\t','Physics:\t\t','Chemistry:\t\t','Computer Science:\t','English:\t\t','Total Marks (For 370): ','Percentage:\t\t','Term:\t\t\t']
            for i in r:
                for j in range(len(i)) :
                    print (e[j],i[j])
            main()
        # Condition for Viewing Pictorial In Graph
        else:
            r=input("Enter Roll: ")
            t=input("Enter Term: ")
            sql = "select * from marks where roll = %s and term =%s"
            c=con.cursor()                                                      # Creating Cursor Object
            c.execute(sql,(r,t))                                                # To Execute SQL Statement
            r=c.fetchall()
            print(r)
            l=[]
            a=[]
            for i in range(len(r)):
                a.append(r[i][1])
                for j in range(2,7):
                    if str(type(r[i][j]))== '<class \'int\'>':
                        l.append(r[i][j])
                    else:
                        continue
            print(a)
            print(l)
            # The Data For Graph
            categories = ['Mathematics', 'Physics', 'Chemistry', 'Computer Science', 'English']
            data_set1 = l                       # Student Marks First set of data Blue
            data_set2 = [80, 70, 70, 70, 80]    # 100% Marks Second set of data Orange

            # To Set the bar width and bar positions
            bar_width = 0.35
            bar_positions = np.arange(len(categories))

            # To Create the grouped bar chart
            pt.bar(bar_positions, data_set1, bar_width, label='Student Marks')
            pt.bar(bar_positions + bar_width, data_set2, bar_width, label='100% Marks')

            # To Add labels and a title
            pt.xlabel('Subjects        ➡        ➡        ➡')
            pt.ylabel('Marks        ➡       ➡       ➡')
            pt.title('Student Marks:')

            # To Add category labels on the x-axis
            pt.xticks(bar_positions + bar_width / 2, categories)

            # To Add a legend
            pt.legend()

            # To Show the chart
            pt.show()
            
            main()

def marks_all():
    t=input("Enter Term: ")
    sql = "select Total,Name from marks where term =%s order by Total "
    c=con.cursor()                                                              # Creating Cursor Object
    c.execute(sql,tuple(t))                                                     # To Execute SQL Statement
    r=c.fetchall()
    l=[]
    a=[]
    for i in r:
        l.append(i[0])
        a.append(i[1])
    print(l)
    print(a)
    

    bar_width = 0.35
    pt.bar(a,l,bar_width,label='Student Marks')
    pt.xlabel('Subjects')
    pt.ylabel('Values')
    pt.title('Student Marks:',)
    pt.legend()
    pt.show()
    main()
    
# User Defined Function For Enterting Attendance And Checking Attendance

def att():
    o=int(input("1.Update Attendance [1] \t2.Check Attendance [2] \n"))
    if o==1:
        d=input("Enter Date: ")
        ab=input("Enter Roll Numbers: ")
        data=(d,ab)
        sql='insert into attdance values (%s,%s)'
        c=con.cursor()                                                          # Creating Cursor Object
        c.execute(sql,data)                                                     # To Execute SQL Statement
        con.commit()                                                            # To Save Data In Database
        print("Data Successfully Entered")
        main()
    else:
        sql='select * from attdance'
        c=con.cursor()                                                          # Creating Cursor Object
        c.execute(sql)                                                          # To Execute SQL Statement
        d=c.fetchall()
        for i in d:
            print(i)
        main()
        
def students():
    o=int(input ("1.Update details [1] \t2.Check details [2] \n"))
    if o==1:
          r=input("Enter Student Roll: ")
          n=input("Enter Student Name: ")
          p=input("Enter Phone: ")
          a=input("Enter Address: ")
          data=(r,n,p,a)
          sql= 'insert into students values(%s,%s,%s,%s)'
          c=con.cursor()                                                        # Creating Cursor Object
          c.execute(sql,data)                                                   # To Execute SQL Statement
          con.commit()                                                          # To Save Data In Database
          print("Data Successfully Entered")
          main()
    else:
        sql='select * from students'
        c=con.cursor()                                                          # Creating Cursor Object
        c.execute(sql)                                                          # To Execute SQL Statement
        d=c.fetchall()
        for i in d:
            print(i)
        main()

# User Defined Function For Enterting Class Inventory And Checking Inventory

def inven():
    o=int(input ("1.Update Inventory [1] \t2.Check details [2]\n"))
    if o==1:
        #x=input('Ente the options below to update:\n [1] Benches\n [1] Teachers Table\n [1] Fans\n [1] Lights\n [1] Display Board\n [1] Black Board\n [1] Cupboard\n  :')
          a=input("Enter No. Of Benches: ")
          s=input("Enter No. Of Teaches Table: ")
          d=input("Enter No. Of Fans: ")
          f=input("Enter No. Of Lights: ")
          g=input("Enter No. Of Display Board: ")
          h=input("Enter No. Of Black Board:")
          j=input("Enter No. Of Cupboard: ")
          l=input("Enter Date Of Updation: ")
          data=(a,s,d,f,g,h,j,l)
          sql= 'insert into inventory values(%s,%s,%s,%s,%s,%s,%s,%s)'
          c=con.cursor()                                                        # Creating Cursor Object
          c.execute(sql,data)                                                   # To Execute SQL Statement
          con.commit()                                                          # To Save Data In Database
          print("Data Successfully Entered")
          main()
    else:
        sql='select * from inventory'
        c=con.cursor()                                                          # Creating Cursor Object
        c.execute(sql)                                                          # To Execute SQL Statement
        d=c.fetchall()                                                          
        L=['Benches:\t\t','Teaches(T):\t\t','Fans:\t\t\t','Lights:\t\t\t','Display(B):\t\t','Black(B):\t\t','Cupboard:\t\t', 'Date Of Updation:\t']
        print()
        for i in d:
            for k in range(len(i)):
                print(L[k],i[k])
            print('\n')
        main()

# User Defined Function For Exiting

def exi():
    print("Exinting!!!...")
    sys.exit(0)

# User Defined Function For Enterting The Choice Of Managment Section

def main():
    print('\n1.Monitor\t\t\t[1] \n2.Report Card\t\t[2] \n3.Attendance\t\t[3] \n4.Students\t\t\t[4]\n5.Inventory\t\t\t[5]\n6.All Marks\t\t\t[6]\n7.Exit\t\t\t\t[7]')
    ch=input("Enter Task No: ")
    while True:
        if ch=='1':
            monitor()
        elif ch=='2':
            marks()
        elif ch=='3':
            att()
        elif ch=='4':
            students()
        elif ch=='5':
            inven()
        elif ch=='6':
            marks_all()
        elif ch=='7':
            exi()
        else:
            print("Wrong choice !!!")
    return -1

# __MAIN__

main()
