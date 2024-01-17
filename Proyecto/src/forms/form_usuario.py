# # import tkinter as tk
# # import util.util_ventana as util_ventana
# # import cx_Oracle
# # from tkinter import ttk
# class Frame_User(tk.Toplevel):
    
    
#     def __init__(self,root=None):
#         super().__init__(root, width=200, height=200) 
#         self.title("Usuarios")
#         self.root=root
#         # self.pack()
#         self.Usuarios()
#         self.deshabilitar_campos()
#         self.tabla_usuarios()
#         self.refrescarUsuarios()
       
        

    
#     def Usuarios(self):
#         #Labels
#         self.label_iduser=tk.Label(self,text="ID_Usuario:")
#         self.label_iduser.config(font=('Arial',12,'bold'))
#         self.label_iduser.grid(row =0, column=0, padx=10,pady=10)

#         self.label_nombre=tk.Label(self,text="Nombre:")
#         self.label_nombre.config(font=('Arial',12,'bold'))
#         self.label_nombre.grid(row =1, column=0,padx=10,pady=10)

#         self.label_idrol=tk.Label(self,text="Rol:")
#         self.label_idrol.config(font=('Arial',12,'bold'))
#         self.label_idrol.grid(row =2, column=0, padx=10,pady=10)

#         self.label_idcc=tk.Label(self,text="ID_CentroDeCosto:")
#         self.label_idcc.config(font=('Arial',12,'bold'))
#         self.label_idcc.grid(row =3, column=0, padx=10,pady=10)


#         #Entrys
#         self.mi_iduser=tk.StringVar()
#         self.entry_iduser=tk.Entry(self,textvariable=self.mi_iduser)
#         self.entry_iduser.config(width=50, font=('Arial',12))
#         self.entry_iduser.grid(row=0,column=1,padx=10,pady=10, columnspan=2)
        
#         self.mi_nombre=tk.StringVar()
#         self.entry_nombre=tk.Entry(self,textvariable=self.mi_nombre)
#         self.entry_nombre.config(width=50, font=('Arial',12))
#         self.entry_nombre.grid(row=1,column=1,padx=10,pady=10, columnspan=2)

#         self.mi_rol=tk.StringVar()
#         self.entry_rol=tk.Entry(self,textvariable=self.mi_rol)
#         self.entry_rol.config(width=50, font=('Arial',12))
#         self.entry_rol.grid(row=2,column=1,padx=10,pady=10, columnspan=2)

#         self.mi_idcc=tk.StringVar()
#         self.entry_idcc=tk.Entry(self,textvariable=self.mi_idcc)
#         self.entry_idcc.config(width=50, font=('Arial',12))
#         self.entry_idcc.grid(row=3,column=1,padx=10,pady=10, columnspan=2)
        

#         #Botones

#         self.boton_nuevo=tk.Button(self,text="Nuevo",command=self.habilitar_campos)
#         self.boton_nuevo.config(width=20, font=('Arial',12,'bold'),
#         fg='White',bg='#4DCB03', cursor='hand2',activebackground='#43B302')
#         self.boton_nuevo.grid(row=6,column=0,padx=10,pady=10)

#         self.boton_guardar=tk.Button(self,text="Guardar",command=self.guarda_Datos)
#         self.boton_guardar.config(width=20, font=('Arial',12,'bold'),
#         fg='White',bg='#0157F2', cursor='hand2',activebackground='#003594')
#         self.boton_guardar.grid(row=6,column=1,padx=10,pady=10)

#         self.boton_cancelar=tk.Button(self,text="Cancelar",command=self.deshabilitar_campos)
#         self.boton_cancelar.config(width=20, font=('Arial',12,'bold'),
#         fg='White',bg='#F30000', cursor='hand2',activebackground='#8A1C1C')
#         self.boton_cancelar.grid(row=6,column=2,padx=10,pady=10)

