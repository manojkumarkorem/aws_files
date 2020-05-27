class Student:
    def __init__(self, name, age, score):
        self.student_id = None
        self.name = name
        self.age = age
        self.score = score
        
sql_query = """CREATE TABLE Student(
               student_id INTEGER PRIMARY KEY AUTOINCREMENT,
               name VARCHAR(20),
               age INT,
               score INT);
               """
sql_query = """INSERT INTO Student(
               name,
               age,
               score
               ) VALUES(%s, %d, %d);
                """




def write_data(sql_query):
	import sqlite3
	connection = sqlite3.connect("db.sqlite3")
	crsr = connection.cursor() 
	crsr.execute("PRAGMA foreign_keys=on;") 
	crsr.execute(sql_query) 
	connection.commit() 
	connection.close()
    
def read_data(sql_query):
    import sqlite3
    connection = sqlite3.connect("db.sqlite3")
    crsr = connection.cursor() 
    crsr.execute(sql_query) 
    ans= crsr.fetchall()  
    connection.close() 
    return ans
    
    