import sqlite3

conexion=sqlite3.connect("Segunda_base.db")

cursor=conexion.cursor()

cursor.execute('''
  CREATE TABLE VIDEOJUEGOS(
  CodigoDeJuego INTEGER PRIMARY KEY AUTOINCREMENT,
  VideConsola VARCHAR(20),
  Videojuego VARCHAR (20))
 
  ''')
videojuegos=[
    ('Nintendo switch','Super smash bros ultimate'),
    ('Psvita','Golden persona 4'),
    ('Ps5','Tekken 7'),
]

cursor.executemany("INSERT INTO VIDEOJUEGOS VALUES(NULL,?,?)",videojuegos)

conexion.commit()
conexion.close()