# import tkinter as tk
# import util.util_ventana as util_ventana
# import cx_Oracle
# from tkinter import ttk
# class Frame_CC(tk.Toplevel):
    
    
#     def __init__(self,root=None):
#         super().__init__(root, width=200, height=200) 
#         self.title("Centro de Costos")
#         self.root=root
#         # self.pack()
#         self.centroDeCostos()
#         self.deshabilitar_campos()
#         self.tabla_cc()
#         self.refrescarCC()
       
        

    
#     def centroDeCostos(self):
#         #Labels
#         self.label_idcc=tk.Label(self,text="ID_CentroDeCosto:")
#         self.label_idcc.config(font=('Arial',12,'bold'))
#         self.label_idcc.grid(row =0, column=0, padx=10,pady=10)

#         self.label_nombre=tk.Label(self,text="Nombre:")
#         self.label_nombre.config(font=('Arial',12,'bold'))
#         self.label_nombre.grid(row =1, column=0,padx=10,pady=10)

#         self.label_idcc=tk.Label(self,text="ID_Padre:")
#         self.label_idcc.config(font=('Arial',12,'bold'))
#         self.label_idcc.grid(row =2, column=0, padx=10,pady=10)


#         #Entrys
#         self.mi_idcc=tk.StringVar()
#         self.entry_idcc=tk.Entry(self,textvariable=self.mi_idcc)
#         self.entry_idcc.config(width=50, font=('Arial',12))
#         self.entry_idcc.grid(row=0,column=1,padx=10,pady=10, columnspan=2)
        
#         self.mi_nombre=tk.StringVar()
#         self.entry_nombre=tk.Entry(self,textvariable=self.mi_nombre)
#         self.entry_nombre.config(width=50, font=('Arial',12))
#         self.entry_nombre.grid(row=1,column=1,padx=10,pady=10, columnspan=2)

#         self.mi_idpadre=tk.StringVar()
#         self.entry_idpadre=tk.Entry(self,textvariable=self.mi_idpadre)
#         self.entry_idpadre.config(width=50, font=('Arial',12))
#         self.entry_idpadre.grid(row=2,column=1,padx=10,pady=10, columnspan=2)
        

#         #Botones

#         self.boton_nuevo=tk.Button(self,text="Nuevo",command=self.habilitar_campos)
#         self.boton_nuevo.config(width=20, font=('Arial',12,'bold'),
#         fg='White',bg='#4DCB03', cursor='hand2',activebackground='#43B302')
#         self.boton_nuevo.grid(row=5,column=0,padx=10,pady=10)

#         self.boton_guardar=tk.Button(self,text="Guardar",command=self.guarda_Datos)
#         self.boton_guardar.config(width=20, font=('Arial',12,'bold'),
#         fg='White',bg='#0157F2', cursor='hand2',activebackground='#003594')
#         self.boton_guardar.grid(row=5,column=1,padx=10,pady=10)

#         self.boton_cancelar=tk.Button(self,text="Cancelar",command=self.deshabilitar_campos)
#         self.boton_cancelar.config(width=20, font=('Arial',12,'bold'),
#         fg='White',bg='#F30000', cursor='hand2',activebackground='#8A1C1C')
#         self.boton_cancelar.grid(row=5,column=2,padx=10,pady=10)

#     def habilitar_campos(self):
#         self.mi_nombre.set('')
#         self.mi_idcc.set('')
#         self.mi_idpadre.set('')
#         self.entry_nombre.config(state='normal')
#         self.entry_idpadre.config(state='normal')
#         self.entry_idcc.config(state='normal')
#         self.boton_guardar.config(state='normal')
#         self.boton_cancelar.config(state='normal')

#     def deshabilitar_campos(self):

