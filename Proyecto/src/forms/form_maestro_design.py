import tkinter as tk
from tkinter import font
from config import COLOR_BARRA_SUPERIOR, COLOR_MENU_LATERAL, COLOR_CUERPO_PRINCIPAL, COLOR_MENU_CURSOR_ENCIMA
import util.util_ventana as util_ventana
import util.util_imagenes as util_img
from PIL import ImageTk, Image
from forms.form_sitio_construccion import FormularioSitioConstruccion
import cx_Oracle
from tkinter import ttk


def mostrar_ventana_exito():
        # Crear la ventana de éxito
        ventana_exito = tk.Toplevel()
        ventana_exito.title("Éxito")

        # Etiqueta con el mensaje de éxito
        label_exito = tk.Label(ventana_exito, text="¡Dato eliminado correctamente!", padx=20, pady=20)
        label_exito.pack()

        # Botón Aceptar para cerrar la ventana
        boton_aceptar = tk.Button(ventana_exito, text="Aceptar", command=ventana_exito.destroy)
        boton_aceptar.pack()
def errorORA1():
    # Crear la ventana de éxito
        error_ora0001 = tk.Toplevel()
        error_ora0001.title("Error")

        # Etiqueta con el mensaje de éxito
        label_error = tk.Label(error_ora0001, text="¡Ya existe un dato con ese ID\nIntenta con otro!", padx=20, pady=20)
        label_error.pack()

        # Botón Aceptar para cerrar la ventana
        boton_aceptar = tk.Button(error_ora0001, text="Aceptar", command=error_ora0001.destroy)
        boton_aceptar.pack()

def mostrar_ventana_fallo(mensaje):
        # Crear la ventana de fallo
        ventana_fallo = tk.Toplevel()
        ventana_fallo.title("Fallo")

        # Etiqueta con el mensaje de fallo
        label_fallo = tk.Label(ventana_fallo, text=mensaje, padx=20, pady=20)
        label_fallo.pack()

        # Botón Aceptar para cerrar la ventana
        boton_aceptar = tk.Button(ventana_fallo, text="Aceptar", command=ventana_fallo.destroy)
        boton_aceptar.pack()
