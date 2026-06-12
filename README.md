College Management System (DBMS Project)
Project Overview

The College Management System is a database-driven web application designed to manage college operations such as student records, faculty details, courses, departments, enrollment, and attendance. The system demonstrates CRUD operations, stored procedures, and triggers using a structured database.

Database Tables
Student
student_id
name
department_id
year
email
Faculty
faculty_id
name
department_id
designation
Department
department_id
department_name
Course
course_id
course_name
credits
department_id
Enrollment
enrollment_id
student_id
course_id
semester
grade
Attendance
attendance_id
student_id
course_id
attendance_percentage
Functional Requirements (Frontend Demonstration)
Insert Operation

Add new student, faculty, course, department, enrollment, and attendance records.

Update Operation

Modify existing records such as student details, faculty data, grades, and attendance.

Delete Operation

Remove student, faculty, or course records from the system.

Display Records

View all stored data in tabular format for each module.

Stored Procedure Execution

Execute predefined SQL stored procedures for efficient database operations.

Trigger Demonstration Scenario

Automatic actions triggered on database events such as logging updates when student data is modified.

Technologies Used
Python (Flask / Backend)
HTML (Frontend)
CSS (Styling)
MySQL (Database)
SQL (Queries, Stored Procedures, Triggers)
Git & GitHub (Version Control)
Project Modules
Student Module
Faculty Module
Department Module
Course Module
Enrollment Module
Attendance Module
How to Run the Project
Clone the repository
git clone https://github.com/your-username/College-Management-System.git
Navigate to project folder
cd College-Management-System
Install dependencies (if Flask is used)
pip install flask
Run the application
python app.py
Open browser
http://127.0.0.1:5000/
Conclusion

This project demonstrates a complete DBMS-based College Management System implementing real-world database operations such as CRUD, stored procedures, and triggers along with a simple web interface.
