import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="staff_records"
    )

def insert_employee(name, email, role, salary):
    db = get_connection()
    cursor = db.cursor()
    query = "INSERT INTO employees (name, email, position, salary) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (name, email, role, salary))
    db.commit()
    print("Employee added successfully.")
    cursor.close()
    db.close()

def delete_employee(employee_id):
    db = get_connection()
    cursor = db.cursor()
    query = "DELETE FROM employees WHERE id = %s"
    cursor.execute(query, (employee_id,))
    db.commit()
    print("Employee deleted successfully.")
    cursor.close()
    db.close()

def update_employee(employee_id, new_role, new_salary):
    db = get_connection()
    cursor = db.cursor()
    query = "UPDATE employees SET position = %s, salary = %s WHERE id = %s"
    cursor.execute(query, (new_role, new_salary, employee_id))
    db.commit()
    print("Employee updated successfully.")
    cursor.close()
    db.close()

def show_all_employees():
    db = get_connection()
    cursor = db.cursor()
    query = "SELECT * FROM employees"
    cursor.execute(query)
    employees = cursor.fetchall()
    for employee in employees:
        print(f"ID: {employee[0]}, Name: {employee[1]}, Email: {employee[2]}, Position: {employee[3]}, Salary: {employee[4]}")
    cursor.close()
    db.close()

def menu():
    while True:
        print("\nEmployee Management System")
        print("1 - Add Employee")
        print("2 - Remove Employee")
        print("3 - Promote Employee")
        print("4 - Display Employee List")
        print("5 - Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter employee name: ")
            email = input("Enter employee email: ")
            role = input("Enter employee role: ")
            salary = float(input("Enter employee salary: "))
            insert_employee(name, email, role, salary)

        elif choice == '2':
            employee_id = int(input("Enter the ID of the employee to remove: "))
            delete_employee(employee_id)

        elif choice == '3':
            employee_id = int(input("Enter the ID of the employee to promote: "))
            new_role = input("Enter the new role: ")
            new_salary = float(input("Enter the new salary: "))
            update_employee(employee_id, new_role, new_salary)

        elif choice == '4':
            show_all_employees()

        elif choice == '5':
            print("Goodbye! you exited the menu")
            break

        else:
            print("Invalid choice, please try again.")

menu()
