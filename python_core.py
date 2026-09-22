# match/case
day = 2

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case _:
        print("Other day")

#  Variable Scope

name = "Khushi"   # Global variable


def greet():
    message = "Hello"   # Local variable
    print(message)
    print(name)


greet()

#  *args

def add_numbers(*args):
    total = 0

    for number in args:
        total += number

    return total


result = add_numbers(10, 20, 30, 40)
print("Sum:", result)

#  **kwargs

def show_details(**kwargs):
    print(kwargs)


show_details(name="Khushi", course="CSE", year=3)


# Lists

numbers = [10, 20, 30, 40, 50]

print("List:", numbers)
print("First element:", numbers[0])
print("Last element:", numbers[-1])

numbers.append(60)
print("After append:", numbers)

numbers.remove(20)
print("After remove:", numbers)

print("Slicing:", numbers[1:4])


# Tuples

student = ("Khushi", 3, "CSE")

print("Tuple:", student)
print("Name:", student[0])
print("Course:", student[2])


# Sets

numbers_set = {10, 20, 20, 30, 30, 40}

print("Set:", numbers_set)

numbers_set.add(50)
print("After add:", numbers_set)

numbers_set.remove(10)
print("After remove:", numbers_set)


#  Dictionaries

student_info = {
    "name": "Khushi",
    "course": "CSE",
    "year": 3
}

print("Dictionary:", student_info)
print("Name:", student_info["name"])

student_info["year"] = 3
print("Updated:", student_info)

student_info["university"] = "Quantum University"
print("After adding:", student_info)


# List Comprehensions
# Filter even numbers
even_numbers = [number for number in range(1, 11) if number % 2 == 0]

print("Even numbers:", even_numbers)

#Transform strings
words = ["python", "machine", "learning", "ai"]

uppercase_words = [word.upper() for word in words]

print("Uppercase words:", uppercase_words)


#Flatten a nested list
nested = [[1, 2], [3, 4], [5, 6]]

flattened = [number for group in nested for number in group]

print("Flattened list:", flattened)


#Dictionary Comprehensions

#Character frequency counter
text = "Transfer"

frequency = {char: text.count(char) for char in set(text)}

print("Character frequency:", frequency)


# Swap keys and values
student_marks = {
    "Khushi": 90,
    "Akash": 85,
    "Ayushman": 88
}

swapped = {value: key for key, value in student_marks.items()}

print("Swapped dictionary:", swapped)


# Set Comprehension

emails = [
    "khushi12@gmail.com",
    "ayush02@gmail.com",
    "tanzironezuko809@brave.com",
    "testcomprehension20@yahoo.com"
]

domains = {email.split("@")[1] for email in emails}

print("Unique domains:", domains)