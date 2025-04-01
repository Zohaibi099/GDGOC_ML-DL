from student_utils.arithmetic import calculate_percentage, grade_classification
from student_utils.attendance import calculate_attendance
from student_utils.performance import evaluate_performance
percentage = calculate_percentage(100, 85)
grade = grade_classification(percentage)
attendance = calculate_attendance(30, 28)
performance = evaluate_performance(3.7)

print(f"Percentage: {percentage}%")
print(f"Grade: {grade}")
print(f"Attendance: {attendance}%")
print(f"Performance: {performance}")
