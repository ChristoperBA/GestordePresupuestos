from PIL import ImageTk, Image

#Redimencionar la imagen, ajustar la imagen
def leer_imagen( path, size): 
        return ImageTk.PhotoImage(Image.open(path).resize(size,  Image.ADAPTIVE))  

