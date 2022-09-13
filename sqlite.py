import sqlite3
from employee import Employee

conn = sqlite3.connect('employee_list.db')

c = conn.cursor()

# c.execute("""CREATE TABLE First (
#             first text,
#             last text,
#             pay integer,
#             unique (first)
#             )""")


def insert_emp(emp):
    with conn:
        c.execute("INSERT INTO First VALUES (:first, :last, :pay)", {'first': emp.first, 'last': emp.last, 'pay': emp.pay})


def get_emps_by_name(lastname):
    c.execute("SELECT * FROM First WHERE last=:last", {'last': lastname})
    return c.fetchall()


def update_pay(emp, pay):
    with conn:
        c.execute("""UPDATE First SET pay = :pay
                    WHERE first = :first AND last = :last""",
                  {'first': emp.first, 'last': emp.last, 'pay': pay})


def remove_emp(emp):
    with conn:
        c.execute("DELETE from First WHERE first = :first AND last = :last",
                  {'first': emp.first, 'last': emp.last})

emp_1 = Employee('John', 'Doe', 80000)
emp_2 = Employee('Jane', 'Stanley', 90000)
emp_3 = Employee('Sakshi', 'Utturi', 100000)
emp_4 = Employee('Sneha', 'Patil', 120000)

# insert_emp(emp_1)
# insert_emp(emp_2)
insert_emp(emp_3)
# insert_emp(emp_4)


# emps = get_emps_by_name('Doe')
# print(emps)
# emps = get_emps_by_name('Jane')
# print(emps)



# emps = get_emps_by_name('Sakshi')
# print(emps)
# emps = get_emps_by_name('Sneha')
# print(emps)

# update_pay(emp_2, 95000)
# remove_emp(emp_3)

conn.commit()
conn.close()