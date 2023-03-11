from helpers import save, get_all_employers, get_employee_by_email


while True:
    print("1.Add new Employee\n2.Get all Employees\n3.Get employee by email")
    flag = input("Choose menu item: ")
    if flag == "1":
        email = input("Employee email: ")
        first_name = input("Employee first name: ")
        last_name = input("Employee last name: ")
        phone_number = input("Employee phone number: ")
        save(email, first_name, last_name, phone_number)
    elif flag == "2":
        get_all_employers()
    elif flag == "3":
        email_to_find = input("Type email of employee which you want to find: ")
        get_employee_by_email(email_to_find)
