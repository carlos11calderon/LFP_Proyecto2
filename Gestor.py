#imports Tkinter
from tkinter import filedialog, Tk
from tkinter.filedialog import askopenfilename
from tkinter import * 
#import graphviz
from graphviz import * 
#imports clases
import Errores
from Token import Token

Text=''
class Gestor:
    
    def __init__(self):
        self.Tokens=[]
        self.TokensComandos=[]
        self.Errores=[]
        
        self.ListRegistros=[]
        self.ListClaves = []
        self.hayClaves = False
        self.hayRegistros = False
        

    def CargarArchivo(self): ##Inicio del metodo
        #self.Tokens.clear()## al cargar un nuevo archivo se borran los tokens actuales
        #self.Errores.clear()## al cargar un nuevo archivo se borran los erroes actuales
        global Text
        ##importamos la opciones para la ventana emergente
        Tk().withdraw()
        filee = filedialog.askopenfile(initialdir="./Archivos Prueba", 
        title="Select a file",filetypes=(("Files lfp",".lfp"),
        ("ALL files",".txt")))
        if filee is None:
            print('No file was selected\n')
            return None
        else:
            ##abrimos el archivo y lo leemos
            Text = filee.read()
            
            ##concatenamos el simbolo terminal
            Text+='\n$'
            filee.close()##Cerramos el archivo
            print("Lectura Exitosa")
            return Text 

    
            

        