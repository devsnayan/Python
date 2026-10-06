import html
import mysql.connector
from Config import DB_CONFIG
from Model.Student import Student

class StudentManagement:
    def __init__(self):
        self.db = mysql.connector.connect(host=DB_CONFIG["host"], user=DB_CONFIG["user"], password=DB_CONFIG["password"], database=DB_CONFIG["database"],)
        self.cursor = self.db.cursor(dictionary=True)

    # DATABASE

    def close_database(self):
        if self.cursor:
            self.cursor.close()

        if self.db:
            self.db.close()

    # GET ALL STUDENTS

    def get_students(self):
        query = "SELECT id, name, email, age, department FROM students ORDER BY id DESC"

        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        students = []

        for row in rows:
            student = Student(row["id"],row["name"],row["email"],row["age"],row["department"],)
            students.append(student)

        return students

    # GET SINGLE STUDENT

    def get_student(self, student_id):
        query = "SELECT id, name, email, age, department FROM students WHERE id = %s"

        self.cursor.execute(query, (student_id,))
        row = self.cursor.fetchone()

        if row is None:
            return None

        return Student( row["id"], row["name"], row["email"], row["age"], row["department"],)

    # STORE STUDENT

    def store(self, name, email, age, department):
        query = "INSERT INTO students (name, email, age, department) VALUES (%s, %s, %s, %s)"

        self.cursor.execute(query, (name, email, age, department))
        self.db.commit()

        return self.cursor.lastrowid

    # UPDATE STUDENT

    def update(self, student_id, name, email, age, department):
        query = "UPDATE students SET name = %s, email = %s, age = %s, department = %s WHERE id = %s"

        self.cursor.execute(query, (name, email, age, department, student_id))
        self.db.commit()

        return self.cursor.rowcount > 0

    # DELETE STUDENT

    def delete(self, student_id):
        query = "DELETE FROM students WHERE id = %s"

        self.cursor.execute(query, (student_id,))
        self.db.commit()

        return self.cursor.rowcount > 0

    # TEMPLATE RENDER

    def render(self, view_name, data=None):
        if data is None:
            data = {}

        layout_path = "View/Layout/App.html"
        view_path = f"View/{view_name}.html"

        with open(layout_path, "r", encoding="utf-8") as file:
            layout = file.read()

        with open(view_path, "r", encoding="utf-8") as file:
            content = file.read()

        for key, value in data.items():
            placeholder = "{{ " + key + " }}"
            content = content.replace(placeholder, str(value))

        html_page = layout.replace("{{ content }}", content)
        return html_page

    # INDEX

    def index(self):
        students = self.get_students()
        rows = ""

        for student in students:
            rows += f"""
                <tr>
                    <td>{student.id}</td>
                    <td>{html.escape(student.name)}</td>
                    <td>{html.escape(student.email)}</td>
                    <td>{student.age}</td>
                    <td>{html.escape(student.department)}</td>
                    <td>
                        <a href="/student/show?id={student.id}">Show</a>
                        <a href="/student/edit?id={student.id}">Edit</a>
                        <a href="/student/delete?id={student.id}" onclick="return confirm('Are you sure?')">Delete</a>
                    </td>
                </tr>
            """
        return self.render("Index", {"students": rows})

    # SHOW

    def show(self, student_id):
        student = self.get_student(student_id)

        if student is None:
            return self.render("Show", {"student": """
                <h2>Student not found</h2>
            """})

        student_html = f"""
            <div class="student-details">
                <h2>{html.escape(student.name)}</h2>
                <p><strong>ID:</strong>{student.id}</p>
                <p><strong>Email:</strong>{html.escape(student.email)}</p>
                <p><strong>Age:</strong> {student.age}</p>
                <p><strong>Department:</strong> {html.escape(student.department)}</p>
                <p><strong>Adult:</strong> {"Yes" if student.is_adult() else "No"}</p>
                <a href="/">Back</a>
            </div>
        """

        return self.render("Show", {"student": student_html})


    # CREATE PAGE

    def create(self):
        return self.render("Create")

    # EDIT PAGE

    def edit(self, student_id):
        student = self.get_student(student_id)

        if student is None:
            return self.render("Edit", {"form": """
                <h2>
                    Student not found
                </h2>
            """})

        form = f"""
            <form method="POST" action="/student/update">
                <input type="hidden" name="id" value="{student.id}">
                <label>Name</label>
                <input type="text" name="name" value="{html.escape(student.name)}" required>
                <label>Email</label>
                <input type="email" name="email" value="{html.escape(student.email)}" required>
                <label>Age</label>
                <input type="number" name="age" value="{student.age}" required>
                <label>Department</label>
                <input type="text" name="department" value="{html.escape(student.department)}" required>
                <button type="submit">Update Student</button>
            </form>
        """

        return self.render("Edit", {"form": form})

    # UPDATE

    def update_student(self, student_id, data):
        name = data["name"][0]
        email = data["email"][0]
        age = data["age"][0]
        department = data["department"][0]
        self.update(student_id, name, email, age, department)
        return self.redirect("/")

    # ==========================================
    # CREATE / STORE
    # ==========================================

    def store_student(self, data):
        name = data["name"][0]
        email = data["email"][0]
        age = data["age"][0]
        department = data["department"][0]

        self.store(name, email, age, department)
        return self.redirect("/")

    # REDIRECT

    def redirect(self, url):
        return f"""<script>window.location.href = "{url}";</script>"""

    # ROUTER - GET

    def handle_get(self, path, query):
        if path == "/":
            return self.index()
        elif path == "/student/create":
            return self.create()
        elif path == "/student/show":
            student_id = query.get("id", [None])[0]
            return self.show(student_id)
        elif path == "/student/edit":
            student_id = query.get("id", [None])[0]
            return self.edit(student_id)
        elif path == "/student/delete":
            student_id = query.get("id", [None])[0]
            self.delete(student_id)
            return self.redirect("/")

        return self.render("Show", {"student": """
            <h2>404 - Page Not Found</h2>
        """})

    # ROUTER - POST

    def handle_post(self, path, data):
        if path == "/student/store":
            return self.store_student(data)
        elif path == "/student/update":
            student_id = data["id"][0]
            return self.update_student(student_id, data)

        return "404 - Page Not Found"