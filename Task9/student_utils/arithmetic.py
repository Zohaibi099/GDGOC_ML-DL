# arithmetic.py - Percentage and Grade Calculation

def calculate_percentage(marks_obtained, total_marks):
    return round((marks_obtained / total_marks) * 100, 2)

def grade_classification(percentage):
    if percentage >= 90:
        return "A"
    elif percentage >= 80:
        return "B"
    elif percentage >= 70:
        return "C"
    else:
        return "D"
