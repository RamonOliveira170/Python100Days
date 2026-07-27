fruits = ["Apple", "Peach", "Pear"]

for fruit in fruits:
    print(fruit)
    print(fruit + " pie")

student_scores = [149, 539, 240, 850, 124, 186, 473, 252, 89, 284, 653, 489]

total_exam_score = sum(student_scores)
print(f"total exam score: {total_exam_score}")

max_exam_score = max(student_scores)
print(f"Highest score: {max_exam_score}\n")

sum = 0
highest = 0
for score in student_scores:
    sum += score
    if score > highest:
        highest = score

print(f"sum: {sum}")
print(f"highest {highest}\n")

gauss = 0
for number in range(1, 101):
    gauss += number

print(gauss)
