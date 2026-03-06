from database.db import connect

def add_student(student):

    conn = connect()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO students(name,age,department,email) VALUES(?,?,?,?)",
        (student.name, student.age, student.department, student.email)
    )

    conn.commit()
    conn.close()


def get_students():

    conn = connect()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")

    rows = cursor.fetchall()

    conn.close()

    return rows


def delete_student(student_id):

    conn = connect()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM students WHERE id=?", (student_id,))

    conn.commit()
    conn.close()


def update_student(student_id, name, age, department, email):

    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE students
        SET name=?, age=?, department=?, email=?
        WHERE id=?
    """, (name, age, department, email, student_id))

    conn.commit()
    conn.close()


def search_student(keyword):

    conn = connect()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM students WHERE name LIKE ?",
        ('%' + keyword + '%',)
    )

    rows = cursor.fetchall()

    conn.close()

    return rows