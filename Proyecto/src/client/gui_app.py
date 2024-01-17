import tkinter as tk
from tkinter import ttk
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
    # print("Conexión exitosa")
    # print("Versión de la base de datos:", connection.version)

    # Realiza operaciones en la base de datos aquí

except cx_Oracle.DatabaseError as db_error:
    print("Error de la base de datos:", db_error)

except Exception as ex:
    print("Error inesperado:", ex)
def barra_menu(root):
    barra_menu=tk.Menu(root)
    root.config(menu=barra_menu,width=300, height=300)
    menu_inicio=tk.Menu(barra_menu,tearoff=0)
    consulta=tk.Menu(barra_menu,tearoff=0)
    info=tk.Menu(barra_menu,tearoff=0)
    barra_menu.add_cascade(label='Inicio', menu=menu_inicio)
    menu_inicio.add_command(label='1')
    menu_inicio.add_command(label='2')
    menu_inicio.add_command(label='Salir Registro en DB',command=root.destroy)
    
    barra_menu.add_cascade(label='Consulta', menu=consulta)
    consulta.add_command(label='1')
    consulta.add_command(label='2')
    consulta.add_command(label='3')

    barra_menu.add_cascade(label='Info', menu=info)
    info.add_command(label='1')
    info.add_command(label='2')
    info.add_command(label='3')

cursor = connection.cursor()
class Frame(tk.Frame):

  
    def __init__(self,root=None):
        super().__init__(root, width=200, height=200, bg='yellow')
        self.root=root
        self.pack()
        self.presupuestos()
        self.deshabilitar_campos()
        self.tabla_presupuesotos()

    def presupuestos(self):
        #Labels
        self.label_nombre=tk.Label(self,text="Nombre:")
        self.label_nombre.config(font=('Arial',12,'bold'))
        self.label_nombre.grid(row =0, column=0, padx=10,pady=10)

        self.label_duracion=tk.Label(self,text="Duracion:")
        self.label_duracion.config(font=('Arial',12,'bold'))
        self.label_duracion.grid(row =1, column=0,padx=10,pady=10)

        self.label_genero=tk.Label(self,text="Genero:")
        self.label_genero.config(font=('Arial',12,'bold'))
        self.label_genero.grid(row =2, column=0,padx=10,pady=10)

        #Entrys
        self.mi_nombre=tk.StringVar()
        self.entry_nombre=tk.Entry(self,textvariable=self.mi_nombre)
        self.entry_nombre.config(width=50, font=('Arial',12))
        self.entry_nombre.grid(row=0,column=1,padx=10,pady=10, columnspan=2)
        
        self.mi_duracion=tk.StringVar()
        self.entry_duracion=tk.Entry(self,textvariable=self.mi_duracion)
        self.entry_duracion.config(width=50, font=('Arial',12))
        self.entry_duracion.grid(row=1,column=1,padx=10,pady=10, columnspan=2)
        
        self.mi_genero=tk.StringVar()
        self.entry_genero=tk.Entry(self,textvariable=self.mi_genero)
        self.entry_genero.config(width=50, font=('Arial',12))
        self.entry_genero.grid(row=2,column=1,padx=10,pady=10, columnspan=2)

        #Botones

        self.boton_nuevo=tk.Button(self,text="Nuevo",command=self.habilitar_campos)
        self.boton_nuevo.config(width=20, font=('Arial',12,'bold'),
        fg='White',bg='#4DCB03', cursor='hand2',activebackground='#43B302')
        self.boton_nuevo.grid(row=3,column=0,padx=10,pady=10)

        self.boton_guardar=tk.Button(self,text="Guardar",command=self.guarda_Datos)
        self.boton_guardar.config(width=20, font=('Arial',12,'bold'),
        fg='White',bg='#0157F2', cursor='hand2',activebackground='#003594')
        self.boton_guardar.grid(row=3,column=1,padx=10,pady=10)

        self.boton_cancelar=tk.Button(self,text="Cancelar",command=self.deshabilitar_campos)
        self.boton_cancelar.config(width=20, font=('Arial',12,'bold'),
        fg='White',bg='#FF1100', cursor='hand2',activebackground='#A30B00')
        self.boton_cancelar.grid(row=3,column=2,padx=10,pady=10)

    def habilitar_campos(self):
        self.mi_nombre.set('')
        self.mi_duracion.set('')
        self.mi_genero.set('')
        self.entry_nombre.config(state='normal')
        self.entry_duracion.config(state='normal')
        self.entry_genero.config(state='normal')
        self.boton_guardar.config(state='normal')
        self.boton_cancelar.config(state='normal')

    def deshabilitar_campos(self):

        self.mi_nombre.set('')
        self.mi_duracion.set('')
        self.mi_genero.set('')
        self.entry_nombre.config(state='disabled')
        self.entry_duracion.config(state='disabled')
        self.entry_genero.config(state='disabled')
        self.boton_guardar.config(state='disabled')
        self.boton_cancelar.config(state='disabled')
    
    def guarda_Datos(self):
        self.deshabilitar_campos()

    def tabla_presupuesotos(self):
        self.tabla =ttk.Treeview(self,columns=('Nombre','Duracion','Genero'))
        self.tabla.grid(row=4,column=0,columnspan=4)
        self.tabla.heading('#0',text='ID')
        self.tabla.heading('#1',text='Nombre')
        self.tabla.heading('#2',text='Duracion')
        self.tabla.heading('#3',text='Genero')

        self.tabla.insert('',0, text='1',values=('Los Vengadores','2.35','Accion'))
    
        self.boton_eliminar=tk.Button(self,text="Eliminar")
        self.boton_eliminar.config(width=20, font=('Arial',12,'bold'),
        fg='White',bg='#4DCB03', cursor='hand2',activebackground='#43B302')
        self.boton_eliminar.grid(row=5,column=0,padx=10,pady=10)

        self.boton_editar=tk.Button(self,text="Editar")
        self.boton_editar.config(width=20, font=('Arial',12,'bold'),
        fg='White',bg='#4DCB03', cursor='hand2',activebackground='#43B302')
        self.boton_editar.grid(row=5,column=1,padx=10,pady=10)

        

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
        connection.commit()
    

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
        




































cursor.close()
connection.close()