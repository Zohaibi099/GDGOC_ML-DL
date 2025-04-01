class StudentList:
    def __init__(self, students):
        self.students = students
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.students):
            raise StopIteration
        student = self.students[self.index]
        self.index += 1
        return student

def attendance_generator(student_names):
    for student in student_names:
        yield f"{student}: {'Present' if random.choice([True, False]) else 'Absent'}"

def random_marks_generator(student_names):
    for student in student_names:
        yield f"{student}: {random.randint(50, 100)}"

# Example Usage
students = ["Alice", "Bob", "Charlie"]
student_iterator = StudentList(students)
for student in student_iterator:
    print(student)

for attendance in attendance_generator(students):
    print(attendance)

for marks in random_marks_generator(students):
    print(marks)
