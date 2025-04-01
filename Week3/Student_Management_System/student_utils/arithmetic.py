

def calculate_percentage(total_marks, obtained_marks):
    if total_marks == 0:
        return 0
    return (obtained_marks / total_marks) * 100

def grade_classification(percentage):
    if percentage >= 90:
        return "A"
    elif percentage >= 80:
        return "B"
    elif percentage >= 70:
        return "C"
    elif percentage >= 60:
        return "D"
    else:
        return "F"
