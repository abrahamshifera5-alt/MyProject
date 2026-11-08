
import sqlite3

conn = sqlite3.connect("blog.db")
cursor = conn.cursor()

cursor.execute("""
    UPDATE blog_posts
    SET author_id = 8
    WHERE id = 2 AND author_id IS NULL
""")

conn.commit()

cursor.execute(
    "SELECT id, title, author_id FROM blog_posts"
)
for row in cursor.fetchall():
    print(row)

conn.close()

