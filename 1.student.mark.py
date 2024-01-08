class_a = {
    "number_of_students": 0,
    "student_info": {},
    "number_of_courses": 0,
    "course_info": {}
}

#Input functions
#Input number of students in a class and student information
def get_student_info():
    class_a["number_of_students"] = int(input("\nPlease enter the numbers of student: "))
    for i in range(class_a["number_of_students"]):
        print(f"\n Student {i+1} info:")
        name = input("Enter student name: ")
        student_id = input("Enter student id: ")
        DoB = input("Enter student Date of Birth (DD/MM/YYYY): ")
        class_a["student_info"][student_id] = {"name": name, "DoB": DoB}

#Input number of courses and course information
def get_course_info():
    class_a["number_of_courses"] = int(input("\nPlease enter the numbers of course: "))
    for i in range(class_a["number_of_courses"]):
        print(f"\n Course {i+1} info:")
        name = input("Enter the course name: ")
        course_id = input("Enter the course id: ")
        class_a["course_info"][course_id] = {"name": name, "student_mark": {}}

#Select a course, input marks for student in this course
def get_student_mark():
    add_check = int(input("\nDo you want to add mark (0/1): "))
    while add_check == 1:
        course_id = input("\nEnter course id to add student mark: ")
        n = int(input("Enter number of student marks you want to add: "))
        for i in range(n):
            student_id = input(f"Enter student {i+1} id: ")
            mark = float(input(f"Enter student {i+1} mark: "))  
            class_a["course_info"][course_id]["student_mark"][student_id] = mark
        add_check = int(input("\nDo you want to add more mark (0/1): "))

#Listing functions
#List courses
def list_courses():
    print("\nList of Courses:")
    for course_id, course_data in class_a["course_info"].items():
        print(f"Course ID: {course_id} - Course Name: {course_data['name']}")

#List students
def list_students():
    print("\nList of Students:")
    for student_id, student_data in class_a["student_info"].items():
        print(f"Student Name: {student_data['name']}\n \tID: {student_id}\n \tDoB: {student_data['DoB']}")
        
#Show student marks for a given course
def show_student_marks():
    show_check = int(input("\nDo you want to show student marks for a given course (0/1): "))
    while show_check == 1:
        course_id = input("\nEnter course id to show student marks: ")
        print("\nStudent Marks for Course:", class_a["course_info"][course_id]["name"])
        for student_id, mark in class_a["course_info"][course_id]["student_mark"].items(): 
            student_data = class_a["student_info"][student_id]
            print(f"Student Name: {student_data['name']}\n \tID: {student_id}\n \tMark: {mark}")
        show_check = int(input("\nDo you want to show student marks for a other given course (0/1): "))

#Example
get_student_info()
get_course_info()
get_student_mark()
list_courses()
list_students()
show_student_marks()