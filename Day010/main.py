def format_name(name, surname):
    """Take the first and last name and format it to return the title case version of the name."""
    if name == "" or surname == "":
        return "You did not provide valid inputs"
    formated_name = name.title()
    formated_surname = surname.title()
    return f"Result: {formated_name} {formated_surname}"


fullname = format_name(input("What is your first name?: "), input("What is your last name?: "))

print(fullname)

def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


print(is_leap_year(1700))
