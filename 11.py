import sqlite3
 
con = sqlite3.connect("films.db")
cur = con.cursor()
result = cur.execute("""SELECT * FROM Films
            WHERE year <= 1997""").fetchall()
for elem in result:
    print(elem)
con.close()
