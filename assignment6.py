grades: list[int] = [55, 70, 65, 40, 90, 85, 50, 77]

filtered_grades = list(filter(lambda grade: grade >= 60, grades))
added_bonus_list = list(map(lambda grade: grade + grade * 0.05, filtered_grades))

print("Grades after filtering and applying bonus: ", added_bonus_list)