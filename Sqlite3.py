import sqlite3 as db
conn=db.connect("demo.db")


data=conn.execute('''delete from emp 
            where id=22''')
conn.commit()

data=conn.execute("select * from emp")

for row in data:
    print("ID:",row[0])
    print("Name:",row[1])
    print("Salary:",row[2])
    print("Age:",row[3])
    print("city:",row[4])
                        




conn.close()
