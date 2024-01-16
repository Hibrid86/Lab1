from datetime import datetime

name = input("What's your name? ")
print(f"Hello {name}")

birth_year = input("What is your YOB? ")
current_year = datetime.now().year
age = current_year - int(birth_year)
print(f"You must be {age} yrs old")

print("Goodbye")