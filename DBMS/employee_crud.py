from db import get_connection

def add_employee():
    conn = get_connection()
    cursor = conn.cursor()

    name = input("Enter Name: ")
    department = input("Enter Department: ")
    salary = float(input("Enter Salary: "))

    sql = """
    INSERT INTO employee
    (name, department, salary)
    VALUES (%s, %s, %s)
    """

    values = (name, department, salary)

    cursor.execute(sql, values)

    conn.commit()

    print("Employee Added Successfully!")

    cursor.close()
    conn.close()

from db import get_connection



def view_employees():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM employee")

    records = cursor.fetchall()

    print("\nEmployees")

    for row in records:
        print(row)

    cursor.close()
    conn.close()

def update_employee():
    conn = get_connection()
    cursor = conn.cursor()

    employee_id = int(input("Enter Employee ID: "))
    salary = float(input("Enter New Salary: "))

    sql = """
    UPDATE employee
    SET salary=%s
    WHERE id=%s
    """

    values = (salary, employee_id)

    cursor.execute(sql, values)

    conn.commit()

    print("Updated Successfully")

    cursor.close()
    conn.close()

def delete_employee():
    conn = get_connection()
    cursor = conn.cursor()

    employee_id = int(input("Enter Employee ID: "))

    sql = """
    DELETE FROM employee
    WHERE id=%s
    """

    cursor.execute(sql, (employee_id,))

    conn.commit()

    print("Deleted Successfully")

    cursor.close()
    conn.close()

def menu():
    while True:
        print()
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Update Employee")
        print("4. Delete Employee")
        print("5. Exit")

        choice = input("Enter Choice: ")

        if choice == "1":
            add_employee()

        elif choice == "2":
            view_employees()

        elif choice == "3":
            update_employee()

        elif choice == "4":
            delete_employee()

        elif choice == "5":
            print("Thank You")
            break

        else:
            print("Invalid Choice")

menu()