import sqlite3

conn = sqlite3.connect('/web/Sqlite-Data/Movies_Database.db')

c = conn.cursor()
c.execute('''
          CREATE TABLE movies
          (id INTEGER PRIMARY KEY ASC, title varchar(250) NOT NULL,
          release_date INTEGER NOT NULL)
          ''')
c.execute('''
          CREATE TABLE actors
          (id INTEGER PRIMARY KEY ASC, name varchar(250), birthday INTEGER NOT NULL)
          ''')
c.execute('''
          CREATE TABLE stuntmen
          (id INTEGER PRIMARY KEY ASC, name varchar(250), active INTEGER NOT NULL,actor_id INTEGER NOT NULL,
           FOREIGN KEY(actor_id) REFERENCES actors(id))
          ''')
c.execute('''
          CREATE TABLE contact_details
          (id INTEGER PRIMARY KEY ASC, phone_number varchar(250),
           address varchar, actor_id INTEGER NOT NULL,
           FOREIGN KEY(actor_id) REFERENCES actors(id))
          ''')

conn.commit()
conn.close()