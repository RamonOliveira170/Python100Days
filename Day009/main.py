programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected",
                          "Function": "A piece of code that you can easily call over and over again",
                          "Loop": "The action of doing something over and over again",
}

print(programming_dictionary["Bug"])

programming_dictionary["Color"] = "Red color"

print(programming_dictionary)

empty_dictionary = {}

programming_dictionary["Bug"] = "An insect in your computer"

print(programming_dictionary)

for thing in programming_dictionary:
    print(thing)
    print(programming_dictionary[thing])

student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

for student in student_scores:
    if student_scores[student] <= 70:
        student_grades[student] = "Fail"

    elif student_scores[student] <= 80:
        student_grades[student] = "Acceptable"

    elif student_scores[student] <= 90:
        student_grades[student] = "Exceeds Expectations"

    elif student_scores[student] <= 100:
        student_grades[student] = "Outstanding"
