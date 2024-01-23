# task 1 
from Student import Student
from Teacher import Teacher
from DepartmentHead import DepartmentHead

student = Student("John", 20, True, 2)
teacher = Teacher("Jane", 35, False, 8)
department_head = DepartmentHead("Jack", 40, True, 10, "Computer Science")

print(f"\nStudent {student}")
print(f"\nTeacher {teacher}")
print(f"\nDepartment Head {department_head}")

student.set_course(3)
teacher.set_experience(9)
department_head.set_department("English")

print("\nUpdated information: ")
print(f"Student {student.get_name()} course {student.get_course()}")
print(f"Teacher {teacher.get_name()} experience {teacher.get_experience()}")
print(f"Department Head {department_head.get_name()} department {department_head.get_department()}")

