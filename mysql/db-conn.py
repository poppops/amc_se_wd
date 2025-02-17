import mysql.connector

"""
Establish a connection to the database
When connecting to a database there are 4 keys pieces of information

- host: The address to the server the database is running on. Typically localhost
- user: The username to connect to the database
- password: The password to connect to the database
- database: The name of the database to connect to
"""
conn = mysql.connector.connect(
    host="localhost", user="root", password="p4??word", database="amc_se"
)

"""
The cursor object is used to interact with the database
"""
curosor = conn.cursor()

# Execute a query
sql = "SELECT * FROM novel_list"
cursor.execute(sql)
novel_list = cursor.fetchall()

for novel in novel_list:
    print(novel)

# Insert Queries
insertQuery = "INSERT INTO novel_list (novel_name, novel_type, theme, author, cover_page) VALUES (%s, %s, %s, %s, %s)"

# Insert a single record
values = (
    "The Great Gatsby",
    "Fiction",
    "Romance",
    "F. Scott Fitzgerald",
    "https://www.google.com",
)

cursor.execute(insertQuery, values)
cursor.commit()

# Insert multiple records
values = [
    (
        "The Great Gatsby",
        "Fiction",
        "Romance",
        "F. Scott Fitzgerald",
        "https://www.google.com",
    ),
    (
        "To Kill a Mockingbird",
        "Fiction",
        "Thriller, Legal Story",
        "Harper Less",
        "https://www.google.com",
    ),
]

cursor.executemany(insertQuery, values)
cursor.commit()
