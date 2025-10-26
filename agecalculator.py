from datetime import date

birth_day = int(input("Enter your birth day: "))
birth_month = int(input("Enter your birth month: "))
birth_year = int(input("Enter your birth year: "))

today = date.today()
age = today.year - birth_year
if (today.month, today.day) < (birth_month, birth_day):
    age -= 1

print(f"Your age is {age} years")