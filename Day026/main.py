numbers_list = [1, 2, 3]
new_list = [number * 5 for number in numbers_list]

print(new_list)

name = "ronaldo"
letters_list = [letter for letter in name]

print(letters_list)

range_list = [number * 2 for number in range(1, 5)] #Excludes the last item

print(range_list)

names = ["Amanda", "Caroline", "Elton", "Thanos", "Valentina", "Eddy"]
short_names = [n for n in names if len(n) < 6]

print(short_names)

upper_case_names = [n.upper() for n in names if len(n) > 5]

print(upper_case_names)

import random
student_scores = {student:random.randint(50, 100) for student in names}

print(student_scores)

passed_students = {student:True for (student, score) in student_scores.items() if score > 75}

print(passed_students)

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

#Looping through dictionaries
#for (key, value) in student_dict.items():
#    print(value)

import pandas
student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

#Looping through data frame
#for (key, value) in student_data_frame.items():
#    print(value)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    print(row)
    print(row.student)
    if row.student == "Angela":
        print(f"SCORE: {row.score}")
