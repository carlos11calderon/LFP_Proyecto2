from Token import Token
from Errores import Errores

i=0
register=[]
ReturnText = ''
class GestorSintactico: 
    
    def __init__(self):
        self.listaTokens=[]
        self.listaErrores=[]
        self.listClaves =[]
        self.listRegisters = []
        
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
            self.lista_Instrucciones()
        elif self.listaTokens[i].lexema == 'claves':
            self.instruccion_Claves()
            self.lista_Instrucciones()
        elif self.listaTokens[i].lexema == 'CommentSimple':
            i+=1
            self.lista_Instrucciones()
            
        elif self.listaTokens[i].lexema=='ComillaSimple':
            i+=1
            self.lista_Instrucciones()
        elif self.listaTokens[i].lexema=='imprimir':
            pass
        elif self.listaTokens[i].lexema=='imprimirln':
            pass
        elif self.listaTokens[i].lexema=='conteo':
            self.instruccion_Conteo()
            self.lista_Instrucciones()
        elif self.listaTokens[i].lexema=='promedio':
            self.instruccion_Promedio()
            self.lista_Instrucciones()
        elif self.listaTokens[i].lexema=='contarsi':
            self.instruccion_Contarsi()
            self.lista_Instrucciones()
        elif self.listaTokens[i].lexema=='datos':
            pass
        elif self.listaTokens[i].lexema=='sumar':
            pass
        elif self.listaTokens[i].lexema=='max':
            self.instruccion_max()
            self.lista_Instrucciones()
        elif self.listaTokens[i].lexema=='min':
            self.instruccion_min()
            self.lista_Instrucciones()
        elif self.listaTokens[i].lexema=='exportar':
            pass
        elif self.listaTokens[i].lexema=='fin':
            print('fin analisis sintactico')
        else:
            pass

    
    
    ##EMPIEZA LAS FUNCIONES PARA LA INSTRUCCION DE CLAVES
    def instruccion_Claves(self):
        global i
        if self.listaTokens[i].lexema == 'claves':
            i+=1
            if self.listaTokens[i].lexema == 'igual':
                i+=1
                if self.listaTokens[i].lexema == 'corchete1':
                    i+=1
                    self.lista_Claves()
                    if self.listaTokens[i].lexema== 'corchete2':
                        i+=1
                        print('finalizaron claves')

    def lista_Claves(self):
        self.clave()

    def clave(self):
        global i
        if self.listaTokens[i].lexema == 'ComillaDoble':
            i+=1
            self.SeparadorClaves() 
        elif self.listaTokens[i].token == 'cadena':
            cadena = self.listaTokens[i].lexema
            self.listClaves.append(cadena)
            print(cadena)
            i+=1
            self.SeparadorClaves()
        else: 
            #creo que aqui va error
            pass

    def SeparadorClaves(self):
        global i
        if self.listaTokens[i].lexema == 'coma':
            i+=1
            self.clave()
        else:
            self.clave()
    ##TERMINA LAS FUNCIONES PARA LA INSTRUCCION DE CLAVES   
    
    ##EMPIEZA LAS FUNCIONES PARA LA INSTRUCCION DE REGISTROS
    def instruccion_Registros(self):
        global i
        if self.listaTokens[i].lexema == 'registros':
            i+=1
            if self.listaTokens[i].lexema == 'igual':
                i+=1
                if self.listaTokens[i].lexema == 'corchete1':
                    i+=1
                    self.lista_Registros()
                    if self.listaTokens[i].lexema== 'corchete2':
                        i+=1
                        print('finalizaron registros')
    
    def lista_Registros(self):
        self.registro()

    def registro(self):
        global i
        global register
        if self.listaTokens[i].lexema == 'ComillaDoble':
            i+=1
            self.SeparadorRegistros()
        elif self.listaTokens[i].token == 'cadena':
            cadena = self.listaTokens[i].lexema
            register.append(cadena)
            print(cadena)
            i+=1
            self.SeparadorRegistros()
        elif self.listaTokens[i].token == 'entero':
            numeroEntero = self.listaTokens[i].lexema
            register.append(numeroEntero)
            print(numeroEntero)
            i+=1
            self.SeparadorRegistros()
            self.registro()
        elif self.listaTokens[i].token == 'real':
            numeroEntero = self.listaTokens[i].lexema
            register.append(numeroEntero)
            print(numeroEntero)
            i+=1
            self.SeparadorRegistros()
        elif self.listaTokens[i].lexema == 'llave1':
            i+=1
            self.registro()
        elif self.listaTokens[i].lexema == 'llave2':
            i+=1
            self.listRegisters.append(register)
            register=[]
            self.registro()
        else: 
            #creo que aqui va error
            pass
    
    def SeparadorRegistros(self):
        global i
        if self.listaTokens[i].lexema =='llave2':
            pass
        elif self.listaTokens[i].lexema == 'coma':
            i+=1
            self.registro()
        else:
            self.registro()
    #Terminan las funciones de Registros

    ## EMPIEZA LA FUNCION IMPRIMIR
    def instruccion_Imprimir(self):
        global i
        if self.listaTokens[i].lexema == 'imprimir':
            i+=1
            if self.listaTokens[i].lexema == 'parentesis1':
                i+=1
                if self.listaTokens[i].lexema == 'cadena':
                    text =  self.listaTokens[i].lexema
                    i+=1
                    if self.listaTokens[i].lexema== 'parentesis2':
                        i+=1
                        if self.listaTokens[i].lexema== 'puntoycoma':
                            i+=1
                            print(text)
    ## Aquí Termina La Funcion Imprimir

    ##EMPIEZA LA FUNCION IMPRIMIRLN
    def instruccion_Imprimirln(self):
        global i
        if self.listaTokens[i].lexema == 'imprimirln':
            i+=1
            if self.listaTokens[i].lexema == 'parentesis1':
                i+=1
                if self.listaTokens[i].lexema == 'ComillaDoble':
                    i+=1
                    if self.listaTokens[i].lexema == 'cadena':
                        text = self.listaTokens[i].lexema
                        i+=1
                        if self.listaTokens[i].lexema == 'ComillaDoble':
                            i+=1
                            if self.listaTokens[i].lexema== 'parentesis2':
                                i+=1
                                if self.listaTokens[i].lexema== 'puntoycoma':
                                    i+=1
                                    print(text+'\n')
    ##TERMINA LA FUNCION IMPRIMIRLN

    def instruccion_Conteo(self):
        global i
        if self.listaTokens[i].lexema == 'conteo':
            i+=1
            if self.listaTokens[i].lexema == 'parentesis1':
                i+=1
                if self.listaTokens[i].lexema== 'parentesis2':
                    i+=1
                    if self.listaTokens[i].lexema== 'puntoycoma':
                        i+=1
                        print("cantidad de registros: "+str(len(self.listRegisters)))
    ## empieza instrucciones promedio
    def instruccion_Promedio(self):
        global i
        if self.listaTokens[i].lexema == 'promedio':
            i+=1
            if self.listaTokens[i].lexema == 'parentesis1':
                i+=1
                if self.listaTokens[i].lexema == 'ComillaDoble':
                    i+=1
                    if self.listaTokens[i].token == 'cadena':
                        field = self.listaTokens[i].lexema
                        i+=1
                        if self.listaTokens[i].lexema == 'ComillaDoble':
                            i+=1
                            if self.listaTokens[i].lexema== 'parentesis2':
                                i+=1
                                if self.listaTokens[i].lexema== 'puntoycoma':
                                    i+=1
                                    for p in range(len(self.listClaves)):
                                        if self.listClaves[p] == field:
                                            posicion = p
                                        else:
                                            print("la clave no existe")
                                    promedio = self.sacarPromedio(posicion)
                                    print('el promedio es: '+str(promedio))
    
    def sacarPromedio(self,posicion):
        summation=0
        totalRegisters=len(self.listRegisters)
        for i in self.listRegisters:
            summation+=int(i[posicion])
        promedio = summation/totalRegisters
        return promedio
    ## termina instrucciones promedio

    def instruccion_Contarsi(self):
        global i
        if self.listaTokens[i].lexema == 'contarsi':
            i+=1
            if self.listaTokens[i].lexema == 'parentesis1':
                i+=1
                if self.listaTokens[i].lexema == 'ComillaDoble':
                    i+=1
                    if self.listaTokens[i].lexema == 'cadena':
                        field = self.listaTokens[i].lexema
                        i+=1
                        if self.listaTokens[i].lexema == 'ComillaDoble':
                            i+=1
                            if self.listaTokens[i].lexema== 'coma':
                                i+=1
                                if self.listaTokens[i].lexema== 'entero':
                                    value = self.listaTokens[i].lexema
                                    i+=1
                                    if self.listaTokens[i].lexema== 'parentesis2':
                                        i+=1
                                        if self.listaTokens[i].lexema== 'puntoycoma':
                                            i+=1
                                            for p in range(len(self.listClaves)):
                                                if self.listClaves[p] == field:
                                                    position = p
                                                    ValueCount = self.ejec_ContarSi(position, value)
                                                    print('cantidad de valores con el valor '+str(value)+'son: '+str(ValueCount)) 
                                                else:
                                                    print("la clave no existe")
                                               
    def ejec_ContarSi(self, position, value):
        summation=0
        for i in self.listRegisters:
            if i[position] == value:
                summation+=1
        return summation
    
    def instruccion_Datos(self):
        pass

    def instruccion_max(self):
        global i
        if self.listaTokens[i].lexema == 'max':
            i+=1
            if self.listaTokens[i].lexema == 'parentesis1':
                i+=1
                if self.listaTokens[i].lexema == 'ComillaDoble':
                    i+=1
                    if self.listaTokens[i].lexema == 'cadena':
                        field = self.listaTokens[i].lexema
                        i+=1
                        if self.listaTokens[i].lexema == 'ComillaDoble':
                            i+=1
                            if self.listaTokens[i].lexema== 'parentesis2':
                                i+=1
                                if self.listaTokens[i].lexema== 'puntoycoma':
                                    i+=1
                                    for p in range(len(self.listClaves)):
                                        if self.listClaves[p] == field:
                                            position = p
                                            ValueMax =self.ValueMax(position)
                                            print('valor minimo en '+field+" es: "+ str(ValueMax))
                                        else:
                                            print("la clave no existe")
    def ValueMax(self, position):
        Vmax = 0
        for i in self.listRegisters:
            if i[position]>Vmax:
                Vmax = i[position]
        return Vmax

    def instruccion_min(self):
        global i
        if self.listaTokens[i].lexema == 'min':
            i+=1
            if self.listaTokens[i].lexema == 'parentesis1':
                i+=1
                if self.listaTokens[i].lexema == 'ComillaDoble':
                    i+=1
                    if self.listaTokens[i].lexema == 'cadena':
                        field = self.listaTokens[i].lexema
                        i+=1
                        if self.listaTokens[i].lexema == 'ComillaDoble':
                            i+=1
                            if self.listaTokens[i].lexema== 'parentesis2':
                                i+=1
                                if self.listaTokens[i].lexema== 'puntoycoma':
                                    i+=1
                                    for p in range(len(self.listClaves)):
                                        if self.listClaves[p] == field:
                                            position = p
                                            ValueMin =self.ValueMax(position)
                                            print('valor minimo en '+field+" es: "+ str(ValueMin))
                                        else:
                                            print("la clave no existe")
    
    def ValueMin(self, position):
        Vmax = 0
        
        for i in self.listRegisters:
            if i[position]>Vmax:
                Vmax = i[position]
        Vmin = Vmax
        for i in self.listRegisters:
            if i[position]<Vmin:
                Vmin = i[position]
        return Vmin
    def instruccion_Exportar(self):
        pass 
    