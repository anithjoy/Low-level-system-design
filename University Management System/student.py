
class Student:
    def __init__(self, student_id, name, age, major):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.major = major
        self.courseList = {} # key - courseId, value - grades

        def student_enroll_course(self, courseId):
            if courseId in self.courseList:
                raise ValueError("Student already enrolled in course")
            self.courseList[courseId] = None

        def student_drop_course(self, courseId):
            if courseId not in self.courseList:
                raise ValueError("Student not enrolled in course")
            del self.courseList[courseId]

        def view_all_grades(self):
            if not self.courseList:
                print("Student {self.name} didnt enrolled to any courses")
                return 
            return self.courseList
        
        def view_courseId_grade(self, courseId):
            if courseId not in self.courseList:
                raise ValueError("Student not enrolled in course")
            return self.courseList[courseId]

