from flask import Flask, render_template, request, redirect
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
    return render_template('students.html', students=students)

@app.route('/faculty')
def faculty_page():
    cursor.execute("SELECT * FROM Faculty")
    faculty = cursor.fetchall()
    return render_template('faculty.html', faculty=faculty)

@app.route('/courses')
def courses_page():
    cursor.execute("SELECT * FROM Course")
    courses = cursor.fetchall()
    return render_template('courses.html', courses=courses)

@app.route('/delete/<int:id>')
def delete_student(id):
    cursor.execute("DELETE FROM Student WHERE student_id=%s", (id,))
    db.commit()
    return redirect('/students')

@app.route('/update/<int:id>', methods=['GET','POST'])
def update_student(id):
    if request.method == 'POST':
        name = request.form['name']
        department_id = request.form['department_id']
        year = request.form['year']
        email = request.form['email']

        cursor.execute(
            """
            UPDATE Student
            SET name=%s,
                department_id=%s,
                year=%s,
                email=%s
            WHERE student_id=%s
            """,
            (name, department_id, year, email, id)
        )
        db.commit()
        return redirect('/students')

    cursor.execute("SELECT * FROM Student WHERE student_id=%s", (id,))
    student = cursor.fetchone()
    return render_template('update_student.html', student=student)

@app.route('/search', methods=['POST'])
def search_student():
    sid = request.form['sid']
    cursor.execute("SELECT * FROM Student WHERE student_id=%s", (sid,))
    student = cursor.fetchone()
    return render_template('students.html', students=[student] if student else [])

@app.route('/logs')
def logs_page():
    cursor.execute("SELECT * FROM Student_Log")
    logs = cursor.fetchall()
    return render_template('logs.html', logs=logs)

@app.route('/procedure')
def procedure_page():
    cursor.callproc('GetAllStudents')
    students = []
    for result in cursor.stored_results():
        students = result.fetchall()
    return render_template('procedure.html', students=students)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/add_faculty', methods=['POST'])
def add_faculty():
    fid = request.form['faculty_id']
    name = request.form['name']
    dept = request.form['department_id']
    designation = request.form['designation']

    cursor.execute(
        "INSERT INTO Faculty VALUES(%s,%s,%s,%s)",
        (fid, name, dept, designation)
    )
    db.commit()
    return redirect('/faculty')

@app.route('/delete_faculty/<int:id>')
def delete_faculty(id):
    cursor.execute("DELETE FROM Faculty WHERE faculty_id=%s", (id,))
    db.commit()
    return redirect('/faculty')

@app.route('/update_faculty/<int:id>', methods=['GET','POST'])
def update_faculty(id):
    if request.method == 'POST':
        name = request.form['name']
        department_id = request.form['department_id']
        designation = request.form['designation']

        cursor.execute(
            """
            UPDATE Faculty
            SET name=%s,
                department_id=%s,
                designation=%s
            WHERE faculty_id=%s
            """,
            (name, department_id, designation, id)
        )
        db.commit()
        return redirect('/faculty')

    cursor.execute("SELECT * FROM Faculty WHERE faculty_id=%s", (id,))
    faculty = cursor.fetchone()
    return render_template('update_faculty.html', faculty=faculty)

@app.route('/add_course', methods=['POST'])
def add_course():
    cid = request.form['course_id']
    cname = request.form['course_name']
    credits = request.form['credits']
    dept = request.form['department_id']

    cursor.execute(
        "INSERT INTO Course VALUES(%s,%s,%s,%s)",
        (cid, cname, credits, dept)
    )
    db.commit()
    return redirect('/courses')

@app.route('/delete_course/<int:id>')
def delete_course(id):
    cursor.execute("DELETE FROM Course WHERE course_id=%s", (id,))
    db.commit()
    return redirect('/courses')

@app.route('/update_course/<int:id>', methods=['GET','POST'])
def update_course(id):
    if request.method == 'POST':
        course_name = request.form['course_name']
        credits = request.form['credits']
        department_id = request.form['department_id']

        cursor.execute(
            """
            UPDATE Course
            SET course_name=%s,
                credits=%s,
                department_id=%s
            WHERE course_id=%s
            """,
            (course_name, credits, department_id, id)
        )
        db.commit()
        return redirect('/courses')

    cursor.execute("SELECT * FROM Course WHERE course_id=%s", (id,))
    course = cursor.fetchone()
    return render_template('update_course.html', course=course)

if __name__ == '__main__':
    app.run(debug=True)
