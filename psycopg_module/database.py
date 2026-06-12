import psycopg2

def table():
    conn = psycopg2.connect(
        dbname = "yadav_brothers",
        host = "localhost",
        user = "postgres",
        password = "Ali@2004python"
    )

    cursor = conn.cursor()
    cursor.execute('''create table students_info(id SERIAL PRIMARY KEY,name VARCHAR(100),contact VARCHAR(12),addmi_date DATE)''')

    conn.commit()
    conn.close()

    print("Table Create successfully")


def insert_data():
    conn = psycopg2.connect(
        dbname = "yadav_brothers",
        host = "localhost",
        user = "postgres",
        password = "Ali@2004python"
    )

    cursor = conn.cursor()
    cursor.execute('''insert into students_info(name,contact,addmi_date) values ('Pankaj','8002938316','15-09-2023')''')

    conn.commit()
    conn.close()

    print("Add data successfully")

def add_data_by_user():
    conn = psycopg2.connect(
        dbname = "yadav_brothers",
        host = "localhost",
        user = "postgres",
        password = "Ali@2004python"
    )

    name = input("Enter name : ")
    contact = input("contact : ")
    addmi_date = input("addmition date : ")

    cursor = conn.cursor()

    query = '''insert into students_info(name,contact,addmi_date) values (%s,%s,%s)'''
    cursor.execute(query,(name,contact,addmi_date))

    conn.commit()
    conn.close()

    print("add data successfully")


def fetch_data():
    conn = psycopg2.connect(
        dbname = "yadav_brothers",
        host = "localhost",
        user = "postgres",
        password = "Ali@2004python"
    )

    cursor = conn.cursor()
    cursor.execute('''select * from students_info''')
    print(cursor.fetchall())

    conn.commit()
    conn.close()

fetch_data()
