import sqlite3 as sql
from os import path


#   Gets the directory name and gets the direct path to the file we pass in
ROOT = path.dirname(path.relpath((__file__)))

#   Takes name and post data as input and returns them to the database
def create_post(name, content):
    
    con = sql.connect(path.join(ROOT, 'database.db'))
    cur = con.cursor()
    cur.execute('insert into posts (name,content) values(?, ?)', [name, content])
    con.commit()
    con.close()

def get_posts():

    con = sql.connect(path.join(ROOT, 'database.db'))
    cur = con.cursor()
    cur.execute('select * from posts')
    posts = cur.fetchall()

    return posts