import sqlite3
import os


def create_database():
    if os.path.exists("students.db"):
        os.remove("students.db")

    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    return conn, cursor


def create_tables(cursor):

    cursor.execute('''
    CREATE TABLE Students (
        id INTEGER PRIMARY KEY,
        name VARCHAR NOT NULL,
        age INTEGER,
        email VARCHAR UNIQUE,
        city VARCHAR)
    ''')

    cursor.execute('''
        CREATE TABLE Courses (
            id INTEGER PRIMARY KEY,
            course_name VARCHAR NOT NULL,
            instructor TEXT,
            credits INTEGER)
        ''')


def insert_sample_data(cursor):

    students = [
        (1,'Alice Johnson', 20, 'alice@gmail.com', 'New York'),
        (2,'Bob Smith', 19, 'bob@gmail.com', 'Chicago'),
        (3,'Carol White', 21, 'carol@gmail.com', 'Boston'),
        (4,'David Brown', 20, 'david@gmail.com', 'New York'),
        (5,'Emma Davis', 22, 'emma@gmail.com', 'Seattle')
    ]

    cursor.executemany("INSERT INTO Students VALUES (?,?,?,?,?)", students)

    courses = [
        (1, 'Python Programming', 'Dr. Anderson', 3),
        (2, 'Web Development', 'Prof. Wilson', 4),
        (3, 'Data Science', 'Dr. Taylor', 3),
        (4, 'Mobile Apps', 'Prof. Garcia', 2)
    ]

    cursor.executemany("INSERT INTO Courses VALUES (?,?,?,?)", courses)

    print("Sample data inserted successfully")

# cursor.execute("INSERT INTO Students (name, age, email, city) VALUES ('eylul', 21, 'abc@mail.com','Izmir')", )
# Excluding 'INSERT INTO' operations, specifying the ID is mandatory.

# READING
def basic_sql_operations(cursor):

    #SELECT All
    print("SELECT ALL ")
    cursor.execute("SELECT * FROM Students") # Students is the table so, uppercase S
    records = cursor.fetchall()
    for row in records:
        print(row)

    # SELECT Columns
    print("\n SELECT ID, NAME, AGE ")
    cursor.execute("SELECT id, name, age FROM Students")
    records = cursor.fetchall()
    for row in records:
        print(row)

    # WHERE Clause
    print("\n WHERE AGE < 21")
    cursor.execute("SELECT name, age FROM Students WHERE age < 21")
    records = cursor.fetchall()
    for row in records:
        print(row)

    # WHERE with string
    print("\n WHERE city LIKE '%e'")
    cursor.execute("SELECT * FROM Students WHERE city LIKE '%e'") # ends with e
    records = cursor.fetchall()
    for row in records:
        print(row)

    # 5) ORDER BY
    print("\n ORDER BY age")
    cursor.execute("SELECT * FROM Students ORDER BY age")
    records = cursor.fetchall()
    for row in records:
        print(row)

   # 6) LIMIT
    print("\n LIMIT BY 1")
    cursor.execute("SELECT * FROM Students LIMIT 1")
    records = cursor.fetchone() # returns one tuple
    print(records[0])

def sql_update_delete_insert_op(conn,cursor):

    #INSERT
    cursor.execute("INSERT INTO Students VALUES (6,'Eylul Bencik',25,'abc@gmail.com','UK')")
    conn.commit() # !!!

    # UPDATE
    cursor.execute("UPDATE Students SET age = ? WHERE id = ?", (19,2))
    conn.commit() # !!!

    # DELETE
    cursor.execute("DELETE FROM Students WHERE age = 25")
    conn.commit() # !!!


def aggregate_functions(cursor):
    # 1) Count
    print("Aggregate Functions Count")
    cursor.execute("SELECT COUNT(*) FROM Students")
    result = cursor.fetchone()
    print(result[0])

    # 2) Average
    print("\nAggregate Functions Average")
    cursor.execute("SELECT AVG(age) FROM Students")
    result = cursor.fetchone()
    print(result[0])

    # 3) MAX - MIN
    print("\nAggregate Functions Max-Min")
    cursor.execute("SELECT MAX(age), MIN(age) FROM Students")
    result = cursor.fetchone()
    max_age, min_age = result
    print(max_age)
    print(min_age)

    # 4) GROUP BY
    print("\nAggregate Functions Group by")
    cursor.execute("SELECT city, COUNT(*) FROM Students GROUP BY city")
    result = cursor.fetchall()
    print(result)

def questions():
    '''
    Basit
    1) Bütün kursların bilgilerini getirin
    2) Sadece eğitmenlerin ismini ve ders ismi bilgilerini getirin
    3) Sadece 21 yaşındaki öğrencileri getirin
    4) Sadece Chicago'da yaşayan öğrencileri getirin
    5) Sadece 'Dr. Anderson' tarafından verilen dersleri getirin
    6) Sadece ismi 'A' ile başlayan öğrencileri getirin
    7) Sadece 3 ve üzeri kredi olan dersleri getirin

    Detaylı
    1) Öğrencileri alphabetic şekilde dizerek getirin
    2) 20 yaşından büyük öğrencileri, ismine göre sıralayarak getirin
    3) Sadece 'New York' veya 'Chicago' da yaşayan öğrencileri getirin ve yaşlarına göre sıralayın.
    4) Sadece 'New York' ta yaşamayan öğrencileri getirin
    '''





def myAnswers(cursor):
    # Q1
    cursor.execute("SELECT * FROM Courses")
    records = cursor.fetchall()
    for row in records:
        print(row)

    #Q2
    print("\n")
    cursor.execute("SELECT instructor, course_name FROM Courses")
    records = cursor.fetchall()
    for row in records:
        print(row)

    #Q3
    print("\n")
    cursor.execute("SELECT * FROM Students WHERE age = 21")
    records = cursor.fetchall()
    for row in records:
        print(row)

    #Q4
    print("\n")
    cursor.execute("SELECT * FROM Students WHERE city = ' Chicago'")
    records = cursor.fetchall()
    for row in records:
        print(row)

    #Q5
    print("\n")
    cursor.execute("SELECT course_name FROM Courses WHERE instructor = 'Dr. Anderson'")
    records = cursor.fetchall()
    for row in records:
        print(row)

    #Q6
    print("\n")
    cursor.execute("SELECT * FROM Students WHERE name LIKE 'a%'")
    records = cursor.fetchall()
    for row in records:
        print(row)

    #complicated ones
    #Q1
    print("\n")
    cursor.execute("SELECT * FROM Students ORDER BY name ")
    records = cursor.fetchall()
    for row in records:
        print(row)

    #Q2
    print("\n")
    cursor.execute("SELECT * FROM Students WHERE age > 20 ORDER BY name")
    records = cursor.fetchall()
    for row in records:
        print(row)

    #Q3
    print("\n")
    cursor.execute("SELECT * FROM Students WHERE city = 'New York' OR city = 'Chicago' ORDER BY age")
    records = cursor.fetchall()
    for row in records:
        print(row)

    #Q4
    print("\n")
    cursor.execute("SELECT * FROM Students WHERE city NOT LIKE 'New York'") # use of NOT LIKE
    records = cursor.fetchall()
    for row in records:
        print(row)


def main():
    conn, cursor = create_database()

    try:
        create_tables(cursor)
        insert_sample_data(cursor)
        #basic_sql_operations(cursor)
        #sql_update_delete_insert_op(conn, cursor)
        #aggregate_functions(cursor)
        myAnswers(cursor)
        conn.commit()

    except sqlite3.Error as e:
        print(e)

    finally:
        conn.close()

if __name__ == "__main__":
    main()