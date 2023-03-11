
def is_email_valid(func):
    def wrapper(email, y, a, z):
        if "@" in email:
            if "." in email.split("@")[1]:
                func(email, y, a, z)
            else:
                print("Email invalid without dot!!!!")
        else:
            print("Email invalid without @ !!!!")
    return wrapper

def is_phone_valid(fun):
    def wrap(email, y, a, phone):
        numbers = str(phone)
        if numbers.startswith('+') and len(numbers) == 13:
            fun(email, y, a, phone)
        else:
            print("Telephone is invalid! Must start with + and contains 13 numbers!")
    return wrap
