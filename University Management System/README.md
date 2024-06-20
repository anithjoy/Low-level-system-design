# University Management System

## Problem Statement

Design a low-level system for managing a university's operations, focusing on the following core components:

### Student Management

- Each student has a unique ID, name, age, and major.
- Students can enroll in courses.
- Students can view their enrolled courses and grades.

### Course Management

- Each course has a unique course code, name, and instructor.
- Courses can have a list of enrolled students.
- Courses can assign grades to students.

### Instructor Management

- Each instructor has a unique ID, name, and department.
- Instructors can teach multiple courses.
- Instructors can view the list of courses they teach and the students enrolled in each course.

### University Administration

- Ability to add/remove students.
- Ability to add/remove courses.
- Ability to assign/remove instructors to/from courses.

## Requirements

### Classes and Attributes

- Define classes for `Student`, `Course`, `Instructor`, and `University`.
- Each class should have appropriate attributes to store the required information.

### Methods

- Methods for enrolling a student in a course.
- Methods for assigning/removing instructors to/from courses.
- Methods for adding/removing students and courses.
- Methods for viewing enrolled courses and grades for a student.
- Methods for instructors to view the list of courses they teach and the students in each course.
- Methods for assigning grades to students in a course.

### Relationships

- A student can enroll in multiple courses.
- A course can have multiple students.
- An instructor can teach multiple courses.
- A course can have one instructor.

### Constraints

- Ensure that a student cannot enroll in the same course multiple times.
- Ensure that grades can only be assigned to students enrolled in the course.
- Ensure that instructors can only view and manage the courses they are assigned to.

## Example Scenarios

### Adding a Student

- Create a new student with a unique ID, name, age, and major.
- Add the student to the university system.

### Enrolling in a Course

- Enroll a student in a specific course.
- Check if the student is already enrolled in the course.

### Assigning an Instructor

- Assign an instructor to a specific course.
- Ensure that the instructor can view the list of students enrolled in the course.

### Viewing Grades

- Allow a student to view their grades for the courses they are enrolled in.
- Allow an instructor to assign and view grades for their courses.

## Implementation

Design and implement the classes and methods needed to fulfill the requirements outlined above. Ensure that your code is modular, maintainable, and adheres to object-oriented principles.