#Crear la clase main para generar la ventana
class FormularioMaestroDesign(tk.Tk):

    def __init__(self):
        super().__init__()
        
        self.logo = util_img.leer_imagen("./src/imagenes/logoFondo.png", (500, 500))
        self.perfil = util_img.leer_imagen("./src/imagenes/logoPantera.png", (150, 150))
        self.img_sitio_construccion=util_img.leer_imagen("./src/imagenes/sitio_construccion.png", (150, 150))
        self.config_window()
        self.paneles()
        self.controles_barra_superior()        
        self.controles_menu_lateral()
        self.controles_cuerpo()
        
    
    def config_window(self):
        # Configuración inicial de la ventana
        self.title('Sistema Presupuestos')
        self.iconbitmap("./src/imagenes/money.ico")
        w, h = 1024, 600        
        util_ventana.centrar_ventana(self, w, h)        

    def paneles(self):        
         # Crear paneles: barra superior, menú lateral y cuerpo principal
        self.barra_superior = tk.Frame(
            self, bg=COLOR_BARRA_SUPERIOR, height=50)
        self.barra_superior.pack(side=tk.TOP, fill='both')      

        self.menu_lateral = tk.Frame(self, bg=COLOR_MENU_LATERAL, width=150)
        self.menu_lateral.pack(side=tk.LEFT, fill='both', expand=False) 
        
        self.cuerpo_principal = tk.Frame(
            self, bg=COLOR_CUERPO_PRINCIPAL)
        self.cuerpo_principal.pack(side=tk.RIGHT, fill='both', expand=True)
    
    def controles_barra_superior(self):
        # Configuración de la barra superior
        font_awesome = font.Font(family='FontAwesome', size=12)

        # Etiqueta de título
        self.labelTitulo = tk.Label(self.barra_superior, text="Sistema de Gestion")
        self.labelTitulo.config(fg="#fff", font=(
            "Roboto", 15), bg=COLOR_BARRA_SUPERIOR, pady=10, width=16)
        self.labelTitulo.pack(side=tk.LEFT)

        # Botón del menú lateral
        self.imagenMenu = Image.open("./src/imagenes/money.ico").resize((30, 30), Image.BICUBIC)
        self.imagenMenu_tk = ImageTk.PhotoImage(self.imagenMenu)

        self.buttonMenuLateral = tk.Button(self.barra_superior, font=font_awesome,
        command=self.toggle_panel, bd=0, bg=COLOR_BARRA_SUPERIOR, fg="white",
        image=self.imagenMenu_tk)
        self.buttonMenuLateral.pack(side=tk.LEFT)


        # Etiqueta de informacion
        self.labelTitulo = tk.Label(
            self.barra_superior, text="El mejor en Presupuestos")
        self.labelTitulo.config(fg="#fff", font=(
            "Roboto", 10), bg=COLOR_BARRA_SUPERIOR, padx=10, width=20)
        self.labelTitulo.pack(side=tk.RIGHT)
    
    def controles_menu_lateral(self):
        # Configuración del menú lateral
        ancho_menu = 20
        alto_menu = 2
        font_awesome = font.Font(family='FontAwesome', size=15)
         
         # Etiqueta de foto de perfil
        self.labelPerfil = tk.Label(
            self.menu_lateral, image=self.perfil, bg=COLOR_MENU_LATERAL)
        self.labelPerfil.pack(side=tk.TOP, pady=10)
        

        # Botones del menú lateral
        
        self.buttonCentroCostos = tk.Button(self.menu_lateral)        
        self.buttonComprasGastos = tk.Button(self.menu_lateral)        
        self.buttonLiquidacion = tk.Button(self.menu_lateral)
        self.buttonModificaciones = tk.Button(self.menu_lateral)        
        self.buttonPermisos = tk.Button(self.menu_lateral)
        self.buttonPresupuesto = tk.Button(self.menu_lateral)
        self.buttonRubro = tk.Button(self.menu_lateral)
        self.buttonUsuario = tk.Button(self.menu_lateral)

      
        #Informacion de los botones en una tupla
        buttons_info = [
            ("Centro de Costos",  "\uf109", self.buttonCentroCostos,self.interfaz_cc),
            ("Compras Gastos",  "\uf109", self.buttonComprasGastos,self.abrirEnconstruccion),
            ("Liquidacion",  "\uf109", self.buttonLiquidacion,self.interfaz_liquidacion),
            ("Modificaciones",  "\uf109", self.buttonModificaciones,self.abrirEnconstruccion),
            ("Permisos",  "\uf109", self.buttonPermisos,self.interfaz_permiso),
            ("Presupuestos", "\uf109", self.buttonPresupuesto,self.interfaz_presupesto),
            ("Rubros", "\uf109", self.buttonRubro,self.interfaz_rubro),
            ("Usuarios", "\uf109", self.buttonUsuario,self.interfaz_user),
        ]

        # Se recorre y se llena la tupla
        for text, icon, button,comando in buttons_info:
            self.configurar_boton_menu(button, text, icon, font_awesome, ancho_menu, alto_menu,comando)
    
    def controles_cuerpo(self):
        # Imagen en el cuerpo principal
        label = tk.Label(self.cuerpo_principal, image=self.logo,
                         bg=COLOR_CUERPO_PRINCIPAL)
        label.place(x=0, y=0, relwidth=1, relheight=1)
    #comando
    def configurar_boton_menu(self, button, text, icon, font_awesome, ancho_menu, alto_menu,comando):
        button.config(text=f"  {icon}    {text}", anchor="w", font=font_awesome,
                      bd=0, bg=COLOR_MENU_LATERAL, fg="white", width=ancho_menu, height=alto_menu,command=comando)
        button.pack(side=tk.TOP)
        self.bind_hover_events(button)

    def bind_hover_events(self, button):
        # Asociar eventos Enter y Leave con la función dinámica
        button.bind("<Enter>", lambda event: self.on_enter(event, button))
        button.bind("<Leave>", lambda event: self.on_leave(event, button))

    def on_enter(self, event, button):
        # Cambiar estilo al pasar el ratón por encima
        button.config(bg=COLOR_MENU_CURSOR_ENCIMA, fg='white')

    def on_leave(self, event, button):
        # Restaurar estilo al salir el ratón
        button.config(bg=COLOR_MENU_LATERAL, fg='white')

    def toggle_panel(self):
        # Alternar visibilidad del menú lateral
        if self.menu_lateral.winfo_ismapped():
            self.menu_lateral.pack_forget()
        else:
            self.menu_lateral.pack(side=tk.LEFT, fill='y')


    #Construccion
    def abrirEnconstruccion(self):   
        self.limpiar_panel(self.cuerpo_principal)     
        FormularioSitioConstruccion(self.cuerpo_principal,self.img_sitio_construccion) 
    
    def limpiar_panel(self,panel):
    # Función para limpiar el contenido del panel
        for widget in panel.winfo_children():
            widget.destroy()
 
    def interfaz_rubro(self):
        mi_frame = Frame_Rubro(self)
        mi_frame.mainloop()        
    def interfaz_cc(self):
        mi_frame = Frame_CC(self)
        mi_frame.mainloop()
    def interfaz_user(self):
        mi_frame=Frame_User(self)
        mi_frame.mainloop()     

    def interfaz_presupesto(self):
        mi_frame = Frame_Presupuesto(self)
        mi_frame.mainloop()
    def interfaz_permiso(self):
        mi_frame = Frame_Permiso(self)
        mi_frame.mainloop()
    def interfaz_liquidacion(self):
        mi_frame = Frame_Liquidacion(self)
        mi_frame.mainloop()
# **********************************************************************************************************************

