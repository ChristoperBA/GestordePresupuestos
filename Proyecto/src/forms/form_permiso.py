# import tkinter as tk
# import util.util_ventana as util_ventana
# import cx_Oracle
# from tkinter import ttk
class Frame_Permiso(tk.Toplevel):
    
    
    def __init__(self,root=None):
        super().__init__(root, width=600, height=600) 
        self.title("Permisos")
        self.root=root
        # self.pack()
        self.Permisos()
        self.deshabilitar_campos()
        self.tabla_permisos()
        self.refrescarPermisos()
       
        

    
    def Permisos(self):
        #Labels
        
        
        self.label_idpresupuesto=tk.Label(self,text="ID_Permiso:")
        self.label_idpresupuesto.config(font=('Arial',12,'bold'))
        self.label_idpresupuesto.grid(row =1, column=0, padx=10,pady=10,columnspan=1)

       
        self.label_iduser=tk.Label(self,text="ID_Usuario:")
        self.label_iduser.config(font=('Arial',12,'bold'))
        self.label_iduser.grid(row =2, column=0, padx=10,pady=10)
    
        self.label_montoSolicitado=tk.Label(self,text="Monto Solicitado:")
        self.label_montoSolicitado.config(font=('Arial',12,'bold'))
        self.label_montoSolicitado.grid(row =3, column=0, padx=10,pady=10)

        
        self.label_estado=tk.Label(self,text="Estado:")
        self.label_estado.config(font=('Arial',12,'bold'))
        self.label_estado.grid(row =4, column=0,padx=10,pady=10)


        self.label_codPermiso=tk.Label(self,text="Codigo Permiso:")
        self.label_codPermiso.config(font=('Arial',12,'bold'))
        self.label_codPermiso.grid(row =5, column=0,padx=10,pady=10)


        self.label_fecha=tk.Label(self,text="Fecha(DD-MM-YYYY):")
        self.label_fecha.config(font=('Arial',12,'bold'))
        self.label_fecha.grid(row =6, column=0,padx=10,pady=10)

        self.label_idpresupuesto=tk.Label(self,text="ID_Presupuesto:")
        self.label_idpresupuesto.config(font=('Arial',12,'bold'))
        self.label_idpresupuesto.grid(row =7, column=0, padx=10,pady=10)


        #Entrys
        self.mi_idpermiso=tk.StringVar()
        self.entry_idpermiso=tk.Entry(self,textvariable=self.mi_idpermiso)
        self.entry_idpermiso.config(width=50, font=('Arial',12))
        self.entry_idpermiso.grid(row=1,column=1,padx=10,pady=10)


        self.mi_iduser=tk.StringVar()
        self.entry_iduser=tk.Entry(self,textvariable=self.mi_iduser)
        self.entry_iduser.config(width=50, font=('Arial',12))
        self.entry_iduser.grid(row=2,column=1)


        self.mi_montoSoli=tk.StringVar()
        self.entry_montoSoli=tk.Entry(self,textvariable=self.mi_montoSoli)
        self.entry_montoSoli.config(width=50, font=('Arial',12))
        self.entry_montoSoli.grid(row=3,column=1,padx=5,pady=10)
        
        self.mi_estado=tk.StringVar()
        self.entry_estado=tk.Entry(self,textvariable=self.mi_estado)
        self.entry_estado.config(width=50, font=('Arial',12))
        self.entry_estado.grid(row=4,column=1,padx=5,pady=10)

        self.mi_codPermiso=tk.StringVar()
        self.entry_codPermiso=tk.Entry(self,textvariable=self.mi_codPermiso)
        self.entry_codPermiso.config(width=50, font=('Arial',12))
        self.entry_codPermiso.grid(row=5,column=1,padx=5,pady=10)

        self.mi_fecha=tk.StringVar()
        self.entry_fecha=tk.Entry(self,textvariable=self.mi_fecha)
        self.entry_fecha.config(width=50, font=('Arial',12))
        self.entry_fecha.grid(row=6,column=1,padx=5,pady=10)


        self.mi_idPresupuesto=tk.StringVar()
        self.entry_idPresupuesto=tk.Entry(self,textvariable=self.mi_idPresupuesto)
        self.entry_idPresupuesto.config(width=50, font=('Arial',12))
        self.entry_idPresupuesto.grid(row=7,column=1,padx=5,pady=10)

       

        
        

        #Botones

        self.boton_nuevo=tk.Button(self,text="Nuevo",command=self.habilitar_campos)
        self.boton_nuevo.config(width=20, font=('Arial',12,'bold'),
        fg='White',bg='#4DCB03', cursor='hand2',activebackground='#43B302')
        self.boton_nuevo.grid(row=8,column=0,padx=10,pady=10)

        self.boton_guardar=tk.Button(self,text="Guardar",command=self.guarda_Datos)
        self.boton_guardar.config(width=20, font=('Arial',12,'bold'),
        fg='White',bg='#0157F2', cursor='hand2',activebackground='#003594')
        self.boton_guardar.grid(row=8,column=1,padx=10,pady=10)

        self.boton_cancelar=tk.Button(self,text="Cancelar",command=self.deshabilitar_campos)
        self.boton_cancelar.config(width=20, font=('Arial',12,'bold'),
        fg='White',bg='#F30000', cursor='hand2',activebackground='#8A1C1C')
        self.boton_cancelar.grid(row=8,column=2,padx=10,pady=10)

    def habilitar_campos(self):
        self.mi_idpermiso.set('')
        self.mi_iduser.set('')
        self.mi_montoSoli.set('')
        self.mi_estado.set('')
        self.mi_codPermiso.set('')
        self.mi_fecha.set('')
        self.mi_idPresupuesto.set('')
        

        self.entry_idpermiso.config(state='normal')
        self.entry_iduser.config(state='normal')
        self.entry_montoSoli.config(state='normal')
        self.entry_estado.config(state='normal')
        self.entry_codPermiso.config(state='normal')
        self.entry_fecha.config(state='normal')
        self.entry_idPresupuesto.config(state='normal')
        
        

    def deshabilitar_campos(self):

        self.mi_idpermiso.set('')
        self.mi_iduser.set('')
        self.mi_montoSoli.set('')
        self.mi_estado.set('')
        self.mi_codPermiso.set('')
        self.mi_fecha.set('')
        self.mi_idPresupuesto.set('')
        

        
        self.entry_idpermiso.config(state='disabled')
        self.entry_iduser.config(state='disabled')
        self.entry_montoSoli.config(state='disabled')
        self.entry_estado.config(state='disabled')
        self.entry_codPermiso.config(state='disabled')
        self.entry_fecha.config(state='disabled')
        self.entry_idPresupuesto.config(state='disabled')
        

        
    
    def guarda_Datos(self):
        self.Create_Permiso()
        self.deshabilitar_campos()

    def edit_Datos(self):
        self.Edit_Permiso()
        self.deshabilitar_campos()
    def delete_datos(self):
        self.Delete_Permiso()
        self.deshabilitar_campos()

   


    def obtener_datos_permiso(self):
        try:
            # Conexión a la base de datos
            connection = cx_Oracle.connect(user='ALONSO', password='123456', dsn='localhost:1521/orcl', encoding='UTF-8')

            # Llamada al procedimiento almacenado
            cursor = connection.cursor()
            p_cursor = cursor.var(cx_Oracle.CURSOR)
            cursor.callproc("ObtenerDatosPermiso", (p_cursor,))

            # Obtener los resultados del cursor
            result_set = p_cursor.getvalue()

            # Cerrar el cursor y la conexión
            # cursor.close()
            # connection.close()

            return result_set
        except cx_Oracle.Error as error:
            print(f"Error de Oracle: {error}")




    def mostrar_datos_en_tabla(self, result_set):
        # Limpiar la tabla antes de insertar nuevos datos
        for item in self.tabla.get_children():
            self.tabla.delete(item)

        # Insertar datos en la tabla
        for row in result_set:
            self.tabla.insert("", "end", values=row)

    def refrescarPermisos(self):
        result_set = self.obtener_datos_permiso()

        # Mostrar datos en la tabla
        self.mostrar_datos_en_tabla(result_set)

    def tabla_permisos(self):
        # Configuración de la tabla
        self.tabla = ttk.Treeview(self, columns=('ID_Permiso', 'ID_Usuario','Monto Solicitado','Estado','CodigoPermiso'))
        self.tabla.grid(row=9, column=0,columnspan=7)
        self.tabla.heading('#1', text='ID_Permiso')
        self.tabla.heading('#2', text='ID_Usuario')
        self.tabla.heading('#3', text='Monto Solicitado')
        self.tabla.heading('#4', text='Estado')
        self.tabla.heading('#5', text='CodigoPermiso')
        
        
        
        

        # Configuración de los botones
        self.boton_eliminar = tk.Button(self, text="Eliminar", command=self.delete_datos)
        self.boton_eliminar.config(width=20, font=('Arial', 12, 'bold'),
                                fg='White', bg='#FF0000', cursor='hand2', activebackground='#AE0000')
        self.boton_eliminar.grid(row=10, column=0, padx=10, pady=10)

        self.boton_editar = tk.Button(self, text="Editar", command=self.edit_Datos)
        self.boton_editar.config(width=20, font=('Arial', 12, 'bold'),
                                fg='White', bg='#4700BA', cursor='hand2', activebackground='#9468DA')
        self.boton_editar.grid(row=10, column=1, padx=10, pady=10)

        self.boton_refresh = tk.Button(self, text="Refrescar", command=self.refrescarPermisos)
        self.boton_refresh.config(width=20, font=('Arial', 12, 'bold'),
                                fg='White', bg='#4700BA', cursor='hand2', activebackground='#9468DA')
        self.boton_refresh.grid(row=10, column=2, padx=10, pady=10)


        

    def Create_Permiso(self):
        #Conexion
        try:
            connection = cx_Oracle.connect(user='ALONSO',password='123456',dsn='localhost:1521/orcl',encoding='UTF-8')
        except cx_Oracle.DatabaseError as db_error:
            print("Error de la base de datos:", db_error)
        except Exception as ex:
            print("Error inesperado:", ex)
        
        # Llamar al procedimiento almacenado
        cursor = connection.cursor()
        try:
            temp=self.mi_montoSoli.get()
            temp=int(temp)
            cursor.callproc("InsertarPermiso", (self.mi_idpermiso.get(),self.mi_iduser.get(),temp,self.mi_estado.get(),self.mi_codPermiso.get(),self.mi_fecha.get(),self.mi_idPresupuesto.get()))
            connection.commit()
            cursor.close()
        except cx_Oracle.DatabaseError as e:
        # Manejar excepciones específicas de Oracle
            error, = e.args
            if error.code == 1017:
                print("Credenciales de Oracle incorrectas.")
            elif error.code == 12541:
                print("No se pudo conectar al servidor Oracle.")
            elif error.code == 1:
                errorORA1()
            else:
                print(f"Error de Oracle: {error.message}")
        self.refrescarPermisos()

    
    
    def Edit_Permiso(self):
        #Conexion
        try:
            connection = cx_Oracle.connect(user='ALONSO',password='123456',dsn='localhost:1521/orcl',encoding='UTF-8')
        except cx_Oracle.DatabaseError as db_error:
            print("Error de la base de datos:", db_error)
        except Exception as ex:
            print("Error inesperado:", ex)
        try:
            # Llamar al procedimiento almacenado
            cursor = connection.cursor()
            temp=self.mi_montoSoli.get()
            temp=float(temp)
            cursor.callproc("EditarPermiso",(self.mi_idpermiso.get(),self.mi_iduser.get(),temp,self.mi_estado.get(),self.mi_codPermiso.get(),self.mi_fecha.get(),self.mi_idPresupuesto.get()))
            connection.commit()
        except cx_Oracle.DatabaseError as e:
        # Manejar excepciones específicas de Oracle
            error, = e.args
            if error.code == 1017:
                print("Credenciales de Oracle incorrectas.")
            elif error.code == 12541:
                print("No se pudo conectar al servidor Oracle.")
            else:
                print(f"Error de Oracle: {error.message}")
        self.refrescarPermisos()
        

    def Delete_Permiso(self):
        #Conexion
        try:
            connection = cx_Oracle.connect(user='ALONSO',password='123456',dsn='localhost:1521/orcl',encoding='UTF-8')
        except cx_Oracle.DatabaseError as db_error:
            print("Error de la base de datos:", db_error)
        except Exception as ex:
            print("Error inesperado:", ex)
        try:
            # Llamar al procedimiento almacenado
            cursor = connection.cursor()
            temp=self.mi_idpermiso.get()
            num=int(temp)
            cursor.callproc("EliminarPermiso", (num,))
            connection.commit()
            if cursor.rowcount > 0:
                # Mostrar ventana de éxito
                mostrar_ventana_exito()
            else:
                # Mostrar ventana de fallo (dato no encontrado)
                mostrar_ventana_fallo("El dato no existe")
        except cx_Oracle.DatabaseError as e:
            # Manejar excepciones específicas de Oracle
            error, = e.args
            if error.code == 1017:
                print("Credenciales de Oracle incorrectas.")
            elif error.code == 12541:
                print("No se pudo conectar al servidor Oracle.")
            else:
                print(f"Error de Oracle: {error.message}")

            # Mostrar ventana de fallo
            self.mostrar_ventana_fallo("No se pudo agregar el dato")
        finally:
            # Cerrar el cursor y la conexión en el bloque finally
            if cursor:
                cursor.close()
        self.refrescarPermisos()
   