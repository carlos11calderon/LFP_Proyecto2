#imports Tkinter
from tkinter import filedialog, Tk
from tkinter.filedialog import askopenfilename
from tkinter import * 
#import graphviz
from graphviz import * 



class Gestor:
    
    def __init__(self):
        self.Tokens=[]
        self.Errores=[]

    def CargarArchivo(self): ##Inicio del metodo
        print("entro")
        #self.Tokens.clear()## al cargar un nuevo archivo se borran los tokens actuales
        #self.Errores.clear()## al cargar un nuevo archivo se borran los erroes actuales
         
        ##importamos la opciones para la ventana emergente
        Tk().withdraw()
        archivo = filedialog.askopenfile(initialdir="./Archivos Prueba", 
        title="Seleccione un archivo",filetypes=(("Archivos lfp",".lfp"),
        ("ALL files",".txt")))
        if archivo is None:
            print('No se selecciono ni un archivo\n')
            return None
        else:
            ##abrimos el archivo y lo leemos
            texto = archivo.read()
            print(texto)
            print('\n\n')
            ##concatenamos el simbolo terminal
            texto+='%'
            print(texto)
            archivo.close()##Cerramos el archivo
            print("Lectura Exitosa")