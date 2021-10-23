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
            pass
        elif self.listaTokens[i].lexema == 'claves':
            pass

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
                    
    
    def lista_Registros(self):
        self.registro()
    
    def registro(self):
        global i
        if self.listaTokens[i].lexema == 'llave1':
            i+=1
            self.lista_valor_registrar() 