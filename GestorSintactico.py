from Token import Token
from Errores import Errores

i=0
class GestorSintactico: 

    def __init__(self):
        self.listaTokens=[]
        self.listaErrores=[]
        

    def analizar(self, listaTokens):
        global i
        i=0
        self.listaTokens = listaTokens
        self.iniciar()

    def iniciar(self):
        self.lista_Instrucciones()
        

    def lista_Instrucciones(self):
        global i
        if self.listaTokens[i].lexema == 'registros':
            self.instruccion_Registros()
        elif self.listaTokens[i].lexema == 'claves':
            self.instruccion_Claves()

    def instruccion_Claves(self):
        global i
        

    def instruccion_Registros(self):
        global i
        if self.listaTokens[i].lexema == 'registros':
            i+=1
            if self.listaTokens[i].lexema == 'igual':
                i+=1
                if self.listaTokens[i].lexema == 'corchete1':
                    i+=1
                    if self.listaTokens[i].lexema == 'llave1':
                        i+=1
                        self.lista_Registros()
                        if self.listaTokens[i].lexema== 'llave2':
                            i+=1
                    
    
    def lista_Registros(self):
        self.registro()
    
    def registro(self):
        global i
        if self.listaTokens[i].lexema == 'comillaDoble':
            i+=1
            self.SeparadorRegistros()
        if self.listaTokens[i].token == 'cadena':
            cadena = self.listaTokens[i].lexema
            print(cadena)
            i+=1
            self.SeparadorRegistros()
        elif self.listaTokens[i].token == 'entero':
            numeroEntero = self.listaTokens[i].lexema
            print(numeroEntero)
            i+=1
            self.SeparadorRegistros()
        elif self.listaTokens[i].token == 'real':
            numeroEntero = self.listaTokens[i].lexema
            print(numeroEntero)
            i+=1
            self.SeparadorRegistros()
        else: 
            #creo que aqui va error
            pass
    
    def SeparadorRegistros(self):
        global i
        if self.listaTokens[i].lexema =='llave2':
            pass
        elif self.listaTokens[i].lexema == 'coma':
            i+=1
        elif self.listaTokens[i].lexema == 'comillaDoble':
            i+=1
            self.registro()
            self.SeparadorRegistros()
        else:
            pass