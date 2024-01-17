import cx_Oracle
import tkinter as tk
from tkinter import ttk

try:
    connection = cx_Oracle.connect(
        user='ALONSO',
        password='123456',
        dsn='localhost:1521/orcl',
        encoding='UTF-8'
    )
    #orclpdb PDB$SEED
    print("Conexión exitosa")
    print("Versión de la base de datos:", connection.version)

    # Realiza operaciones en la base de datos aquí

except cx_Oracle.DatabaseError as db_error:
    print("Error de la base de datos:", db_error)

except Exception as ex:
    print("Error inesperado:", ex)


# Crear un cursor
cursor = connection.cursor()
class CRUD_Rubro:
    

    def Create_Rubro(ID_Rubro,Nombre):
        # Llamar al procedimiento almacenado
        cursor.callproc("InsertarRubro", (ID_Rubro, f'{Nombre}'))
        connection.commit()
    def Read_Rubros(datos):
        # Crear la interfaz gráfica
        root = tk.Tk()
        root.title("Datos de la Tabla Rubro")

        # Crear un treeview para mostrar los datos
        tree = ttk.Treeview(root)
        tree["columns"] = ("ID_Rubro", "Nombre")
        tree.heading("#0", text="ID_Rubro", anchor=tk.W)
        tree.column("#0", anchor=tk.W)
        for col in tree["columns"]:
            tree.heading(col, text=col)
            tree.column(col, anchor=tk.W)

        # Insertar los datos en el treeview
        for row in datos:
            tree.insert("", "end", values=row)

        tree.pack(expand=True, fill=tk.BOTH)

        # Ejecutar la interfaz gráfica
        root.mainloop()
    

    def Edit_Rubro(ID_Rubro,Nombre):
        cursor.callproc("EditarRubro", (21, f'{Nombre}'))
        connection.commit()

    def Delete_Rubro(ID_Rubro):
        cursor.callproc("EliminarRubro", (ID_Rubro,))
        connection.commit()
        
    def obtener_datos():
        # Conectarse a la base de datos
        connection = cx_Oracle.connect('usuario/contraseña@localhost:1521/nombre_base_datos')
        cursor = connection.cursor()

        # Llamar al procedimiento almacenado para obtener los datos
        datos_cursor = cursor.var(cx_Oracle.CURSOR)
        cursor.callproc("ObtenerDatosRubro", (datos_cursor,))

        # Obtener los datos del cursor
        datos = datos_cursor.getvalue().fetchall()

        # Cerrar el cursor y la conexión
        cursor.close()
        connection.close()

        return datos
        
    



# Cerrar el cursor y la conexión
cursor.close()
connection.close()