#     def habilitar_campos(self):
#         self.mi_nombre.set('')
#         self.mi_rol.set('')
#         self.mi_idcc.set('')
#         self.mi_iduser.set('')
#         self.entry_nombre.config(state='normal')
#         self.entry_iduser.config(state='normal')
#         self.entry_idcc.config(state='normal')
#         self.entry_rol.config(state='normal')
#         self.boton_guardar.config(state='normal')
#         self.boton_cancelar.config(state='normal')

#     def deshabilitar_campos(self):

#         self.mi_nombre.set('')
#         self.mi_idcc.set('')
#         self.mi_iduser.set('')
#         self.mi_rol.set('')
        
#         self.entry_idcc.config(state='disabled')
#         self.entry_iduser.config(state='disabled')
#         self.entry_nombre.config(state='disabled')
#         self.entry_rol.config(state='disabled')
#         self.boton_guardar.config(state='disabled')
#         self.boton_cancelar.config(state='disabled')
    
#     def guarda_Datos(self):
#         self.Create_User()
#         self.deshabilitar_campos()

#     def edit_Datos(self):
#         self.Edit_User()
#         self.deshabilitar_campos()
#     def delete_datos(self):
#         self.Delete_User()
#         self.deshabilitar_campos()

   


#     def obtener_datos_user(self):
#         try:
#             # Conexión a la base de datos
#             connection = cx_Oracle.connect(user='ALONSO', password='123456', dsn='localhost:1521/orcl', encoding='UTF-8')

#             # Llamada al procedimiento almacenado
#             cursor = connection.cursor()
#             p_cursor = cursor.var(cx_Oracle.CURSOR)
#             cursor.callproc("ObtenerDatosUsuario", (p_cursor,))

#             # Obtener los resultados del cursor
#             result_set = p_cursor.getvalue()

#             # Cerrar el cursor y la conexión
#             # cursor.close()
#             # connection.close()

#             return result_set
#         except cx_Oracle.Error as error:
#             print(f"Error de Oracle: {error}")




#     def mostrar_datos_en_tabla(self, result_set):
#         # Limpiar la tabla antes de insertar nuevos datos
#         for item in self.tabla.get_children():
#             self.tabla.delete(item)

#         # Insertar datos en la tabla
#         for row in result_set:
#             self.tabla.insert("", "end", values=row)

#     def refrescarUsuarios(self):
#         result_set = self.obtener_datos_user()

#         # Mostrar datos en la tabla
#         self.mostrar_datos_en_tabla(result_set)

#     def tabla_usuarios(self):
#         # Configuración de la tabla
#         self.tabla = ttk.Treeview(self, columns=('ID_Usuario', 'Nombre','Rol','ID_CentroDeCosto'))
#         self.tabla.grid(row=7, column=0, columnspan=3)
#         self.tabla.heading('#1', text='ID_Usuario')
#         self.tabla.heading('#2', text='Nombre')
#         self.tabla.heading('#3', text='Rol')
#         self.tabla.heading('#4', text='ID_CentroDeCosto')
        

#         # Configuración de los botones
#         self.boton_eliminar = tk.Button(self, text="Eliminar", command=self.delete_datos)
#         self.boton_eliminar.config(width=20, font=('Arial', 12, 'bold'),
#                                 fg='White', bg='#FF0000', cursor='hand2', activebackground='#AE0000')
#         self.boton_eliminar.grid(row=8, column=0, padx=10, pady=10)

#         self.boton_editar = tk.Button(self, text="Editar", command=self.edit_Datos)
#         self.boton_editar.config(width=20, font=('Arial', 12, 'bold'),
#                                 fg='White', bg='#4700BA', cursor='hand2', activebackground='#9468DA')
#         self.boton_editar.grid(row=8, column=1, padx=10, pady=10)

#         self.boton_refresh = tk.Button(self, text="Refrescar", command=self.refrescarUsuarios)
#         self.boton_refresh.config(width=20, font=('Arial', 12, 'bold'),
#                                 fg='White', bg='#4700BA', cursor='hand2', activebackground='#9468DA')
#         self.boton_refresh.grid(row=8, column=2, padx=10, pady=10)


        

