import sqlite3

conexion=sqlite3.connect("Productos.db")

cursor=conexion.cursor()

cursor.execute('''
      CREATE TABLE PRODUCTOS(
      ID INTEGER PRIMARY KEY AUTOINCREMENT,
      NOMBRE_P VARCHAR(20),
      SECCION_p VARCHAR(20))
''')

productos= [
    ('Leche','Lacteos'),
    ('Pan','Panaderia'),
    ('Carne','Carniceria'),
]

cursor.executemany("INSERT INTO PRODUCTOS VALUES (NULL,?,?),",productos)

conexion.commit()
conexion.close()