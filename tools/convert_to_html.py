import sqlite3

conn = sqlite3.connect('ashok_blog.db')
c = conn.cursor()
rs = c.execute('select * from posts')

records = rs.fetchall()

i = len(records)
for record in records:
    content = ""
    content = """
<html>
<body>
<h1>"""+ record[0] +"""</h1>
"""+ record[1] +"""
</body>
</html>"""
    open("../html/" + str(i) + ".html","w+").write(content.encode("utf-8"))
    i = i - 1
c.close()
conn.close()
