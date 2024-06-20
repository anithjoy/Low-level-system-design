

class Instructor:
    def __init__(self, instructor_id, name, department=None):
        self.instructor_id = instructor_id
        self.name = name
        self.department = department
        self.courseList = {} # key - courseId, value - course


    def assign_course(self, courseId,course):
        if courseId in self.courseList:
            raise ValueError("Instructor already assigned to course")
        
        self.courseList[courseId] = course

    def remove_course(self, courseId):
        if courseId not in self.courseList:
            raise ValueError("Instructor not assigned to course")
        del self.courseList[courseId]

    def view_couseList(self):
        if not self.courseList:
            print(f"Instructor {self.name} didnt assigned to any courses")
            return
        
        return self.courseList
    
    def view_students_of_course(self, courseId):
        if courseId not in self.courseList:
            raise ValueError("Instructor not assigned to course")
        
        return self.courseList[courseId].get_all_students()

        