#Interfaz Grafica para la tabla de Rubros
class Frame_Rubro(tk.Toplevel):
    
    
    def __init__(self,root=None):
        super().__init__(root, width=200, height=200) 
        self.title("Rubros")
        self.root=root
        # self.pack()
        self.rubros()
        self.deshabilitar_campos()
        self.tabla_rubros()
        self.refrescarRubro()
       
       
        

    
    def rubros(self):
        #Labels
        self.label_idRubro=tk.Label(self,text="ID_Rubro:")
        self.label_idRubro.config(font=('Arial',12,'bold'))
        self.label_idRubro.grid(row =0, column=0, padx=10,pady=10)

        self.label_nombre=tk.Label(self,text="Nombre:")
        self.label_nombre.config(font=('Arial',12,'bold'))
        self.label_nombre.grid(row =1, column=0,padx=10,pady=10)

       

        #Entrys
        self.mi_idRubro=tk.StringVar()
        self.entry_idRubro=tk.Entry(self,textvariable=self.mi_idRubro)
        self.entry_idRubro.config(width=50, font=('Arial',12))
        self.entry_idRubro.grid(row=0,column=1,padx=10,pady=10, columnspan=2)
        
        self.mi_nombre=tk.StringVar()
        self.entry_nombre=tk.Entry(self,textvariable=self.mi_nombre)
        self.entry_nombre.config(width=50, font=('Arial',12))
        self.entry_nombre.grid(row=1,column=1,padx=10,pady=10, columnspan=2)

        self.mi_idcc=tk.StringVar()
        self.entry_idcc=tk.Entry(self,textvariable=self.mi_idcc)
        self.entry_idcc.config(width=50, font=('Arial',12))
        self.entry_idcc.grid(row=2,column=1,padx=10,pady=10, columnspan=2)
        

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
        fg='White',bg='#F30000', cursor='hand2',activebackground='#8A1C1C')
        self.boton_cancelar.grid(row=3,column=2,padx=10,pady=10)

    def habilitar_campos(self):
        self.mi_nombre.set('')
        self.mi_idRubro.set('')
        self.entry_nombre.config(state='normal')
        self.entry_idRubro.config(state='normal')
        self.boton_guardar.config(state='normal')
        self.boton_cancelar.config(state='normal')

    def deshabilitar_campos(self):

        self.mi_nombre.set('')
        self.mi_idRubro.set('')
        self.entry_idRubro.config(state='disabled')
        self.entry_nombre.config(state='disabled')
        self.boton_guardar.config(state='disabled')
        self.boton_cancelar.config(state='disabled')
    
    def guarda_Datos(self):
        self.Create_Rubro()
        self.deshabilitar_campos()

    def edit_Datos(self):
        self.Edit_Rubro()
        self.deshabilitar_campos()
    def delete_datos(self):
        self.Delete_Rubro()
        self.deshabilitar_campos()

   


    def obtener_datos_rubro(self):
        try:
            # Conexión a la base de datos
            connection = cx_Oracle.connect(user='ALONSO', password='123456', dsn='localhost:1521/orcl', encoding='UTF-8')

            # Llamada al procedimiento almacenado
            cursor = connection.cursor()
            p_cursor = cursor.var(cx_Oracle.CURSOR)
            cursor.callproc("ObtenerDatosRubro", (p_cursor,))

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

    def refrescarRubro(self):
        result_set = self.obtener_datos_rubro()

        # Mostrar datos en la tabla
        self.mostrar_datos_en_tabla(result_set)

    def tabla_rubros(self):
        # Configuración de la tabla
        self.tabla = ttk.Treeview(self, columns=('ID_Rubro', 'Nombre'))
        self.tabla.grid(row=4, column=0, columnspan=3)
        self.tabla.heading('#1', text='ID_Rubro')
        self.tabla.heading('#2', text='Nombre')

        # Configuración de los botones
        self.boton_eliminar = tk.Button(self, text="Eliminar", command=self.delete_datos)
        self.boton_eliminar.config(width=20, font=('Arial', 12, 'bold'),
                                fg='White', bg='#FF0000', cursor='hand2', activebackground='#AE0000')
        self.boton_eliminar.grid(row=5, column=0, padx=10, pady=10)

        self.boton_editar = tk.Button(self, text="Editar", command=self.edit_Datos)
        self.boton_editar.config(width=20, font=('Arial', 12, 'bold'),
                                fg='White', bg='#4700BA', cursor='hand2', activebackground='#9468DA')
        self.boton_editar.grid(row=5, column=1, padx=10, pady=10)

        self.boton_refresh = tk.Button(self, text="Refrescar", command=self.refrescarRubro)
        self.boton_refresh.config(width=20, font=('Arial', 12, 'bold'),
                                fg='White', bg='#4700BA', cursor='hand2', activebackground='#9468DA')
        self.boton_refresh.grid(row=5, column=2, padx=10, pady=10)
        self.refrescarRubro()


        

    def Create_Rubro(self):
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
            cursor.callproc("InsertarRubro", (self.mi_idRubro.get(),self.mi_nombre.get()))
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
        self.refrescarRubro()

    
    
    def Edit_Rubro(self):
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
            cursor.callproc("EditarRubro", (self.mi_idRubro.get(),self.mi_nombre.get()))
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
        self.refrescarRubro()
        

    def Delete_Rubro(self):
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
            temp=self.mi_idRubro.get()
            num=int(temp)
            cursor.callproc("EliminarRubro", (num,))
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
        self.refrescarRubro()
       
     
