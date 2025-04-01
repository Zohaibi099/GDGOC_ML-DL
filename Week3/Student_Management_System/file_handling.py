# file_handling.py

def read_student_data(file_name):
    try:
        with open(file_name, 'r') as file:
            students = file.readlines()
            print("Student Records:")
            for student in students:
                print(student.strip())
            return len(students)
    except FileNotFoundError:
        print("File not found.")
        return 0
    except Exception as e:
        print(f"Error reading file: {e}")
        return 0

def write_student_data(file_name, data):
    try:
        with open(file_name, 'w') as file:
            file.writelines(data)
            print("Data successfully written to file.")
    except Exception as e:
        print(f"Error writing to file: {e}")


students_data = ["John Doe, 20, S12345, Math, Science\n", "Jane Doe, 21, S12346, Math, History\n"]
write_student_data("student_output.txt", students_data)
num_students = read_student_data("students.txt")
print("Total number of students:", num_students)