#         self.mi_nombre.set('')
#         self.mi_idcc.set('')
#         self.mi_idpadre.set('')
#         self.entry_idcc.config(state='disabled')
#         self.entry_idpadre.config(state='disabled')
#         self.entry_nombre.config(state='disabled')
#         self.boton_guardar.config(state='disabled')
#         self.boton_cancelar.config(state='disabled')
    
#     def guarda_Datos(self):
#         self.Create_CC()
#         self.deshabilitar_campos()

#     def edit_Datos(self):
#         self.Edit_CC()
#         self.deshabilitar_campos()
#     def delete_datos(self):
#         self.Delete_CC()
#         self.deshabilitar_campos()

   


#     def obtener_datos_cc(self):
#         try:
#             # Conexión a la base de datos
#             connection = cx_Oracle.connect(user='ALONSO', password='123456', dsn='localhost:1521/orcl', encoding='UTF-8')

#             # Llamada al procedimiento almacenado
#             cursor = connection.cursor()
#             p_cursor = cursor.var(cx_Oracle.CURSOR)
#             cursor.callproc("ObtenerDatosCentroDeCosto", (p_cursor,))

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

#     def refrescarCC(self):
#         result_set = self.obtener_datos_cc()

#         # Mostrar datos en la tabla
#         self.mostrar_datos_en_tabla(result_set)

#     def tabla_cc(self):
#         # Configuración de la tabla
#         self.tabla = ttk.Treeview(self, columns=('ID_CentroDeCosto', 'Nombre','ID_Padre'))
#         self.tabla.grid(row=6, column=0, columnspan=3)
#         self.tabla.heading('#1', text='ID_CentroDeCosto')
#         self.tabla.heading('#2', text='Nombre')
#         self.tabla.heading('#3', text='ID_Padre')

#         # Configuración de los botones
#         self.boton_eliminar = tk.Button(self, text="Eliminar", command=self.delete_datos)
#         self.boton_eliminar.config(width=20, font=('Arial', 12, 'bold'),
#                                 fg='White', bg='#FF0000', cursor='hand2', activebackground='#AE0000')
#         self.boton_eliminar.grid(row=7, column=0, padx=10, pady=10)

#         self.boton_editar = tk.Button(self, text="Editar", command=self.edit_Datos)
#         self.boton_editar.config(width=20, font=('Arial', 12, 'bold'),
#                                 fg='White', bg='#4700BA', cursor='hand2', activebackground='#9468DA')
#         self.boton_editar.grid(row=7, column=1, padx=10, pady=10)

#         self.boton_refresh = tk.Button(self, text="Refrescar", command=self.refrescarCC)
#         self.boton_refresh.config(width=20, font=('Arial', 12, 'bold'),
#                                 fg='White', bg='#4700BA', cursor='hand2', activebackground='#9468DA')
#         self.boton_refresh.grid(row=7, column=2, padx=10, pady=10)


        

#     def Create_CC(self):
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
#             cursor.callproc("InsertarCentroDeCosto", (self.mi_idcc.get(),self.mi_nombre.get(),self.mi_idpadre.get()))
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
#                 # errorORA1()
#                 print("")
#             else:
#                 print(f"Error de Oracle: {error.message}")
#         self.refrescarCC()

    
    
#     def Edit_CC(self):
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
#             cursor.callproc("EditarCentroDeCosto", (self.mi_idcc.get(),self.mi_nombre.get(),self.mi_idpadre.get()))
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
#         self.refrescarCC()
        

#     def Delete_CC(self):
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
#             temp=self.mi_idcc.get()
#             num=int(temp)
#             cursor.callproc("EliminarCentroDeCosto", (num,))
#             connection.commit()
#             if cursor.rowcount > 0:
#                 # Mostrar ventana de éxito
#                 # mostrar_ventana_exito()
#                 print("")
#             else:
#                 # Mostrar ventana de fallo (dato no encontrado)
#                 # mostrar_ventana_fallo("El dato no existe")
#                 print("")
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
#         self.refrescarCC()
       
            