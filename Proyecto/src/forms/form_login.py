import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.font import BOLD
import util.util_ventana as util_ventana
import util.util_imagenes as util_img



from forms.form_maestro_design import FormularioMaestroDesign


class App:
    
    
    def verificar(self):
        usu = self.usuario.get()
        password = self.password.get()        
        if(usu == "ALONSO" and password == "123456") :
            self.ventana.destroy()
            #Abrir la ventana principal 
            app = FormularioMaestroDesign()
            #Adaptar la geometria de la ventana para que se abra por completo
            app.geometry("{0}x{1}+0+0".format(app.winfo_screenwidth(), app.winfo_screenheight()))

            app.mainloop()
        else:
            messagebox.showerror(message="La contraseña no es correcta",title="Mensaje")           
                      
    def __init__(self):        
        self.ventana = tk.Tk()                             
        self.ventana.title('Inicio de sesion')
        self.ventana.geometry('800x500')
        self.ventana.config(bg='#fcfcfc')
        self.ventana.resizable(width=0, height=0)   
        
        # frame_logo
        frame_logo = tk.Frame(self.ventana, bd=0, width=300, relief=tk.SOLID, padx=10, pady=10,bg='#3a7ff6')
        frame_logo.pack(side="left",expand=tk.YES,fill=tk.BOTH)
        self.perfil = util_img.leer_imagen("./src/imagenes/logoPantera.png", (150, 150))
        
       
        
        
        #frame_form
        frame_form = tk.Frame(self.ventana, bd=0, relief=tk.SOLID, bg='#fcfcfc')
        frame_form.pack(side="right",expand=tk.YES,fill=tk.BOTH)
        #frame_form
        
        #frame_form_top
        frame_form_top = tk.Frame(frame_form,height = 50, bd=0, relief=tk.SOLID,bg='black')
        frame_form_top.pack(side="top",fill=tk.X)
        title = tk.Label(frame_form_top, text="Inicio de sesion",font=('Times', 30), fg="#666a88",bg='#fcfcfc',pady=50)
        title.pack(expand=tk.YES,fill=tk.BOTH)
        #end frame_form_top

        #frame_form_fill
        frame_form_fill = tk.Frame(frame_form,height = 50,  bd=0, relief=tk.SOLID,bg='#fcfcfc')
        frame_form_fill.pack(side="bottom",expand=tk.YES,fill=tk.BOTH)

        etiqueta_usuario = tk.Label(frame_form_fill, text="Usuario", font=('Times', 14) ,fg="#666a88",bg='#fcfcfc', anchor="w")
        etiqueta_usuario.pack(fill=tk.X, padx=20,pady=5)
        self.usuario = ttk.Entry(frame_form_fill, font=('Times', 14))
        self.usuario.pack(fill=tk.X, padx=20,pady=10)

        etiqueta_password = tk.Label(frame_form_fill, text="Contraseña", font=('Times', 14),fg="#666a88",bg='#fcfcfc' , anchor="w")
        etiqueta_password.pack(fill=tk.X, padx=20,pady=5)
        self.password = ttk.Entry(frame_form_fill, font=('Times', 14))
        self.password.pack(fill=tk.X, padx=20,pady=10)
        self.password.config(show="*")

        inicio = tk.Button(frame_form_fill,text="Iniciar sesion",font=('Times', 15,BOLD),bg='#3a7ff6', bd=0,fg="#fff",command=self.verificar)
        inicio.pack(fill=tk.X, padx=20,pady=20)        
        inicio.bind("<Return>", (lambda event: self.verificar()))
        #end frame_form_fill
        self.ventana.mainloop()
        
if __name__ == "__main__":
   App()