import cx_Oracle
import tkinter as tk
from tkinter import ttk

def obtener_datos():
    # Conectarse a la base de datos
    connection = cx_Oracle.connect(
        user='ALONSO',
        password='123456',
        dsn='localhost:1521/orcl',
        encoding='UTF-8'
    ) 
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

def mostrar_interfaz(datos):
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

# Obtener datos de la base de datos
datos_rubro = obtener_datos()

# Mostrar la interfaz gráfica con los datos
mostrar_interfaz(datos_rubro)