#     def Create_User(self):
#         #Conexion
#         try:
#             connection = cx_Oracle.connect(user='ALONSO',password='123456',dsn='localhost:1521/orcl',encoding='UTF-8')
#         except cx_Oracle.DatabaseError as db_error:
#             print("Error de la base de datos:", db_error)
#         except Exception as ex:
#             print("Error inesperado:", ex)
        
#         # Llamar al procedimiento almacenado
#         cursor = connection.cursor()
#         try:
#             cursor.callproc("InsertarUsuario", (self.mi_iduser.get(),self.mi_nombre.get(),self.mi_rol.get(),self.mi_idcc.get()))
#             connection.commit()
#             cursor.close()
#         except cx_Oracle.DatabaseError as e:
#         # Manejar excepciones específicas de Oracle
#             error, = e.args
#             if error.code == 1017:
#                 print("Credenciales de Oracle incorrectas.")
#             elif error.code == 12541:
#                 print("No se pudo conectar al servidor Oracle.")
#             elif error.code == 1:
#                 errorORA1()
#             else:
#                 print(f"Error de Oracle: {error.message}")
#         self.refrescarUsuarios()

    
    
#     def Edit_User(self):
#         #Conexion
#         try:
#             connection = cx_Oracle.connect(user='ALONSO',password='123456',dsn='localhost:1521/orcl',encoding='UTF-8')
#         except cx_Oracle.DatabaseError as db_error:
#             print("Error de la base de datos:", db_error)
#         except Exception as ex:
#             print("Error inesperado:", ex)
#         try:
#             # Llamar al procedimiento almacenado
#             cursor = connection.cursor()
#             cursor.callproc("EditarUsuario", (self.mi_iduser.get(),self.mi_nombre.get(),self.mi_rol.get(),self.mi_idcc.get()))
#             connection.commit()
#         except cx_Oracle.DatabaseError as e:
#         # Manejar excepciones específicas de Oracle
#             error, = e.args
#             if error.code == 1017:
#                 print("Credenciales de Oracle incorrectas.")
#             elif error.code == 12541:
#                 print("No se pudo conectar al servidor Oracle.")
#             else:
#                 print(f"Error de Oracle: {error.message}")
#         self.refrescarUsuarios()
        

#     def Delete_User(self):
#         #Conexion
#         try:
#             connection = cx_Oracle.connect(user='ALONSO',password='123456',dsn='localhost:1521/orcl',encoding='UTF-8')
#         except cx_Oracle.DatabaseError as db_error:
#             print("Error de la base de datos:", db_error)
#         except Exception as ex:
#             print("Error inesperado:", ex)
#         try:
#             # Llamar al procedimiento almacenado
#             cursor = connection.cursor()
#             temp=self.mi_iduser.get()
#             num=int(temp)
#             cursor.callproc("EliminarUsuario", (num,))
#             connection.commit()
#             if cursor.rowcount > 0:
#                 # Mostrar ventana de éxito
#                 mostrar_ventana_exito()
#             else:
#                 # Mostrar ventana de fallo (dato no encontrado)
#                 mostrar_ventana_fallo("El dato no existe")
#         except cx_Oracle.DatabaseError as e:
#             # Manejar excepciones específicas de Oracle
#             error, = e.args
#             if error.code == 1017:
#                 print("Credenciales de Oracle incorrectas.")
#             elif error.code == 12541:
#                 print("No se pudo conectar al servidor Oracle.")
#             else:
#                 print(f"Error de Oracle: {error.message}")

#             # Mostrar ventana de fallo
#             self.mostrar_ventana_fallo("No se pudo agregar el dato")
#         finally:
#             # Cerrar el cursor y la conexión en el bloque finally
#             if cursor:
#                 cursor.close()
#         self.refrescarUsuarios()
  