#*********************************************************************************
#Interfaz Grafica para la tabla de Centro de Costo
class Frame_CC(tk.Toplevel):
    
    
    def __init__(self,root=None):
        super().__init__(root, width=200, height=200) 
        self.title("Centro de Costos")
        self.root=root
        # self.pack()
        self.centroDeCostos()
        self.deshabilitar_campos()
        self.tabla_cc()
        self.refrescarCC()
       
        

    
    def centroDeCostos(self):
        #Labels
        self.label_idcc=tk.Label(self,text="ID_CentroDeCosto:")
        self.label_idcc.config(font=('Arial',12,'bold'))
        self.label_idcc.grid(row =0, column=0, padx=10,pady=10)

        self.label_nombre=tk.Label(self,text="Nombre:")
        self.label_nombre.config(font=('Arial',12,'bold'))
        self.label_nombre.grid(row =1, column=0,padx=10,pady=10)

        self.label_idcc=tk.Label(self,text="ID_Padre:")
        self.label_idcc.config(font=('Arial',12,'bold'))
        self.label_idcc.grid(row =2, column=0, padx=10,pady=10)


        #Entrys
        self.mi_idcc=tk.StringVar()
        self.entry_idcc=tk.Entry(self,textvariable=self.mi_idcc)
        self.entry_idcc.config(width=50, font=('Arial',12))
        self.entry_idcc.grid(row=0,column=1,padx=10,pady=10, columnspan=2)
        
        self.mi_nombre=tk.StringVar()
        self.entry_nombre=tk.Entry(self,textvariable=self.mi_nombre)
        self.entry_nombre.config(width=50, font=('Arial',12))
        self.entry_nombre.grid(row=1,column=1,padx=10,pady=10, columnspan=2)

        self.mi_idpadre=tk.StringVar()
        self.entry_idpadre=tk.Entry(self,textvariable=self.mi_idpadre)
        self.entry_idpadre.config(width=50, font=('Arial',12))
        self.entry_idpadre.grid(row=2,column=1,padx=10,pady=10, columnspan=2)
        

        #Botones

        self.boton_nuevo=tk.Button(self,text="Nuevo",command=self.habilitar_campos)
        self.boton_nuevo.config(width=20, font=('Arial',12,'bold'),
        fg='White',bg='#4DCB03', cursor='hand2',activebackground='#43B302')
        self.boton_nuevo.grid(row=5,column=0,padx=10,pady=10)

        self.boton_guardar=tk.Button(self,text="Guardar",command=self.guarda_Datos)
        self.boton_guardar.config(width=20, font=('Arial',12,'bold'),
        fg='White',bg='#0157F2', cursor='hand2',activebackground='#003594')
        self.boton_guardar.grid(row=5,column=1,padx=10,pady=10)

        self.boton_cancelar=tk.Button(self,text="Cancelar",command=self.deshabilitar_campos)
        self.boton_cancelar.config(width=20, font=('Arial',12,'bold'),
        fg='White',bg='#F30000', cursor='hand2',activebackground='#8A1C1C')
        self.boton_cancelar.grid(row=5,column=2,padx=10,pady=10)

    def habilitar_campos(self):
        self.mi_nombre.set('')
        self.mi_idcc.set('')
        self.mi_idpadre.set('')
        self.entry_nombre.config(state='normal')
        self.entry_idpadre.config(state='normal')
        self.entry_idcc.config(state='normal')
        self.boton_guardar.config(state='normal')
        self.boton_cancelar.config(state='normal')

    def deshabilitar_campos(self):

        self.mi_nombre.set('')
        self.mi_idcc.set('')
        self.mi_idpadre.set('')
        self.entry_idcc.config(state='disabled')
        self.entry_idpadre.config(state='disabled')
        self.entry_nombre.config(state='disabled')
        self.boton_guardar.config(state='disabled')
        self.boton_cancelar.config(state='disabled')
    
    def guarda_Datos(self):
        self.Create_CC()
        self.deshabilitar_campos()

    def edit_Datos(self):
        self.Edit_CC()
        self.deshabilitar_campos()
    def delete_datos(self):
        self.Delete_CC()
        self.deshabilitar_campos()

   


    def obtener_datos_cc(self):
        try:
            # Conexión a la base de datos
            connection = cx_Oracle.connect(user='ALONSO', password='123456', dsn='localhost:1521/orcl', encoding='UTF-8')

            # Llamada al procedimiento almacenado
            cursor = connection.cursor()
            p_cursor = cursor.var(cx_Oracle.CURSOR)
            cursor.callproc("ObtenerDatosCentroDeCosto", (p_cursor,))

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

    def refrescarCC(self):
        result_set = self.obtener_datos_cc()

        # Mostrar datos en la tabla
        self.mostrar_datos_en_tabla(result_set)

    def tabla_cc(self):
        # Configuración de la tabla
        self.tabla = ttk.Treeview(self, columns=('ID_CentroDeCosto', 'Nombre','ID_Padre'))
        self.tabla.grid(row=6, column=0, columnspan=3)
        self.tabla.heading('#1', text='ID_CentroDeCosto')
        self.tabla.heading('#2', text='Nombre')
        self.tabla.heading('#3', text='ID_Padre')

        # Configuración de los botones
        self.boton_eliminar = tk.Button(self, text="Eliminar", command=self.delete_datos)
        self.boton_eliminar.config(width=20, font=('Arial', 12, 'bold'),
                                fg='White', bg='#FF0000', cursor='hand2', activebackground='#AE0000')
        self.boton_eliminar.grid(row=7, column=0, padx=10, pady=10)

        self.boton_editar = tk.Button(self, text="Editar", command=self.edit_Datos)
        self.boton_editar.config(width=20, font=('Arial', 12, 'bold'),
                                fg='White', bg='#4700BA', cursor='hand2', activebackground='#9468DA')
        self.boton_editar.grid(row=7, column=1, padx=10, pady=10)

        self.boton_refresh = tk.Button(self, text="Refrescar", command=self.refrescarCC)
        self.boton_refresh.config(width=20, font=('Arial', 12, 'bold'),
                                fg='White', bg='#4700BA', cursor='hand2', activebackground='#9468DA')
        self.boton_refresh.grid(row=7, column=2, padx=10, pady=10)


        

    def Create_CC(self):
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
            cursor.callproc("InsertarCentroDeCosto", (self.mi_idcc.get(),self.mi_nombre.get(),self.mi_idpadre.get()))
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
        self.refrescarCC()

    
    
    def Edit_CC(self):
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
            cursor.callproc("EditarCentroDeCosto", (self.mi_idcc.get(),self.mi_nombre.get(),self.mi_idpadre.get()))
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
        self.refrescarCC()
        

    def Delete_CC(self):
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
            temp=self.mi_idcc.get()
            num=int(temp)
            cursor.callproc("EliminarCentroDeCosto", (num,))
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
        self.refrescarCC()
       

#*********************************************************************************       

