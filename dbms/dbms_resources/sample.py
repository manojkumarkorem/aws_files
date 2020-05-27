import sqlite3
conn = sqlite3.connect('sample.db')
c = conn.cursor()
c.execute("""CREATE TABLE emp(
            first text,
            last text,
            pay integer
            )""")
            
conn.commit()
