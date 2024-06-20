class Course:
    def __init__(self, course_id, name, instrutor = None):
        self.course_id = course_id
        self.name = name
        self.instrutor = instrutor  # Instructor id
        self.studentList = {} # key - Sid, Value - grades

        def get_all_students(self):
            if not self.studentList:
                print("No students enrolled in this course")
                return
            return self.studentList
        

        def assign_grades(self, instructorId, studentId, grades):
            if instructorId != self.instructor:
                raise ValueError("Instructor not assigned to this course")
            
            if studentId not in self.studentList:
                raise ValueError("Student not assigned to this course")
            
            if grades not in "ABCD":
                raise ValueError(f"Invalid Grades {grades}")
            
            self.studentList[studentId] = grades
            
        def get_student_grade(self, studentId):
            if studentId not in self.studentList:
                raise ValueError("Student not assigned to this course")
            return self.studentList[studentId]
        

        def assign_instructor(self, instructorId):
            if self.instructor and  self.instructor == instructorId:
                raise ValueError("Instructor already assigned to this course")
            
            self.instructor = instructorId
            

        def remove_instructor(self):
            if not self.instructor:
                raise ValueError("Course is already empty")
            self.instructor = None
            