#Interfaz Grafica para la tabla de Usuarios
class Frame_User(tk.Toplevel):
    
    
    def __init__(self,root=None):
        super().__init__(root, width=200, height=200) 
        self.title("Usuarios")
        self.root=root
        # self.pack()
        self.Usuarios()
        self.deshabilitar_campos()
        self.tabla_usuarios()
        self.refrescarUsuarios()
       
        

    
    def Usuarios(self):
        #Labels
        self.label_iduser=tk.Label(self,text="ID_Usuario:")
        self.label_iduser.config(font=('Arial',12,'bold'))
        self.label_iduser.grid(row =0, column=0, padx=10,pady=10)

        self.label_nombre=tk.Label(self,text="Nombre:")
        self.label_nombre.config(font=('Arial',12,'bold'))
        self.label_nombre.grid(row =1, column=0,padx=10,pady=10)

        self.label_idrol=tk.Label(self,text="Rol:")
        self.label_idrol.config(font=('Arial',12,'bold'))
        self.label_idrol.grid(row =2, column=0, padx=10,pady=10)

        self.label_idcc=tk.Label(self,text="ID_CentroDeCosto:")
        self.label_idcc.config(font=('Arial',12,'bold'))
        self.label_idcc.grid(row =3, column=0, padx=10,pady=10)


        #Entrys
        self.mi_iduser=tk.StringVar()
        self.entry_iduser=tk.Entry(self,textvariable=self.mi_iduser)
        self.entry_iduser.config(width=50, font=('Arial',12))
        # self.entry_iduser.grid(row=0,column=1,padx=10,pady=10, columnspan=2)
        # self.label_iduser=tk.Label(self,text="ID_Usuario:")
        # self.label_iduser.config(font=('Arial',12,'bold'))
        # self.label_iduser.grid(row =0, column=0, padx=10,pady=10)

        
        self.mi_nombre=tk.StringVar()
        self.entry_nombre=tk.Entry(self,textvariable=self.mi_nombre)
        self.entry_nombre.config(width=50, font=('Arial',12))
        self.entry_nombre.grid(row=1,column=1,padx=10,pady=10, columnspan=2)

        self.mi_rol=tk.StringVar()
        self.entry_rol=tk.Entry(self,textvariable=self.mi_rol)
        self.entry_rol.config(width=50, font=('Arial',12))
        self.entry_rol.grid(row=2,column=1,padx=10,pady=10, columnspan=2)

        self.mi_idcc=tk.StringVar()
        self.entry_idcc=tk.Entry(self,textvariable=self.mi_idcc)
        self.entry_idcc.config(width=50, font=('Arial',12))
        self.entry_idcc.grid(row=3,column=1,padx=10,pady=10, columnspan=2)
        

        #Botones

        self.boton_nuevo=tk.Button(self,text="Nuevo",command=self.habilitar_campos)
        self.boton_nuevo.config(width=20, font=('Arial',12,'bold'),
        fg='White',bg='#4DCB03', cursor='hand2',activebackground='#43B302')
        self.boton_nuevo.grid(row=6,column=0,padx=10,pady=10)

        self.boton_guardar=tk.Button(self,text="Guardar",command=self.guarda_Datos)
        self.boton_guardar.config(width=20, font=('Arial',12,'bold'),
        fg='White',bg='#0157F2', cursor='hand2',activebackground='#003594')
        self.boton_guardar.grid(row=6,column=1,padx=10,pady=10)

        self.boton_cancelar=tk.Button(self,text="Cancelar",command=self.deshabilitar_campos)
        self.boton_cancelar.config(width=20, font=('Arial',12,'bold'),
        fg='White',bg='#F30000', cursor='hand2',activebackground='#8A1C1C')
        self.boton_cancelar.grid(row=6,column=2,padx=10,pady=10)

    def habilitar_campos(self):
        self.mi_nombre.set('')
        self.mi_rol.set('')
        self.mi_idcc.set('')
        self.mi_iduser.set('')
        self.entry_nombre.config(state='normal')
        self.entry_iduser.config(state='normal')
        self.entry_idcc.config(state='normal')
        self.entry_rol.config(state='normal')
        self.boton_guardar.config(state='normal')
        self.boton_cancelar.config(state='normal')

    def deshabilitar_campos(self):

        self.mi_nombre.set('')
        self.mi_idcc.set('')
        self.mi_iduser.set('')
        self.mi_rol.set('')
        
        self.entry_idcc.config(state='disabled')
        self.entry_iduser.config(state='disabled')
        self.entry_nombre.config(state='disabled')
        self.entry_rol.config(state='disabled')
        self.boton_guardar.config(state='disabled')
        self.boton_cancelar.config(state='disabled')
    
    def guarda_Datos(self):
        self.Create_User()
        self.deshabilitar_campos()

    def edit_Datos(self):
        self.Edit_User()
        self.deshabilitar_campos()
    def delete_datos(self):
        self.Delete_User()
        self.deshabilitar_campos()

   


    def obtener_datos_user(self):
        try:
            # Conexión a la base de datos
            connection = cx_Oracle.connect(user='ALONSO', password='123456', dsn='localhost:1521/orcl', encoding='UTF-8')

            # Llamada al procedimiento almacenado
            cursor = connection.cursor()
            p_cursor = cursor.var(cx_Oracle.CURSOR)
            cursor.callproc("ObtenerDatosUsuario", (p_cursor,))

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

    def refrescarUsuarios(self):
        result_set = self.obtener_datos_user()

        # Mostrar datos en la tabla
        self.mostrar_datos_en_tabla(result_set)

    def tabla_usuarios(self):
        # Configuración de la tabla
        self.tabla = ttk.Treeview(self, columns=('ID_Usuario', 'Nombre','Rol','ID_CentroDeCosto'))
        self.tabla.grid(row=7, column=0, columnspan=3)
        self.tabla.heading('#1', text='ID_Usuario')
        self.tabla.heading('#2', text='Nombre')
        self.tabla.heading('#3', text='Rol')
        self.tabla.heading('#4', text='ID_CentroDeCosto')
        

        # Configuración de los botones
        self.boton_eliminar = tk.Button(self, text="Eliminar", command=self.delete_datos)
        self.boton_eliminar.config(width=20, font=('Arial', 12, 'bold'),
                                fg='White', bg='#FF0000', cursor='hand2', activebackground='#AE0000')
        self.boton_eliminar.grid(row=8, column=0, padx=10, pady=10)

        self.boton_editar = tk.Button(self, text="Editar", command=self.edit_Datos)
        self.boton_editar.config(width=20, font=('Arial', 12, 'bold'),
                                fg='White', bg='#4700BA', cursor='hand2', activebackground='#9468DA')
        self.boton_editar.grid(row=8, column=1, padx=10, pady=10)

        self.boton_refresh = tk.Button(self, text="Refrescar", command=self.refrescarUsuarios)
        self.boton_refresh.config(width=20, font=('Arial', 12, 'bold'),
                                fg='White', bg='#4700BA', cursor='hand2', activebackground='#9468DA')
        self.boton_refresh.grid(row=8, column=2, padx=10, pady=10)


        

    def Create_User(self):
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
            cursor.callproc("InsertarUsuario", (self.mi_iduser.get(),self.mi_nombre.get(),self.mi_rol.get(),self.mi_idcc.get()))
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
        self.refrescarUsuarios()

    
    
    def Edit_User(self):
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
            cursor.callproc("EditarUsuario", (self.mi_iduser.get(),self.mi_nombre.get(),self.mi_rol.get(),self.mi_idcc.get()))
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
        self.refrescarUsuarios()
        

    def Delete_User(self):
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
            temp=self.mi_iduser.get()
            num=int(temp)
            cursor.callproc("EliminarUsuario", (num,))
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
        self.refrescarUsuarios()
   

