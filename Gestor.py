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
            Text+='%'
            filee.close()##Cerramos el archivo
            print("Lectura Exitosa")
            return Text 

    def isLetter(self,Character):##metodo que retorna si es una letra alfabetica
        if((ord(Character) >= 65 and ord(Character) <= 90) 
        or (ord(Character) >= 97 and ord(Character) <= 122) 
        or ord(Character) == 164 or ord(Character) == 165):
            return True
        else:
            return False
    
    def isNum(self,Character):##metodo que retorna si es un digito
        if ((ord(Character) >= 48 and ord(Character) <= 57)):
            return True
        else:
            return False

    def isCharacter(self, Character):
        if ((ord(Character)>=32 and ord(Character)!=34 and ord(Character)<=125 )):
            return True
        elif ord(Character)==34:
            return False

    def Analysis(self, Text):
        CuerpoClaves=[]
        CuerpoRegistros=[]
        estado = 0
        lexema=""
        contadorColumna=0
        contadorFila=1
        for x in Text:
            if(ord(x)==10):## decision si hay un salto de linea se reinicia contadores
                contadorFila+=1
                contadorColumna=0
            contadorColumna+=1
            if (estado==0):## inicia el automata
                if self.isLetter(x) == True:
                    lexema += x
                    estado = 1
                elif x == "#":
                    lexema=""
                    estado = 21
                elif x == "'":
                    lexema+="'"
                    estado = 24   
            elif (estado==1):
                if self.isLetter(x)==True:
                    lexema+=x
                    
                elif ord(x)==61: #if character is '='
                    if lexema=="Claves":
                        self.Tokens.append(Token("Reservada", '=', contadorFila, contadorColumna))
                        estado = 2
                    elif lexema=='Registros':
                        self.Tokens.append(Token("Reservada", '=', contadorFila, contadorColumna))
                        estado = 3
                elif ord(x) == 32 or ord(x) == 10 or ord(x) == 9: 
                    pass
            elif (estado==2):
                if (ord(x)==91):
                    self.Tokens.append(Token("Reservada", '[', contadorFila, contadorColumna))
                    estado=3
                elif ord(x) == 32 or ord(x) == 10 or ord(x) == 9: 
                    pass
            elif (estado==3):
                
                if(x=='"'):
                    if lexema=="Claves":
                        self.Tokens.append(Token("Reservada",lexema,contadorFila,contadorColumna))
                        lexema=""
                        lexema+=x
                        self.Tokens.append(Token("Simbolo", x, contadorFila, contadorColumna))
                        lexema=''
                        estado=4
                    else:
                        e = 'Error sintactico en la palabra reservada clave'
                elif(x=='{'):
                    if lexema=="Registros":
                        self.Tokens.append(Token("Reservada",lexema,contadorFila,contadorColumna))
                        lexema=""
                        lexema+=x
                        self.Tokens.append(Token("Simbolo", x, contadorFila, contadorColumna))
                        lexema=''
                        estado = 5
                    else:
                        e = 'Error sintactico en la palabra reservada clave'
                elif ord(x) == 32 or ord(x) == 10 or ord(x) == 9: 
                    pass
            elif (estado==4):
                    if self.isCharacter(x)==True:
                        lexema+=x
                        estado=6
            elif (estado==5):
                
                if self.isNum(x)==True:
                    lexema+=x
                    estado=10
                elif x == '"':
                    self.Tokens.append(Token("Simbolo", x, contadorFila, contadorColumna))
                    estado =11
                elif ord(x) == 32 or ord(x) == 10 or ord(x) == 9: 
                    pass    
            elif (estado==6):
                if self.isCharacter(x)==True:
                    lexema+=x
                elif x == '"':
                    self.Tokens.append(Token("Simbolo", x, contadorFila, contadorColumna))
                    estado=7
                    self.Tokens.append(Token("Clave", lexema, contadorFila, contadorColumna))
                    CuerpoClaves.append(lexema)
                    lexema=''
            elif(estado==7):
                if x==",":
                    self.Tokens.append(Token("Simbolo", x, contadorFila, contadorColumna))
                    estado = 8
                elif x=="]":
                    self.Tokens.append(Token("Simbolo", x, contadorFila, contadorColumna))
                    self.ListClaves.append(CuerpoClaves)
                    estado=9
            elif(estado==8):
                if x=='"':
                    self.Tokens.append(Token("Simbolo", x, contadorFila, contadorColumna))
                    estado=4
                elif ord(x) == 32 or ord(x) == 10 or ord(x) == 9: 
                    pass
            elif(estado==9):
                lexema=''
                if self.isLetter(x):
                    lexema+=x
                    estado=1
                elif ord(x) == 32 or ord(x) == 10 or ord(x) == 9: 
                    pass
            elif(estado==10):
                if self.isNum(x)==True or x=='.':
                    lexema+=x
                elif x==',':
                    self.Tokens.append(Token("Simbolo", x, contadorFila, contadorColumna))
                    self.Tokens.append(Token("Registro", lexema, contadorFila, contadorColumna))
                    
                    CuerpoRegistros.append(lexema)
                    lexema=''
                    estado=5
                elif x=='}':
                    CuerpoRegistros.append(lexema)
                    self.ListRegistros.append(CuerpoRegistros)
                    CuerpoRegistros=[]
                    lexema=''
                    self.Tokens.append(Token("Simbolo", x, contadorFila, contadorColumna))
                    estado=12
                elif ord(x) == 32 or ord(x) == 10 or ord(x) == 9: 
                    pass
            elif(estado==11):
                if self.isCharacter(x)==True:
                    lexema+=x
                    estado=29
                elif x==",":
                    CuerpoRegistros.append(lexema)

                    lexema=''
                    estado=5
            elif(estado==12):
                if x == ']':
                    self.Tokens.append(Token("Simbolo", x, contadorFila, contadorColumna))
                    estado = 13
                    lexema=''
                elif x =='{':
                    self.Tokens.append(Token("Simbolo", x, contadorFila, contadorColumna))
                    estado = 5
            elif (estado==13):
                if self.isLetter(x)==True:
                    lexema+=x
                    estado=14
                elif x=="'":
                    estado=24
                elif x=="#":
                    estado=23
                
            elif estado==23:
                if x !='\n':
                    pass
                else:
                    estado=13
            elif estado==24:
                if lexema != "'''":
                    if x=="'":
                        lexema+=x
                    else:
                        lexema=''
                        pass
                else:
                    lexema=''

            elif estado==29:
                if self.isCharacter(x)==True:
                    lexema+=x
                elif x=='"':
                    self.Tokens.append(Token("Simbolo", x, contadorFila, contadorColumna))
                    self.Tokens.append(Token("Registro", lexema, contadorFila, contadorColumna))
                    CuerpoRegistros.append(lexema)
                    lexema=''
                    estado=30
            elif estado == 30:
                if x == ',':
                    self.Tokens.append(Token("Simbolo", x, contadorFila, contadorColumna))
                    estado = 5
                elif x == '}':
                    
                    self.Tokens.append(Token("Simbolo", x, contadorFila, contadorColumna))
                    
                    estado = 12
                elif ord(x) == 32 or ord(x) == 10 or ord(x) == 9: 
                    pass
            

        