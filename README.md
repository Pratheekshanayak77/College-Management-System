# College Management System 

## Project Overview

This is a database-driven College Management System used to manage student, faculty, course, department, enrollment, and attendance data.

---

## Database Tables

### Student Table
**student_id**  
**name**  
**department_id**  
**year**  
**email**

---

### Faculty Table
**faculty_id**  
**name**  
**department_id**  
**designation**

---

### Department Table
**department_id**  
**department_name**

---

### Course Table
**course_id**  
**course_name**  
**credits**  
**department_id**

---

### Enrollment Table
**enrollment_id**  
**student_id**  
**course_id**  
**semester**  
**grade**

---

### Attendance Table
**attendance_id**  
**student_id**  
**course_id**  
**attendance_percentage**

---

## Functional Requirements

### Insert Operation
Add new records for student, faculty, course, department, enrollment, and attendance.

### Update Operation
Modify existing records in all modules.

### Delete Operation
Remove unwanted records from the system.

### Display Records
View all stored records in tabular format.

### Stored Procedure
Execute SQL stored procedures for database operations.

### Trigger
Automatic execution on database events like update logging.

---

## Technologies Used
- Python (Flask)
- HTML
- CSS
- MySQL
- SQL (Stored Procedures, Triggers)
- Git & GitHub

---

## Project Modules
- Student Module  
- Faculty Module  
- Department Module  
- Course Module  
- Enrollment Module  
- Attendance Module  

---

## Conclusion

The College Management System is a database-driven web application designed to simplify and automate the management of college operations. It effectively handles key academic and administrative tasks such as student management, faculty records, course details, department organization, enrollment tracking, and attendance monitoring.

This project demonstrates the practical implementation of important DBMS concepts including CRUD operations (Insert, Update, Delete, Display), stored procedures, and triggers. These features ensure efficient data handling, reduced manual effort, and improved accuracy in record management.

By developing this system, we gain hands-on experience in integrating frontend technologies like HTML and CSS with backend programming using Python Flask, along with database management using MySQL. It also helps in understanding how real-world applications are structured and how data flows between the user interface and the database.

