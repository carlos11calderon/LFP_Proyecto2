from tkinter.constants import E
import token
from Errores import Errores
from Token import Token
class AutomataLexico:
    
    def __init__(self):
        self.listaTokens=[]
        self.listaErrores=[]

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
        if ((ord(Character)>=32 and ord(Character)!=34)):
            return True
        elif (160<=ord(Character)<=165 or ord(Character)==129 or ord(Character)==130):
            return True
        elif ord(Character)==34:
            return False
    
    def analizar(self, texto):  #inserta solamente al final
        #inicializar listas nuevamente
        self.listaTokens = []
        self.listaErrores = []

        estado = 0
        fila =1
        columna=1
        lexema = ''    
        i = 0
        while i <len(texto):
            x=texto[i]
            if estado==0:
                if x == '=':
                    self.listaTokens.append(Token("=",'igual',fila,columna))
                    columna+=1
                elif x=='[':
                    self.listaTokens.append(Token("[",'corchete1',fila,columna))
                    columna+=1
                elif x==']':
                    self.listaTokens.append(Token("]",'corchete2',fila,columna))
                    columna+=1
                elif x=='{':
                    self.listaTokens.append(Token("{",'llave1',fila,columna))
                    columna+=1
                elif x=='}':
                    self.listaTokens.append(Token("}",'llave2',fila,columna))
                    columna+=1
                elif x=='(':
                    self.listaTokens.append(Token("(",'parentesis1',fila,columna))
                    columna+=1
                elif x==')':
                    self.listaTokens.append(Token(")",'parentesis2',fila,columna))
                    columna+=1
                elif x==';':
                    self.listaTokens.append(Token(";",'puntoycoma',fila,columna))
                    columna+=1
                elif x==',':
                    self.listaTokens.append(Token(",",'coma',fila,columna))
                    columna+=1
                elif x=='"':
                    self.listaTokens.append(Token('"', 'ComillaDoble',fila,columna))
                    columna+=1
                    estado=7
                elif x=="#":
                    self.listaTokens.append(Token('#', 'CommentSimple',fila,columna))
                    columna+=1
                    estado=1
                elif x=='.':
                    self.listaTokens.append(Token('.', 'punto',fila,columna))
                    columna+=1
                elif x=="'":
                    self.listaTokens.append(Token("'", 'ComillaSimple',fila,columna))
                    columna+=1
                    estado=2
                elif x=='\n':
                    fila+=1
                    columna=1
                elif self.isNum(x)==True:
                    lexema+=x
                    columna+=1
                    estado=9
                elif self.isLetter(x)==True:
                    lexema+=x
                    columna+=1
                    estado=11
                elif x=='$':
                    self.listaTokens.append(Token('$','Fin',fila,columna))
                    print('fin de lectura')
                else:
                    e='Error lexico en fila '+str(fila)+' y columna '+str(columna)+" revisar"
                    self.listaErrores.append(Errores(fila, columna, e, "Simbolo, letra o digito"))
            elif estado==1:
                if x=='\n':
                    fila+=1
                    columna=1
                    estado=0
                else:
                    pass
            elif estado==2:
                if x == "'":
                    
                    columna+=1
                    estado=3
                elif ord(x) == 32 or ord(x) == 10 or ord(x) == 9: 
                    pass
                elif x=='\n':
                    fila+=1
                    columna=1
                
            elif estado==3:
                if x == "'":
                    self.listaTokens.append(Token("'''", 'ComillaSimple',fila,columna))
                    columna+=1
                    estado=4
                elif ord(x) == 32 or ord(x) == 10 or ord(x) == 9: 
                    pass
                elif x=='\n':
                    fila+=1
                    columna=1
                else:
                    e='Error lexico en fila '+str(fila)+' y columna '+str(columna)+" revisar"
                    self.listaErrores.append(Errores(fila, columna, e, "ComillaSimple"))
            elif estado==4:
                if x == "'":
                    columna+=1
                    estado=5
                elif x=='\n':
                    fila+=1
                    columna=1
                else:
                    pass
            elif estado==5:
                if x == "'":
                    columna+=1
                    estado=6
                elif ord(x) == 32 or ord(x) == 10 or ord(x) == 9:
                    pass
                elif x=='\n':
                    fila+=1
                    columna=1
            elif estado==6:
                if x == "'":
                    self.listaTokens.append(Token("'''", 'ComillaSimple',fila,columna))
                    columna+=1
                    estado=0
                elif ord(x) == 32 or ord(x) == 10 or ord(x) == 9:
                    pass
                elif x=='\n':
                    fila+=1
                    columna=1
            elif estado==7:
                if self.isCharacter(x)==True:
                    lexema+=x
                    columna+=1
                    estado=8
                elif x=='"':
                    lexema=''
                    columna+=1
                    i-=1
                    estado=8
                else:
                    e='Error lexico en fila '+str(fila)+' y columna '+str(columna)+" revisar"
                    self.listaErrores.append(Errores(fila, columna, e, "caracter o cadena vacía"))
            elif estado==8:
                if self.isCharacter(x)==True:
                    lexema+=x
                    columna+=1
                elif x=='"':
                    self.listaTokens.append(Token('cadena',lexema,fila,columna))
                    lexema=''
                    self.listaTokens.append(Token('"', 'ComillaDoble',fila,columna))
                    columna+=1
                    estado=0
                else:
                    e='Error lexico en fila '+str(fila)+' y columna '+str(columna)+" revisar"
                    self.listaErrores.append(Errores(fila, columna, e, 'caracter o " '))
            elif estado==9:
                if self.isNum(x)==True:
                    lexema+=x
                    columna+=1
                elif x == '.':
                    lexema+=x
                    estado=10
                    columna+=1
                else: 
                    self.listaTokens.append(Token('entero',lexema ,fila,columna))
                    lexema=''
                    i-=1
                    estado=0
            elif estado==10:
                if self.isNum(x)==True:
                    lexema+=x
                    columna+=1
                else:
                    self.listaTokens.append(Token('real',lexema,fila, columna))
                    lexema=''
                    estado=0
                    i-=1
                
            elif estado==11:
                if self.isLetter(x)==True:
                    lexema+=x
                else:
                    if lexema=='Claves':
                        self.listaTokens.append(Token(lexema,'claves',fila,columna))
                    elif lexema=='Registros':
                        self.listaTokens.append(Token(lexema,'registros',fila,columna))
                    elif lexema=='imprimir':
                        self.listaTokens.append(Token(lexema,'imprimir',fila,columna))
                    elif lexema=='imprimirln':
                        self.listaTokens.append(Token(lexema,'imprimirln',fila,columna))
                    elif lexema=='conteo':
                        self.listaTokens.append(Token(lexema,'conteo',fila,columna))
                    elif lexema=='promedio':
                        self.listaTokens.append(Token(lexema,'promedio',fila,columna))
                    elif lexema=='contarsi':
                        self.listaTokens.append(Token(lexema,'contarsi',fila,columna))
                    elif lexema=='datos':
                        self.listaTokens.append(Token(lexema,'datos',fila,columna))
                    elif lexema=='sumar':
                        self.listaTokens.append(Token(lexema,'sumar',fila,columna))
                    elif lexema=='max':
                        self.listaTokens.append(Token(lexema,'max',fila,columna))
                    elif lexema=='min':
                        self.listaTokens.append(Token(lexema,'min',fila,columna))
                    elif lexema=='exportarReporte':
                        self.listaTokens.append(Token(lexema,'exportar',fila,columna))
                    else:
                        e='Error lexico en fila '+str(fila)+' y columna '+str(columna)+" revisar comando"
                        self.listaErrores.append(Errores(fila, columna, e, "Comando"))
                    lexema=''
                    i-=1
                    estado=0
            i+=1
        ##print('ultimo token--->'+self.listaTokens[473].lexema)
        #print(self.listaTokens[526].lexema)
        return self.listaTokens

    def listE(self):
        return self.listaErrores

    def ListaErroresReporte(self):
        return self.listaErrores           