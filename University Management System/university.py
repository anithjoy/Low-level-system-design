from student import Student
from course import Course
from instructor import Instructor

class University:
    def __int__(self, name):
        self.name = name
        self.students = {}
        self.courses = {}
        self.instructors = {}
        print(f"self.name {self.name}")

    # Students 

    def add_student(self, student_id, name, age, major):
        if student_id in self.students:
            raise ValueError('Student already existed')
        self.students[student_id] = Student(student_id, name, age, major)

    def remove_student(self, student_id):
        if student_id not in self.students:
            raise ValueError('Student not existed')
        del self.students[student_id]

    # def student_enroll_course(self,student_id,course_id):
    #     if student_id not in self.students:
    #         raise ValueError('Student not existed')
    #     if course_id not in self.courses:
    #         raise ValueError('Course not existed')
        
    #     student = self.students[student_id]
    #     student.student_enroll_course(course_id)
    #     print(f"student{student.name} enrolled in course {self.courses[course_id].name}")




    def add_course(self, course_id, name, instructor = None):
        if course_id in self.courses:
            raise ValueError('Course already existed')
        self.courses[course_id] = Course(course_id, name, instructor)

    def remove_course(self, course_id):
        if course_id not in self.courses:
            raise ValueError('Course not existed')
        del self.courses[course_id]




    def add_instructor(self, instructor_id, name, department=None):
        if instructor_id in self.instructors:
            raise ValueError('Instructor already existed')
        self.instructors[instructor_id] = Instructor(instructor_id, name, department)

    def remove_instructor(self, instructor_id):
        if instructor_id not in self.instructors:
            raise ValueError('Instructor not existed')
        del self.instructors[instructor_id]

    

    