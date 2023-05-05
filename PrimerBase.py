import sqlite3

conexion=sqlite3.connect("PrimeraBase.db")#Establecemos conexion

cursor=conexion.cursor()
#cursor.execute("CREATE TABLE USUARIOS(NOMBRE VARCHAR(50),EDAD INTEGER,SEXO VARCHAR(50))")

#cursor.execute("INSERT INTO USUARIOS VALUES('Anthony',22,'Masculino')")
#cursor.execute("SELECT * FROM USUARIOS")

#usuario=cursor.fetchone()
#print(usuario)

#usuarios=[
#    ("Timo",7,"Masculino"),
#    ("Omar",57,"Masculino"),
#    ("Amarilis",56,"Femenino"),
#]

#cursor.executemany("INSERT INTO USUARIOS VALUES(?,?,?)",usuarios)

cursor.execute("SELECT * FROM USUARIOS")
usuarios=cursor.fetchall()
print(usuarios)

for i in usuarios:
 print(i)
conexion.commit()
conexion.close()



