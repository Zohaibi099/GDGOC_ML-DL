class Student:
    def __init__(self, name, age, student_id, courses=None):
        self.name = name
        self.age = age
        self.student_id = student_id
        self.courses = courses if courses is not None else []

    
    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_student_id(self):
        return self.student_id

    def get_courses(self):
        return self.courses

   
    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        self.age = age

    def set_student_id(self, student_id):
        self.student_id = student_id

    def set_courses(self, courses):
        self.courses = courses

    
    def calculate_gpa(self, grades):
        if len(grades) == 0:
            return 0
        return sum(grades) / len(grades)

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Student ID: {self.student_id}, Courses: {self.courses}"


student = Student("John Doe", 20, "S12345", ["Math", "Science"])
print(student)
student.set_name("Jane Doe")
student.set_age(21)
student.set_courses(["Math", "History"])
print(student)


grades = [85, 90, 88]
print("GPA:", student.calculate_gpa(grades))




class GraduateStudent(Student):
    def __init__(self, name, age, student_id, courses, thesis_title):
        super().__init__(name, age, student_id, courses)
        self.thesis_title = thesis_title

    def get_thesis_title(self):
        return self.thesis_title

    def set_thesis_title(self, thesis_title):
        self.thesis_title = thesis_title

    def __str__(self):
        return f"{super().__str__()}, Thesis Title: {self.thesis_title}"


grad_student = GraduateStudent("Alice Smith", 24, "G98765", ["Research Methods", "Advanced AI"], "AI in Healthcare")
print(grad_student)



class StudentList:
    def __init__(self, students):
        self.students = students
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.students):
            student = self.students[self.index]
            self.index += 1
            return student
        else:
            raise StopIteration


students = [Student("John Doe", 20, "S12345", ["Math", "Science"]),
            Student("Jane Doe", 21, "S12346", ["Math", "History"])]
student_list = StudentList(students)

for student in student_list:
    print(student)




import random

def attendance_generator(num_days):
    for _ in range(num_days):
        yield random.choice(["Present", "Absent"])

for attendance in attendance_generator(10):
    print(attendance)



def random_marks_generator(num_students):
    for _ in range(num_students):
        yield random.randint(50, 100)

for marks in random_marks_generator(5):
    print(f"Random marks: {marks}")
