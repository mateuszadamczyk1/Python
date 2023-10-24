student_scores = {
    "Harry": 81,
    "Mark": 76,
    "Draco": 74,
    "Hermione": 99,
    "Stella": 32,
    "Hannah": 66,
}

student_grades = {}

for key in student_scores:
    if student_scores[key] < 70:
        student_grades[key] = "Not good"
    elif student_scores[key] < 80:
        student_grades[key] = "Acceptable"  
    else:
        student_grades[key] = "Good"

print(student_grades)              