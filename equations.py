# first install "python with path"
# If you have any questions this youtube video will explain
# https://www.youtube.com/watch?v=byHcYRpMgI4
import sqlite3 

#connect to database
conn = sqlite3.connect('equations.db')

#Create a cursor
c = conn.cursor()

#Create a Table
#Datatypes are NULL, INTEGAR, REAL, TEXT, BLOB
# c.execute("""CREATE TABLE addition (
#     s_problems TEXT,
#     s_answer INTEGAR
# )""")

#Query the Database
c.execute("SELECT rowid, * FROM division")
items = c.fetchall()

for item in items:
    print(item)


# addition = [('4 + 4', 8),
#             ('10 + 13', 23), 
#             ('20 + 70', 90), 
#             ('81 + 3', 84), 
#             ('41 + 40', 81), 
#             ('66 + 30', 96), 
#             ('11 + 10', 21), 
#             ('15 + 13', 28), 
#             ('16 + 22', 38), 
#             ('70 + 23', 93), 
#             ('88 + 11', 99), 
#             ('35 + 10', 45), 
#             ('34 + 35', 69), 
#             ('32 + 33', 65), 
#             ('20 + 8', 28), 
#             ('11 + 3', 14), 
#             ('15 + 5', 20), 
#             ('31 + 8', 39), 
#             ('44 + 11', 55),]

# c.executemany("INSERT INTO addition VALUES (?,?)", addition)

#Commit our command
conn.commit()

#Close our connection
conn.close()
