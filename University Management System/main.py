from university import University
from student import Student
from instructor import Instructor
from course import Course

# Doesnt work, I have to fix it. 



# Initialize University
university = University("Example University")

# Create Students
student1 = Student("S1", "Alice", 20, "Computer Science")
student2 = Student("S2", "Bob", 22, "Mechanical Engineering")

# Create Instructors
instructor1 = Instructor("I1", "Dr. Smith", "Computer Science")
instructor2 = Instructor("I2", "Dr. Brown", "Mechanical Engineering")

# Create Courses
course1 = Course("CSE101", "Introduction to Computer Science")
course2 = Course("ME101", "Introduction to Mechanical Engineering")

# Add students, instructors, and courses to university
university.add_student(student1)
university.add_student(student2)
university.add_instructor(instructor1)
university.add_instructor(instructor2)
university.add_course(course1)
university.add_course(course2)

# Assign instructors to courses
course1.assign_instructor(instructor1)
course2.assign_instructor(instructor2)

# Students enroll in courses
student1.enroll_course(course1)
student2.enroll_course(course2)

# Instructor assigns grades
course1.assign_grade(student1, 'A')
course2.assign_grade(student2, 'B')

# View student's grades
student1.view_grades()
student2.view_grades()

# Instructor views courses and students
instructor1.view_courses()
instructor1.view_students(course1)

instructor2.view_courses()
instructor2.view_students(course2)

