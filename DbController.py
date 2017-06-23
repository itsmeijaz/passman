def Add(cur):
  cur.execute("SELECT * FROM table")
  for row in cur.fetchall():
    print row[0]
