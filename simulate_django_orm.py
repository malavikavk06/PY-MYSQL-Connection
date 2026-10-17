import mysql.connector

conn=mysql.connector.connect(host="localhost",user="root",password="root",database="DjangoORM")
cur=conn.cursor()
# print("connection created")

# cur.execute("CREATE DATABASE DjangoORM")
# print("Database created")

# cur.execute('''CREATE TABLE employee
#               (id int primary key auto_increment,
#                name varchar(20),
#                designation varchar(30),
#                salary decimal(10,2)
#            )''')
# print("table created")

class Employee:
    def create(self,*args,**kwargs):
        cols=""
        placeholder=""
        for col in kwargs.keys():
            if cols!="":
                cols+=','
                placeholder+=','
            cols+=col
            placeholder+="%s"
        values=tuple(kwargs.values())
        print(f"insert into employee({cols}) values({placeholder}),{values}")
        query=f"insert into employee({cols}) values({placeholder})"
        print(query)
        cur.execute(query,values)
        conn.commit()

    def list(self,*args,**kwargs):
        cur.execute("SELECT * FROM employee")
        # for emp in employee:
        #     print(emp)
        print(cur.fetchall())

    def retrieve(self,*args,**kwargs):
        for key in kwargs:
            cur.execute(f"SELECT * FROM employee where {key}={kwargs.get(key)}")
            print(cur.fetchall())
        
    def update(self,*args,**kwargs):
        print(args,kwargs)
        for key in kwargs:
            print(f"Update employee SET {key}={kwargs.get(key)} WHERE id={args[0]}")
            cur.execute(f"Update employee SET {key}='{kwargs.get(key)}' WHERE id={args[0]}")
            conn.commit()

    def delete(self,*args,**kwargs):
        cur.execute(f"DELETE from employee WHERE id={args[0]}")
        conn.commit()

    def filter(self,*args,**kwargs):
        for key in kwargs:
            cur.execute(f"SELECT * FROM employee WHERE {key}='{kwargs.get(key)}'")
            print(cur.fetchall())

employee=Employee()

while True:

    print("1.Create employee")
    print("2.List all employee")
    print("3.Employee details view")
    print("4.Update employee")
    print("5.Delete employee")
    print("6.Filter")
    print("7.Exit")

    choice=int(input("Enter your choice:"))
    if choice==1:
        name=input("Enter the employee name:")
        desig=input("Enter the designation:")
        salary=float(input("Enter the salary:"))
        employee.create(name=name,designation=desig,salary=salary)
        print("======================")

    elif choice==2:
        employee.list()
        print("======================")

    elif choice==3:
        id=int(input("enter  the employee id:"))
        employee.retrieve(id=id)
        employee.retrieve()
        print("======================")

    elif choice==4:
        id=int(input("Enter the id:"))
        print("Update")
        print("1.Update employee name")
        print("2.Update employee designation")
        print("3.Update employee salary")
        choice=input("Enter your choice to update:")
        if choice=="1":
            name=input("Enter the new name:")
            employee.update(id,name=name)
        elif choice=="2":
            desig=input("Enter the new designation:")
            employee.update(id,designation=desig)
        elif choice=="3":
            salary=input("Enter the new salary:")
            employee.update(id,salary=salary)
            break
        else:
            print("Invalid choice")
            print("======================")

    elif choice==5:
        id=int(input("Enter the employee id:"))
        employee.delete(id)
        print("======================")

    elif choice==6:
        print("Filter")
        print("1.Filter by name:")
        print("2.Filter by designation:")
        print("3.Filetr by salary:")
        choice=input("Enter your choice to filter:")
        if choice=="1":
            name=input("Enter the name:")
            employee.filter(name=name)

        elif choice=="2":
            desig=input("Enter the designation:")
            employee.filter(designation=desig)

        elif choice=="3":
            salary=float(input("Enter the salary:"))
            employee.filter(salary=salary)
        print("======================")

    elif choice==7:
        break
        print("======================")

    else:
        print("Invalid choice")

conn.close()
print("connection closed")
print("bye")

