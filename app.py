from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="019283",
    database="college_management"
)

cursor = db.cursor()

@app.route('/')
def home():

    cursor.execute("SELECT * FROM Student")
    students = cursor.fetchall()

    cursor.execute("SELECT COUNT(*) FROM Student")
    student_count = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM Faculty")
    faculty_count = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM Course")
    course_count = cursor.fetchone()[0]

    cursor.execute("SELECT AVG(attendance_percentage) FROM Attendance")
    attendance = cursor.fetchone()[0]

    return render_template(
        'index.html',
        students=students,
        student_count=student_count,
        faculty_count=faculty_count,
        course_count=course_count,
        attendance=round(attendance, 2)
    )

@app.route('/add', methods=['POST'])
def add():
    sid = request.form['sid']
    name = request.form['name']
    dept = request.form['dept']
    year = request.form['year']
    email = request.form['email']

    cursor.execute(
        "INSERT INTO Student VALUES(%s,%s,%s,%s,%s)",
        (sid, name, dept, year, email)
    )

    db.commit()

    return "Student Added Successfully"


@app.route('/students')
def students_page():

    cursor.execute("SELECT * FROM Student")
    students = cursor.fetchall()

    return render_template(
        'students.html',
        students=students
    )


@app.route('/faculty')
def faculty_page():

    cursor.execute("SELECT * FROM Faculty")
    faculty = cursor.fetchall()

    return render_template(
        'faculty.html',
        faculty=faculty
    )


@app.route('/courses')
def courses_page():

    cursor.execute("SELECT * FROM Course")
    courses = cursor.fetchall()

    return render_template(
        'courses.html',
        courses=courses
    )
@app.route('/delete/<int:id>')
def delete_student(id):

    cursor.execute(
        "DELETE FROM Student WHERE student_id=%s",
        (id,)
    )

    db.commit()

    return '''
    <h2>Student Deleted Successfully</h2>
    <a href="/students">Back to Students</a>
    '''
@app.route('/update/<int:id>')
def update_student(id):

    cursor.execute(
        "UPDATE Student SET year = year + 1 WHERE student_id=%s",
        (id,)
    )

    db.commit()

    return '''
    <h2>Student Updated Successfully</h2>
    <a href="/students">Back to Students</a>
    '''

if __name__ == '__main__':
    app.run(debug=True)