# file_handling.py - Read & Write Student Data

def read_students(filename):
    try:
        with open(filename, "r") as file:
            students = file.readlines()
            print("Student Records:")
            for student in students:
                print(student.strip())
            print(f"Total Students: {len(students)}")
    except FileNotFoundError:
        print("Error: File not found!")
    except Exception as e:
        print(f"Error while reading file: {e}")

def write_students(filename, students):
    try:
        with open(filename, "w") as file:
            for student in students:
                file.write(student + "\n")
        print(f"Successfully wrote to {filename}")
    except Exception as e:
        print(f"Error writing file: {e}")

# Example Usage
students_list = ["Zohaib, 21, S1001, Math, Science", "Rahat, 24, G2002, AI, ML"]
write_students("student_output.txt", students_list)
read_students("student_output.txt")