#*******************************************************************************************************8
#Interfaz Grafica para la tabla de Presupuestos
class Frame_Presupuesto(tk.Toplevel):
    
    
    def __init__(self,root=None):
        super().__init__(root, width=200, height=200) 
        self.title("Presupuestos")
        self.root=root
        # self.pack()
        self.Presupuestos()
        self.deshabilitar_campos()
        self.tabla_presupuestos()
        self.refrescarPresupuestos()
       
        

    
    def Presupuestos(self):
        #Labels
        self.label_idpresupuesto=tk.Label(self,text="ID_Presupuesto:")
        self.label_idpresupuesto.config(font=('Arial',12,'bold'))
        self.label_idpresupuesto.grid(row =0, column=0, padx=10,pady=10)
        
        self.label_idcc=tk.Label(self,text="ID_CentroDeCosto:")
        self.label_idcc.config(font=('Arial',12,'bold'))
        self.label_idcc.grid(row =1, column=0, padx=10,pady=10)

       
        self.label_idRubro=tk.Label(self,text="ID_Rubro:")
        self.label_idRubro.config(font=('Arial',12,'bold'))
        self.label_idRubro.grid(row =2, column=0, padx=10,pady=10)

        
        self.label_monto=tk.Label(self,text="Monto:")
        self.label_monto.config(font=('Arial',12,'bold'))
        self.label_monto.grid(row =3, column=0,padx=10,pady=10)


        self.label_periodo=tk.Label(self,text="Periodo:")
        self.label_periodo.config(font=('Arial',12,'bold'))
        self.label_periodo.grid(row =4, column=0,padx=10,pady=10)
        


        #Entrys
        self.mi_idpresupuesto=tk.StringVar()
        self.entry_idpresupuesto=tk.Entry(self,textvariable=self.mi_idpresupuesto)
        self.entry_idpresupuesto.config(width=50, font=('Arial',12))
        self.entry_idpresupuesto.grid(row=0,column=1,padx=10,pady=10, columnspan=3)

        self.mi_idcc=tk.StringVar()
        self.entry_idcc=tk.Entry(self,textvariable=self.mi_idcc)
        self.entry_idcc.config(width=50, font=('Arial',12))
        self.entry_idcc.grid(row=1,column=1,padx=5,pady=10, columnspan=3)
        
        self.mi_idRubro=tk.StringVar()
        self.entry_idRubro=tk.Entry(self,textvariable=self.mi_idRubro)
        self.entry_idRubro.config(width=50, font=('Arial',12))
        self.entry_idRubro.grid(row=2,column=1,padx=5,pady=10, columnspan=3)


        self.mi_monto=tk.StringVar()
        self.entry_monto=tk.Entry(self,textvariable=self.mi_monto)
        self.entry_monto.config(width=50, font=('Arial',12))
        self.entry_monto.grid(row=3,column=1,padx=5,pady=10, columnspan=3)

       

        self.mi_periodo=tk.StringVar()
        self.entry_periodo=tk.Entry(self,textvariable=self.mi_periodo)
        self.entry_periodo.config(width=50, font=('Arial',12))
        self.entry_periodo.grid(row=4,column=1,padx=5,pady=10, columnspan=3)
        

        #Botones

        self.boton_nuevo=tk.Button(self,text="Nuevo",command=self.habilitar_campos)
        self.boton_nuevo.config(width=20, font=('Arial',12,'bold'),
        fg='White',bg='#4DCB03', cursor='hand2',activebackground='#43B302')
        self.boton_nuevo.grid(row=6,column=0,padx=10,pady=10)

        self.boton_guardar=tk.Button(self,text="Guardar",command=self.guarda_Datos)
        self.boton_guardar.config(width=20, font=('Arial',12,'bold'),
        fg='White',bg='#0157F2', cursor='hand2',activebackground='#003594')
        self.boton_guardar.grid(row=6,column=1,padx=10,pady=10)

        self.boton_cancelar=tk.Button(self,text="Cancelar",command=self.deshabilitar_campos)
        self.boton_cancelar.config(width=20, font=('Arial',12,'bold'),
        fg='White',bg='#F30000', cursor='hand2',activebackground='#8A1C1C')
        self.boton_cancelar.grid(row=6,column=2,padx=10,pady=10)

    def habilitar_campos(self):
        self.mi_idpresupuesto.set('')
        self.mi_idcc.set('')
        self.mi_idRubro.set('')
        self.mi_monto.set('')
        self.mi_periodo.set('')
        self.entry_idpresupuesto.config(state='normal')
        self.entry_idcc.config(state='normal')
        self.entry_idRubro.config(state='normal')
        self.entry_monto.config(state='normal')
        self.entry_periodo.config(state='normal')
        self.boton_guardar.config(state='normal')
        self.boton_cancelar.config(state='normal')

    def deshabilitar_campos(self):

        self.mi_idpresupuesto.set('')
        self.mi_idcc.set('')
        self.mi_idRubro.set('')
        self.mi_monto.set('')
        self.mi_periodo.set('')
        
        self.entry_idpresupuesto.config(state='disabled')
        self.entry_idcc.config(state='disabled')
        self.entry_idRubro.config(state='disabled')
        self.entry_monto.config(state='disabled')
        self.entry_periodo.config(state='disabled')
        self.boton_guardar.config(state='disabled')
        self.boton_cancelar.config(state='disabled')
        
    
    def guarda_Datos(self):
        self.Create_Presupuesto()
        self.deshabilitar_campos()

    def edit_Datos(self):
        self.Edit_Presupuesto()
        self.deshabilitar_campos()
    def delete_datos(self):
        self.Delete_Presupuesto()
        self.deshabilitar_campos()

   


    def obtener_datos_presupuesto(self):
        try:
            # Conexión a la base de datos
            connection = cx_Oracle.connect(user='ALONSO', password='123456', dsn='localhost:1521/orcl', encoding='UTF-8')

            # Llamada al procedimiento almacenado
            cursor = connection.cursor()
            p_cursor = cursor.var(cx_Oracle.CURSOR)
            cursor.callproc("ObtenerDatosPresupuesto", (p_cursor,))

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

    def refrescarPresupuestos(self):
        result_set = self.obtener_datos_presupuesto()

        # Mostrar datos en la tabla
        self.mostrar_datos_en_tabla(result_set)

    def tabla_presupuestos(self):
        # Configuración de la tabla
        self.tabla = ttk.Treeview(self, columns=('ID_Presupuesto', 'ID_CentroDeCosto','ID_Rubro','Monto','Periodo'))
        self.tabla.grid(row=7, column=0,columnspan=3)
        self.tabla.heading('#1', text='ID_Presupuesto')
        self.tabla.heading('#2', text='ID_CentroDeCosto')
        self.tabla.heading('#3', text='ID_Rubro')
        self.tabla.heading('#4', text='Monto')
        self.tabla.heading('#5', text='Periodo')
        
        

        # Configuración de los botones
        self.boton_eliminar = tk.Button(self, text="Eliminar", command=self.delete_datos)
        self.boton_eliminar.config(width=20, font=('Arial', 12, 'bold'),
                                fg='White', bg='#FF0000', cursor='hand2', activebackground='#AE0000')
        self.boton_eliminar.grid(row=8, column=0, padx=10, pady=10)

        self.boton_editar = tk.Button(self, text="Editar", command=self.edit_Datos)
        self.boton_editar.config(width=20, font=('Arial', 12, 'bold'),
                                fg='White', bg='#4700BA', cursor='hand2', activebackground='#9468DA')
        self.boton_editar.grid(row=8, column=1, padx=10, pady=10)

        self.boton_refresh = tk.Button(self, text="Refrescar", command=self.refrescarPresupuestos)
        self.boton_refresh.config(width=20, font=('Arial', 12, 'bold'),
                                fg='White', bg='#4700BA', cursor='hand2', activebackground='#9468DA')
        self.boton_refresh.grid(row=8, column=2, padx=10, pady=10)


        

    def Create_Presupuesto(self):
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
            temp=self.mi_monto.get()
            temp=float(temp)
            cursor.callproc("InsertarPresupuesto", (self.mi_idpresupuesto.get(),self.mi_idcc.get(),self.mi_idRubro.get(),temp,self.mi_periodo.get()))
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
        self.refrescarPresupuestos()

    
    
    def Edit_Presupuesto(self):
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
            temp=self.mi_monto.get()
            temp=float(temp)
            cursor.callproc("EditarPresupuesto",(self.mi_idpresupuesto.get(),self.mi_idcc.get(),self.mi_idRubro.get(),temp,self.mi_periodo.get()))
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
        self.refrescarPresupuestos()
        

    def Delete_Presupuesto(self):
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
            temp=self.mi_idpresupuesto.get()
            num=int(temp)
            cursor.callproc("EliminarPresupuesto", (num,))
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
        self.refrescarPresupuestos()
   
