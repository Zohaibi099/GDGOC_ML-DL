# SMS.py - Object-Oriented Student Management System

class Student:
    def __init__(self, name, age, student_id, courses):
        self.name = name
        self.age = age
        self.student_id = student_id
        self.courses = courses  # List of (course, grade)

    def get_details(self):
        return f"Student: {self.name}, Age: {self.age}, ID: {self.student_id}, Courses: {self.courses}"

    def set_details(self, name=None, age=None, student_id=None, courses=None):
        if name:
            self.name = name
        if age:
            self.age = age
        if student_id:
            self.student_id = student_id
        if courses:
            self.courses = courses

    def calculate_gpa(self):
        if not self.courses:
            return 0.0
        total_points = sum(grade for _, grade in self.courses)
        return round(total_points / len(self.courses), 2)

class GraduateStudent(Student):
    def __init__(self, name, age, student_id, courses, thesis_title):
        super().__init__(name, age, student_id, courses)
        self.thesis_title = thesis_title

    def __str__(self):
        return f"{super().get_details()}, Thesis: {self.thesis_title}"

# Example Usage
student = Student("Alice", 21, "S1001", [("Math", 85), ("Science", 90)])
grad_student = GraduateStudent("Bob", 24, "G2002", [("AI", 88), ("ML", 92)], "Deep Learning")

print(student.get_details())
print(f"GPA: {student.calculate_gpa()}")
print(grad_student)
