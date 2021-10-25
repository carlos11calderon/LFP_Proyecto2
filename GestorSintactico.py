from Token import Token
from Errores import Errores
from prettytable import *

i=0
register=[]
ReturnText = ''
contadorImprimir =1
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
        self.listClaves=[]
        self.listRegisters=[]
        self.iniciar()
        return ReturnText

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
            self.instruccion_Imprimir()
            self.lista_Instrucciones()
        elif self.listaTokens[i].lexema=='imprimirln':
            self.instruccion_Imprimirln()
            self.lista_Instrucciones()
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
            self.instruccion_Datos()
            self.lista_Instrucciones()
        elif self.listaTokens[i].lexema=='sumar':
            self.instruccion_Sumar()
            self.lista_Instrucciones()
        elif self.listaTokens[i].lexema=='max':
            self.instruccion_max()
            self.lista_Instrucciones()
        elif self.listaTokens[i].lexema=='min':
            self.instruccion_min()
            self.lista_Instrucciones()
        elif self.listaTokens[i].lexema=='exportar':
            self.instruccion_Exportar()
            self.lista_Instrucciones()
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
        global i, ReturnText, contadorImprimir
        if self.listaTokens[i].lexema == 'imprimir':
            i+=1
            if self.listaTokens[i].lexema == 'parentesis1':
                i+=1
                if self.listaTokens[i].lexema == 'ComillaDoble':
                    i+=1
                    if self.listaTokens[i].token == 'cadena':
                        text =  self.listaTokens[i].lexema
                        i+=1
                        if self.listaTokens[i].lexema == 'ComillaDoble':
                            i+=1
                            if self.listaTokens[i].lexema== 'parentesis2':
                                i+=1
                                if self.listaTokens[i].lexema== 'puntoycoma':
                                    i+=1
                                    if contadorImprimir==0:
                                        ReturnText+=text
                                    else:
                                        ReturnText+='-->'+text
                                        contadorImprimir=0
    ## Aquí Termina La Funcion Imprimir

    ##EMPIEZA LA FUNCION IMPRIMIRLN
    def instruccion_Imprimirln(self):
        global i, ReturnText,contadorImprimir
        if self.listaTokens[i].lexema == 'imprimirln':
            i+=1
            if self.listaTokens[i].lexema == 'parentesis1':
                i+=1
                if self.listaTokens[i].lexema == 'ComillaDoble':
                    i+=1
                    if self.listaTokens[i].token == 'cadena':
                        text = self.listaTokens[i].lexema
                        i+=1
                        if self.listaTokens[i].lexema == 'ComillaDoble':
                            i+=1
                            if self.listaTokens[i].lexema== 'parentesis2':
                                i+=1
                                if self.listaTokens[i].lexema== 'puntoycoma':
                                    i+=1
                                    if contadorImprimir==0:
                                        ReturnText+=text
                                    else:
                                        ReturnText+='\n-->'+text+'\n'
                                        contadorImprimir=1
    ##TERMINA LA FUNCION IMPRIMIRLN

    def instruccion_Conteo(self):
        global i, ReturnText, contadorImprimir
        if self.listaTokens[i].lexema == 'conteo':
            i+=1
            if self.listaTokens[i].lexema == 'parentesis1':
                i+=1
                if self.listaTokens[i].lexema== 'parentesis2':
                    i+=1
                    if self.listaTokens[i].lexema== 'puntoycoma':
                        i+=1
                        print("cantidad de registros: "+str(len(self.listRegisters)))
                        ReturnText+='\n-->'+str(len(self.listRegisters))
                        contadorImprimir=1
    ## empieza instrucciones promedio
    def instruccion_Promedio(self):
        global i, ReturnText, contadorImprimir
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
                                        
                                    promedio = self.sacarPromedio(posicion)
                                    print('el promedio es: '+str(promedio))
                                    ReturnText+='\n-->'+str(promedio)
                                    contadorImprimir=1
    
    def sacarPromedio(self,posicion):
        summation=0
        totalRegisters=len(self.listRegisters)
        for i in self.listRegisters:
            summation+=float(i[posicion])
        promedio = summation/totalRegisters
        return promedio
    ## termina instrucciones promedio

    def instruccion_Sumar(self):
        global i, ReturnText, contadorImprimir
        if self.listaTokens[i].lexema == 'sumar':
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
                                            position = p
                                        
                                    summation = self.Sumar(position)
                                    print('La sumatoria en '+self.listClaves[position]+' es: '+str(summation))
                                    ReturnText+='\n-->'+str(summation)
                                    contadorImprimir=1
    def Sumar(self, position):
        summation=0
        for i in self.listRegisters:
            summation+=float(i[position])
        return summation

    def instruccion_Contarsi(self):
        global i, ReturnText, contadorImprimir
        if self.listaTokens[i].lexema == 'contarsi':
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
                            if self.listaTokens[i].lexema== 'coma':
                                i+=1
                                if self.listaTokens[i].token== 'entero':
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
                                                    ReturnText+='\n-->'+str(ValueCount)
                                                    contadorImprimir=1
    def ejec_ContarSi(self, position, value):
        summation=0
        for i in self.listRegisters:
            if i[position] == value:
                summation+=1
        return summation
    
    def instruccion_Datos(self):
        global i, ReturnText, contadorImprimir
        if self.listaTokens[i].lexema == 'datos':
            i+=1
            if self.listaTokens[i].lexema == 'parentesis1':
                i+=1 
                if self.listaTokens[i].lexema== 'parentesis2':
                    i+=1
                    if self.listaTokens[i].lexema== 'puntoycoma':
                        i+=1
                        datos=self.impDatos()
                        print(datos)
                        ReturnText+='\n-->\n'+str(datos)+'\n'
                        contadorImprimir=1
    def impDatos(self):
        a = PrettyTable()
        a.field_names = self.listClaves
        for i in self.listRegisters:
            a.add_row(i)
        return a   
    
    def instruccion_max(self):
        global i, ReturnText, contadorImprimir
        if self.listaTokens[i].lexema == 'max':
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
                                            position = p
                                            ValueMax =self.ValueMax(position)
                                            print('valor maximo en '+field+" es: "+ str(ValueMax))
                                            ReturnText+='\n-->'+str(ValueMax)
                                            contadorImprimir=1
    def ValueMax(self, position):
        Vmax = 0
        for i in self.listRegisters:
            Vtemp = i[position]
            if float(Vtemp)>Vmax:
                Vmax = float(Vtemp)
        return Vmax

    def instruccion_min(self):
        global i, ReturnText, contadorImprimir
        if self.listaTokens[i].lexema == 'min':
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
                                            position = p
                                            ValueMin =self.ValueMin(position)
                                            print('valor minimo en '+field+" es: "+ str(ValueMin))
                                            ReturnText+='\n-->'+str(ValueMin)
                                            contadorImprimir=1
    def ValueMin(self, position):
        Vmin = self.ValueMax(position)
        
        for i in self.listRegisters:
            if float(i[position])<Vmin:
                Vmin = float(i[position])
        return Vmin
    
    def instruccion_Exportar(self):
        global i, ReturnText, contadorImprimir
        if self.listaTokens[i].lexema == 'exportar':
            i+=1
            if self.listaTokens[i].lexema == 'parentesis1':
                i+=1
                if self.listaTokens[i].lexema == 'ComillaDoble':
                    i+=1
                    if self.listaTokens[i].token == 'cadena':
                        titulo = self.listaTokens[i].lexema
                        i+=1
                        if self.listaTokens[i].lexema == 'ComillaDoble':
                            i+=1
                            if self.listaTokens[i].lexema== 'parentesis2':
                                i+=1
                                if self.listaTokens[i].lexema== 'puntoycoma':
                                    i+=1
                                    self.generarReporteHtml(titulo)
                                    ReturnText+='\n-->Revisar Reporte'
                                    contadorImprimir=1
    def generarReporteHtml(self, titulo):
        Filee = open("./Reportes/"+titulo+".html",'w')
        contenidoHead=''
        contenidoTabla = ''
        for i in self.listClaves:
            contenidoHead +='<th scope="col">'+i+'</th>\n'
        for i in self.listRegisters:
            contenidoTabla+='<tr>\n'
            for j in i:
                contenidoTabla+='<td>'+j+'</td>\n'
            contenidoTabla+='<tr>\n'
        contenidoHTML=(
              '<!DOCTYPE html>\n'
                ' <html>\n' 
                '<head> \n'
                '<meta charset="utf-8"> \n'
                '<link href="assets/css/bootstrap-responsive.css" type="text/css" rel="stylesheet">\n'
                '<link href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css" type="text/css" rel="stylesheet">\n'
                '<link rel="stylesheet" type="text/css" href="./css/bootstrap.css">\n'
                '<link rel="stylesheet" type="text/css"  href="css/Style.css">'
                '<title>'+titulo+ '</title>\n'
                '</head>\n' 
                '<body>\n'
                '<div class="container-fluid welcome-page" id="home">\n'
                '   <div class="jumbotron">\n'
                '       <h1>\n <span> '+titulo+
                '\n</span>\n </h1>\n<p>Tabla de datos</p>\n'
                '</div>'
                '</div>'
                '<div class="container-fluid " ><div class="jumbotron">'
                '<table class="table table-responsive">\n'
                '   <thead>\n'
                        '<tr>\n'
                        +contenidoHead+
                        '</tr>\n'
                    '</thead>\n'
                    '<tbody>\n'
                    +contenidoTabla+
                    '</tbody>\n'
                    '</table>'   
                    '</div>'
                '</div>\n'
            '</body>\n'
            '</html>\n')    
        Filee.write(contenidoHTML)
        Filee.close()
        print('reporte Exportado')

