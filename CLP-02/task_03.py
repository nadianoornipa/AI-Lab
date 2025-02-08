def sort_students(students):
    return sorted(students, key=lambda x: x[2])

students = [("Nadia", 23, 85), ("Shahan", 18, 90), ("Rahi", 19, 80)]
print(sort_students(students))