#Interfaz Grafica para la tabla de Permiso
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
   
#Interfaz Grafica para la tabla de Liquidacion
class Frame_Liquidacion(tk.Toplevel):
    
    
    def __init__(self,root=None):
        super().__init__(root, width=200, height=200) 
        self.title("Liquidacion")
        self.root=root
        # self.pack()
        self.Liquidacion()
        self.deshabilitar_campos()
        self.tabla_liquidacion()
        self.refrescarLiquidacion()
       
        

    
    def Liquidacion(self):
        #Labels
        self.label_idLiquidacion=tk.Label(self,text="ID_Liquidacion:")
        self.label_idLiquidacion.config(font=('Arial',12,'bold'))
        self.label_idLiquidacion.grid(row =0, column=0, padx=10,pady=10)

        self.label_idPresupuesto=tk.Label(self,text="ID_Presupuesto:")
        self.label_idPresupuesto.config(font=('Arial',12,'bold'))
        self.label_idPresupuesto.grid(row =1, column=0,padx=10,pady=10)

        self.label_monto=tk.Label(self,text="Monto:")
        self.label_monto.config(font=('Arial',12,'bold'))
        self.label_monto.grid(row =2, column=0, padx=10,pady=10)

        self.label_fecha=tk.Label(self,text="Fecha:")
        self.label_fecha.config(font=('Arial',12,'bold'))
        self.label_fecha.grid(row =3, column=0, padx=10,pady=10)


        #Entrys
        self.mi_idLiquidacion=tk.StringVar()
        self.entry_idLiquidacion=tk.Entry(self,textvariable=self.mi_idLiquidacion)
        self.entry_idLiquidacion.config(width=50, font=('Arial',12))
        self.entry_idLiquidacion.grid(row=0,column=1,padx=10,pady=10, columnspan=2)


        
        self.mi_idPresupuesto=tk.StringVar()
        self.entry_idPresupuesto=tk.Entry(self,textvariable=self.mi_idPresupuesto)
        self.entry_idPresupuesto.config(width=50, font=('Arial',12))
        self.entry_idPresupuesto.grid(row=1,column=1,padx=10,pady=10, columnspan=2)

        self.mi_monto=tk.StringVar()
        self.entry_monto=tk.Entry(self,textvariable=self.mi_monto)
        self.entry_monto.config(width=50, font=('Arial',12))
        self.entry_monto.grid(row=2,column=1,padx=10,pady=10, columnspan=2)

        self.mi_fecha=tk.StringVar()
        self.entry_fecha=tk.Entry(self,textvariable=self.mi_fecha)
        self.entry_fecha.config(width=50, font=('Arial',12))
        self.entry_fecha.grid(row=3,column=1,padx=10,pady=10, columnspan=2)
        

        #Botones

        self.boton_nuevo=tk.Button(self,text="Nuevo",command=self.habilitar_campos)
        self.boton_nuevo.config(width=20, font=('Arial',12,'bold'),
        fg='White',bg='#4DCB03', cursor='hand2',activebackground='#43B302')
        self.boton_nuevo.grid(row=6,column=0,padx=10,pady=10)

        self.boton_guardar=tk.Button(self,text="Guardar",command=self.guarda_Datos)
        self.boton_guardar.config(width=20, font=('Arial',12,'bold'),
        fg='White',bg='#0157F2', cursor='hand2',activebackground='#003594')
        self.boton_guardar.grid(row=6,column=1,padx=10,pady=10)

        self.boton_cancelar=tk.Button(self,text="Cancelar",command=self.deshabilitar_campos)
        self.boton_cancelar.config(width=20, font=('Arial',12,'bold'),
        fg='White',bg='#F30000', cursor='hand2',activebackground='#8A1C1C')
        self.boton_cancelar.grid(row=6,column=2,padx=10,pady=10)

    def habilitar_campos(self):
        self.mi_idLiquidacion.set('')
        self.mi_idPresupuesto.set('')
        self.mi_monto.set('')
        self.mi_fecha.set('')
        self.entry_idLiquidacion.config(state='normal')
        self.entry_idPresupuesto.config(state='normal')
        self.entry_monto.config(state='normal')
        self.entry_fecha.config(state='normal')
        self.boton_guardar.config(state='normal')
        self.boton_cancelar.config(state='normal')

    def deshabilitar_campos(self):

        self.mi_idLiquidacion.set('')
        self.mi_idPresupuesto.set('')
        self.mi_monto.set('')
        self.mi_fecha.set('')

    
        self.entry_idLiquidacion.config(state='disabled')
        self.entry_idPresupuesto.config(state='disabled')
        self.entry_monto.config(state='disabled')
        self.entry_fecha.config(state='disabled')
        self.boton_guardar.config(state='disabled')
        self.boton_cancelar.config(state='disabled')
    
    def guarda_Datos(self):
        self.Create_Liquidacion()
        self.deshabilitar_campos()

    def edit_Datos(self):
        self.Edit_Liquidacion()
        self.deshabilitar_campos()
    def delete_datos(self):
        self.Delete_Liquidacion()
        self.deshabilitar_campos()

   


    def obtener_datos_liquidacion(self):
        try:
            # Conexión a la base de datos
            connection = cx_Oracle.connect(user='ALONSO', password='123456', dsn='localhost:1521/orcl', encoding='UTF-8')

            # Llamada al procedimiento almacenado
            cursor = connection.cursor()
            p_cursor = cursor.var(cx_Oracle.CURSOR)
            cursor.callproc("ObtenerDatosLiquidacion", (p_cursor,))

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

    def refrescarLiquidacion(self):
        result_set = self.obtener_datos_liquidacion()

        # Mostrar datos en la tabla
        self.mostrar_datos_en_tabla(result_set)

    def tabla_liquidacion(self):
        # Configuración de la tabla
        self.tabla = ttk.Treeview(self, columns=('ID_Liquidacion', 'Id_Presupuesto','Monto','Fecha'))
        self.tabla.grid(row=7, column=0, columnspan=3)
        self.tabla.heading('#1', text='ID_Liquidacion')
        self.tabla.heading('#2', text='Id_Presupuesto')
        self.tabla.heading('#3', text='Monto')
        self.tabla.heading('#4', text='Fecha')
        

        # Configuración de los botones
        self.boton_eliminar = tk.Button(self, text="Eliminar", command=self.delete_datos)
        self.boton_eliminar.config(width=20, font=('Arial', 12, 'bold'),
                                fg='White', bg='#FF0000', cursor='hand2', activebackground='#AE0000')
        self.boton_eliminar.grid(row=8, column=0, padx=10, pady=10)

        self.boton_editar = tk.Button(self, text="Editar", command=self.edit_Datos)
        self.boton_editar.config(width=20, font=('Arial', 12, 'bold'),
                                fg='White', bg='#4700BA', cursor='hand2', activebackground='#9468DA')
        self.boton_editar.grid(row=8, column=1, padx=10, pady=10)

        self.boton_refresh = tk.Button(self, text="Refrescar", command=self.refrescarLiquidacion)
        self.boton_refresh.config(width=20, font=('Arial', 12, 'bold'),
                                fg='White', bg='#4700BA', cursor='hand2', activebackground='#9468DA')
        self.boton_refresh.grid(row=8, column=2, padx=10, pady=10)


        

    def Create_Liquidacion(self):
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
            temp =self.mi_monto.get()
            temp=float(temp)
            cursor.callproc("InsertarLiquidacion", (self.mi_idLiquidacion.get(),self.mi_idPresupuesto.get(),temp,self.mi_monto.get()))
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
        self.refrescarLiquidacion()

    
    
    def Edit_Liquidacion(self):
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
            cursor.callproc("EditarLiquidacion", (self.mi_idLiquidacion.get(),self.mi_idPresupuesto.get(),self.mi_monto.get(),self.mi_fecha.get()))
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
        self.refrescarLiquidacion()
        

    def Delete_Liquidacion(self):
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
            temp=self.mi_idLiquidacion.get()
            num=int(temp)
            cursor.callproc("EliminarLiquidacion", (num,))
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
        self.refrescarLiquidacion()
   
#Interfaz Grafica para la tabla de Compra Gasto

















