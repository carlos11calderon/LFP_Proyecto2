from Token import Token
from Errores import Errores
from prettytable import *
from graphviz import *
import os, webbrowser
i=0
register=[]
ReturnText = ''
contadorImprimir =1
NodeData=''
NodosCrear=''
CountInstrucciones=0
CountInstruccion=0
CountClave=0
CountSimboloIgual=0
CountSimboloCorchete=0
CountListClaves=0
CountListRegistro=0
CountCadena=0
CountComa=0
CountRegistro=0
CountReal=0
CountLlave=0
CountValue=0
CountEntero=0
CountProceso=0
CountSimboloPa=0
countToken=0
class GestorSintactico: 
    
    def __init__(self):
        self.listaTokens=[]
        self.listaErrores=[]
        self.listClaves =[]
        self.listRegisters = []
        
    def analizar(self, listaTokens, listaErrores):
        global i, ReturnText,NodeData, NodosCrear
        ReturnText=NodeData=NodosCrear=''
        i=0
        self.InicializarContadores()
        self.listaTokens = listaTokens
        self.listaErrores = listaErrores
        self.listClaves=[]
        self.listRegisters=[]
        self.iniciar()
        return ReturnText

    def InicializarContadores(self):
        global contadorImprimir, NodeData, NodosCrear, CountInstrucciones, CountInstruccion, CountClave
        global CountSimboloIgual, CountSimboloCorchete, CountListClaves,  CountListRegistro, CountCadena, CountComa
        global CountRegistro, CountReal, CountLlave, CountValue, CountEntero, CountProceso, CountSimboloPa, countToken
        CountInstrucciones=0
        CountInstruccion=0
        CountClave=0
        CountSimboloIgual=0
        CountSimboloCorchete=0
        CountListClaves=0
        CountListRegistro=0
        CountCadena=0
        CountComa=0
        CountRegistro=0
        CountReal=0
        CountLlave=0
        CountValue=0
        CountEntero=0
        CountProceso=0
        CountSimboloPa=0
        countToken=0

    def iniciar(self):
        global NodeData,CountInstrucciones,NodosCrear
        NodosCrear+='Instrucciones'+str(CountInstrucciones)+'[label="Instrucciones"]\n'
        NodeData+='inicio->Instrucciones'+str(CountInstrucciones)+'\n'
        self.lista_Instrucciones()
      
    def lista_Instrucciones(self):
        global i, NodeData, CountInstrucciones, NodosCrear, CountInstruccion, CountRegistro,CountListRegistro
        global CountProceso
        
        
        
        if self.listaTokens[i].lexema == 'registros':
            CountInstrucciones+=1
            CountInstruccion+=1
            NodosCrear+='Instrucciones'+str(CountInstrucciones)+'[label="Instrucciones"]\n'
            NodosCrear+='Instruccion'+str(CountInstruccion)+'[label="Instruccion"]\n'
            NodeData+='Instrucciones'+str(CountInstrucciones-1)+'-> Instruccion'+str(CountInstruccion)+'\n'
            NodeData+='Instruccion'+str(CountInstruccion)+'->Proceso_Registros\n'
            self.instruccion_Registros()
            
            NodeData+='Instrucciones'+str(CountInstrucciones-1)+'-> Instrucciones'+str(CountInstrucciones)+'\n'
            self.lista_Instrucciones()
        elif self.listaTokens[i].lexema == 'claves':
            CountInstrucciones+=1
            CountInstruccion+=1
            NodosCrear+='Instrucciones'+str(CountInstrucciones)+'[label="Instrucciones"]\n'
            NodosCrear+='Instruccion'+str(CountInstruccion)+'[label="Instruccion"]\n'
            NodeData+='Instrucciones'+str(CountInstrucciones-1)+'-> Instruccion'+str(CountInstruccion)+'\n'
            NodeData+='Instruccion'+str(CountInstruccion)+'->Proceso_Claves\n'
            self.instruccion_Claves()
            
            NodeData+='Instrucciones'+str(CountInstrucciones-1)+'-> Instrucciones'+str(CountInstrucciones)+'\n'
            self.lista_Instrucciones()
        elif self.listaTokens[i].lexema == 'CommentSimple':
            i+=1
            self.lista_Instrucciones()
        elif self.listaTokens[i].lexema=='ComillaSimple':
            i+=1
            self.lista_Instrucciones()
        elif self.listaTokens[i].lexema=='imprimir':
            CountInstrucciones+=1
            CountInstruccion+=1
            NodosCrear+='Instrucciones'+str(CountInstrucciones)+'[label="Instrucciones"]\n'
            NodosCrear+='Instruccion'+str(CountInstruccion)+'[label="Instruccion"]\n'
            NodosCrear+='ProcesoImprimir'+str(CountProceso)+'[label="ProcesoImprimir"]\n'
            NodeData+='Instrucciones'+str(CountInstrucciones-1)+'-> Instruccion'+str(CountInstruccion)+'\n'
            NodeData+='Instruccion'+str(CountInstruccion)+'->ProcesoImprimir'+str(CountProceso)+'\n'
            self.instruccion_Imprimir()
            
            NodeData+='Instrucciones'+str(CountInstrucciones-1)+'-> Instrucciones'+str(CountInstrucciones)+'\n'
            self.lista_Instrucciones()
        elif self.listaTokens[i].lexema=='imprimirln':
            CountInstrucciones+=1
            CountInstruccion+=1
            NodosCrear+='Instrucciones'+str(CountInstrucciones)+'[label="Instrucciones"]\n'
            NodosCrear+='Instruccion'+str(CountInstruccion)+'[label="Instruccion"]\n'
            NodosCrear+='ProcesoImprimirln'+str(CountProceso)+'[label="ProcesoImprimirln"]\n'
            NodeData+='Instrucciones'+str(CountInstrucciones-1)+'-> Instruccion'+str(CountInstruccion)+'\n'
            NodeData+='Instruccion'+str(CountInstruccion)+'->ProcesoImprimirln'+str(CountProceso)+'\n'
            self.instruccion_Imprimirln()
            
            NodeData+='Instrucciones'+str(CountInstrucciones-1)+'-> Instrucciones'+str(CountInstrucciones)+'\n'
            self.lista_Instrucciones()
        elif self.listaTokens[i].lexema=='conteo':
            CountInstrucciones+=1
            CountInstruccion+=1
            NodosCrear+='Instrucciones'+str(CountInstrucciones)+'[label="Instrucciones"]\n'
            NodosCrear+='Instruccion'+str(CountInstruccion)+'[label="Instruccion"]\n'
            NodosCrear+='ProcesoConteo'+str(CountProceso)+'[label="ProcesoConteo"]\n'
            NodeData+='Instrucciones'+str(CountInstrucciones-1)+'-> Instruccion'+str(CountInstruccion)+'\n'
            NodeData+='Instruccion'+str(CountInstruccion)+'->ProcesoConteo'+str(CountProceso)+'\n'
            self.instruccion_Conteo()
            
            NodeData+='Instrucciones'+str(CountInstrucciones-1)+'-> Instrucciones'+str(CountInstrucciones)+'\n'
            self.lista_Instrucciones()
        elif self.listaTokens[i].lexema=='promedio':
            CountInstrucciones+=1
            CountInstruccion+=1
            NodosCrear+='Instrucciones'+str(CountInstrucciones)+'[label="Instrucciones"]\n'
            NodosCrear+='Instruccion'+str(CountInstruccion)+'[label="Instruccion"]\n'
            NodosCrear+='ProcesoPromedio'+str(CountProceso)+'[label="ProcesoPromedio"]\n'
            NodeData+='Instrucciones'+str(CountInstrucciones-1)+'-> Instruccion'+str(CountInstruccion)+'\n'
            NodeData+='Instruccion'+str(CountInstruccion)+'->ProcesoPromedio'+str(CountProceso)+'\n'
            self.instruccion_Promedio()
            
            NodeData+='Instrucciones'+str(CountInstrucciones-1)+'-> Instrucciones'+str(CountInstrucciones)+'\n'
            self.lista_Instrucciones()
        elif self.listaTokens[i].lexema=='contarsi':
            CountInstrucciones+=1
            CountInstruccion+=1
            NodosCrear+='Instrucciones'+str(CountInstrucciones)+'[label="Instrucciones"]\n'
            NodosCrear+='Instruccion'+str(CountInstruccion)+'[label="Instruccion"]\n'
            NodosCrear+='ProcesoContarSi'+str(CountProceso)+'[label="ProcesoContarSi"]\n'
            NodeData+='Instrucciones'+str(CountInstrucciones-1)+'-> Instruccion'+str(CountInstruccion)+'\n'
            NodeData+='Instruccion'+str(CountInstruccion)+'->ProcesoContarSi'+str(CountProceso)+'\n'
            self.instruccion_Contarsi()
            
            NodeData+='Instrucciones'+str(CountInstrucciones-1)+'-> Instrucciones'+str(CountInstrucciones)+'\n'
            self.lista_Instrucciones()
        elif self.listaTokens[i].lexema=='datos':
            CountInstrucciones+=1
            CountInstruccion+=1
            NodosCrear+='Instrucciones'+str(CountInstrucciones)+'[label="Instrucciones"]\n'
            NodosCrear+='Instruccion'+str(CountInstruccion)+'[label="Instruccion"]\n'
            NodosCrear+='ProcesoDatos'+str(CountProceso)+'[label="ProcesoDatos"]\n'
            NodeData+='Instrucciones'+str(CountInstrucciones-1)+'-> Instruccion'+str(CountInstruccion)+'\n'
            NodeData+='Instruccion'+str(CountInstruccion)+'->ProcesoDatos'+str(CountProceso)+'\n'
            self.instruccion_Datos()
            
            NodeData+='Instrucciones'+str(CountInstrucciones-1)+'-> Instrucciones'+str(CountInstrucciones)+'\n'
            self.lista_Instrucciones()
        elif self.listaTokens[i].lexema=='sumar':
            CountInstrucciones+=1
            CountInstruccion+=1
            NodosCrear+='Instrucciones'+str(CountInstrucciones)+'[label="Instrucciones"]\n'
            NodosCrear+='Instruccion'+str(CountInstruccion)+'[label="Instruccion"]\n'
            NodosCrear+='ProcesoSumar'+str(CountProceso)+'[label="ProcesoSumar"]\n'
            NodeData+='Instrucciones'+str(CountInstrucciones-1)+'-> Instruccion'+str(CountInstruccion)+'\n'
            NodeData+='Instruccion'+str(CountInstruccion)+'->ProcesoSumar'+str(CountProceso)+'\n'
            self.instruccion_Sumar()
            
            NodeData+='Instrucciones'+str(CountInstrucciones-1)+'-> Instrucciones'+str(CountInstrucciones)+'\n'
            self.lista_Instrucciones()
        elif self.listaTokens[i].lexema=='max':
            CountInstrucciones+=1
            CountInstruccion+=1
            NodosCrear+='Instrucciones'+str(CountInstrucciones)+'[label="Instrucciones"]\n'
            NodosCrear+='Instruccion'+str(CountInstruccion)+'[label="Instruccion"]\n'
            NodosCrear+='ProcesoMax'+str(CountProceso)+'[label="ProcesoMax"]\n'
            NodeData+='Instrucciones'+str(CountInstrucciones-1)+'-> Instruccion'+str(CountInstruccion)+'\n'
            NodeData+='Instruccion'+str(CountInstruccion)+'->ProcesoMax'+str(CountProceso)+'\n'
            self.instruccion_max()
            
            NodeData+='Instrucciones'+str(CountInstrucciones-1)+'-> Instrucciones'+str(CountInstrucciones)+'\n'
            self.lista_Instrucciones()
        elif self.listaTokens[i].lexema=='min':
            CountInstrucciones+=1
            CountInstruccion+=1
            NodosCrear+='Instrucciones'+str(CountInstrucciones)+'[label="Instrucciones"]\n'
            NodosCrear+='Instruccion'+str(CountInstruccion)+'[label="Instruccion"]\n'
            NodosCrear+='ProcesoMin'+str(CountProceso)+'[label="ProcesoMin"]\n'
            NodeData+='Instrucciones'+str(CountInstrucciones-1)+'-> Instruccion'+str(CountInstruccion)+'\n'
            NodeData+='Instruccion'+str(CountInstruccion)+'->ProcesoMin'+str(CountProceso)+'\n'
            self.instruccion_min()
            
            NodeData+='Instrucciones'+str(CountInstrucciones-1)+'-> Instrucciones'+str(CountInstrucciones)+'\n'
            self.lista_Instrucciones()
        elif self.listaTokens[i].lexema=='exportar':
            CountInstrucciones+=1
            CountInstruccion+=1
            NodosCrear+='Instrucciones'+str(CountInstrucciones)+'[label="Instrucciones"]\n'
            NodosCrear+='Instruccion'+str(CountInstruccion)+'[label="Instruccion"]\n'
            NodosCrear+='ProcesoExportar'+str(CountProceso)+'[label="ProcesoExportar"]\n'
            NodeData+='Instrucciones'+str(CountInstrucciones-1)+'-> Instruccion'+str(CountInstruccion)+'\n'
            NodeData+='Instruccion'+str(CountInstruccion)+'->ProcesoExportar'+str(CountProceso)+'\n'
            self.instruccion_Exportar()
            
            NodeData+='Instrucciones'+str(CountInstrucciones-1)+'-> Instrucciones'+str(CountInstrucciones)+'\n'
            self.lista_Instrucciones()
        elif self.listaTokens[i].lexema=='Fin':
            CountInstrucciones+=1
            CountInstruccion+=1
            NodosCrear+='Instruccion'+str(CountInstruccion)+'[label="Instruccion"]\n'
            NodeData+='Instrucciones'+str(CountInstrucciones-1)+'-> Instruccion'+str(CountInstruccion)+'->Fin\n'
            print('fin analisis sintactico')
     
    ##EMPIEZA LAS FUNCIONES PARA LA INSTRUCCION DE CLAVES
    def instruccion_Claves(self):
        global i, NodeData, CountClave, CountSimboloIgual, NodosCrear, CountSimboloCorchete,CountListClaves
        global CountClave
        if self.listaTokens[i].lexema == 'claves':
            NodeData+='Proceso_Claves-> TokenClaves\n'
            NodeData+='TokenClaves-> Claves\n'
            i+=1

            if self.listaTokens[i].lexema == 'igual':
                NodosCrear+='Simboloigual'+str(CountSimboloIgual)+'[label="SimboloIgual"]\n'
                NodeData+='Proceso_Claves-> Simboloigual'+str(CountSimboloIgual)+'\n'
                NodosCrear+='igual'+str(CountSimboloIgual)+'[label="="]\n'
                NodeData+='Simboloigual'+str(CountSimboloIgual)+'->igual'+str(CountSimboloIgual)+'\n'
                CountSimboloIgual+=1
                i+=1
                if self.listaTokens[i].lexema == 'corchete1':
                    NodosCrear+='SimboloCorchete'+str(CountSimboloCorchete)+'[label="SimboloCorchete"]\n'
                    NodosCrear+='CorcheteA'+str(CountSimboloCorchete)+'[label="["]\n'
                    NodeData+='Proceso_Claves-> SimboloCorchete'+str(CountSimboloCorchete)+'->CorcheteA'+str(CountSimboloCorchete)+'\n'
                    CountSimboloCorchete+=1
                    i+=1
                    NodosCrear+='ListClaves'+str(CountListClaves)+'[label="ListClaves"]\n'
                    NodeData+='Proceso_Claves-> ListClaves'+str(CountListClaves)+'\n'
                    self.lista_Claves()
                    if self.listaTokens[i].lexema== 'corchete2':
                        NodosCrear+='SimboloCorchete'+str(CountSimboloCorchete)+'[label="SimboloCorchete"]\n'
                        NodosCrear+='CorcheteC'+str(CountSimboloCorchete)+'[label="]"]\n'
                        NodeData+='Proceso_Claves-> SimboloCorchete'+str(CountSimboloCorchete)+'->CorcheteC'+str(CountSimboloCorchete)+'\n'
                        i+=1
                        CountSimboloCorchete+=1
                        print('finalizaron claves')
                    else:
                        e='Error sintactico en fila '+str(self.listaTokens[i].Fila)+' y columna '+str(self.listaTokens[i].Columna)+" revisar"
                        self.listaErrores.append(Errores(self.listaTokens[i].Fila, self.listaTokens[i].Columna, e, "]"))
                else:
                        e='Error sintactico en fila '+str(self.listaTokens[i].Fila)+' y columna '+str(self.listaTokens[i].Columna)+" revisar"
                        self.listaErrores.append(Errores(self.listaTokens[i].Fila, self.listaTokens[i].Columna, e, "["))
            else:
                        e='Error sintactico en fila '+str(self.listaTokens[i].Fila)+' y columna '+str(self.listaTokens[i].Columna)+" revisar"
                        self.listaErrores.append(Errores(self.listaTokens[i].Fila, self.listaTokens[i].Columna, e, "="))
        else:
                        e='Error sintactico en fila '+str(self.listaTokens[i].Fila)+' y columna '+str(self.listaTokens[i].Columna)+" revisar"
                        self.listaErrores.append(Errores(self.listaTokens[i].Fila, self.listaTokens[i].Columna, e, "claves"))
    def lista_Claves(self):
        global NodeData, CountListClaves, CountClave, NodosCrear
        NodosCrear+='Clave'+str(CountClave)+'[label="Clave"]\n'
        NodeData+='ListClaves'+str(CountListClaves)+'->Clave'+str(CountClave)+'\n'
        CountListClaves+=1
        CountClave+=1
        self.clave()

    def clave(self):
        global i, NodeData, CountClave, NodosCrear, CountCadena
        if self.listaTokens[i].lexema == 'ComillaDoble':
            i+=1
            self.SeparadorClaves() 
        elif self.listaTokens[i].token == 'cadena':
            cadena = self.listaTokens[i].lexema
            self.listClaves.append(cadena)
            
            print(cadena)
            NodosCrear+='Cadena'+str(CountCadena)+'[label="Cadena"]\n'
            NodeData+='Clave'+str(CountClave-1)+'->Cadena'+str(CountCadena)+'->'+cadena+'\n'
            CountCadena+=1
            i+=1
            self.SeparadorClaves()
        else:
            e='Error sintactico en fila '+str(self.listaTokens[i].Fila)+' y columna '+str(self.listaTokens[i].Columna)+" revisar"
            self.listaErrores.append(Errores(self.listaTokens[i].Fila, self.listaTokens[i].Columna, e, "cadena o ComillaDoble"))

    def SeparadorClaves(self):
        global i, NodeData, CountClave, CountComa, NodosCrear
        if self.listaTokens[i].lexema == 'coma':
            NodosCrear+='SimboloComa'+str(CountComa)+'[label="Coma"]\n'
            NodosCrear+='Coma'+str(CountComa)+'[label=","]\n'
            NodosCrear+='Clave'+str(CountClave)+'[label="Clave"]\n'
            NodeData+='Clave'+str(CountClave-1)+'-> SimboloComa'+str(CountComa)+'-> Coma'+str(CountComa)+'\n'
            CountComa+=1
            NodeData+='Clave'+str(CountClave-1)+'->Clave'+str(CountClave)+'\n'
            CountClave+=1
            i+=1
            self.clave()
        else:
            self.clave()
    ##TERMINA LAS FUNCIONES PARA LA INSTRUCCION DE CLAVES   
    
    ##EMPIEZA LAS FUNCIONES PARA LA INSTRUCCION DE REGISTROS
    def instruccion_Registros(self):
        global i, NodeData, CountRegistro, CountSimboloIgual, NodosCrear, CountSimboloCorchete,CountListRegistro
        global CountClave
        
        if self.listaTokens[i].lexema == 'registros':
            NodeData+='Proceso_Registros-> TokenRegistros\n'
            NodeData+='TokenRegistros-> Registros\n'
            i+=1
            if self.listaTokens[i].lexema == 'igual':
                NodosCrear+='Simboloigual'+str(CountSimboloIgual)+'[label="SimboloIgual"]\n'
                NodeData+='Proceso_Registros-> Simboloigual'+str(CountSimboloIgual)+'\n'
                NodosCrear+='igual'+str(CountSimboloIgual)+'[label="="]\n'
                NodeData+='Simboloigual'+str(CountSimboloIgual)+'->igual'+str(CountSimboloIgual)+'\n'
                CountSimboloIgual+=1
                i+=1
                if self.listaTokens[i].lexema == 'corchete1':
                    NodosCrear+='SimboloCorchete'+str(CountSimboloCorchete)+'[label="SimboloCorchete"]\n'
                    NodosCrear+='CorcheteA'+str(CountSimboloCorchete)+'[label="["]\n'
                    NodeData+='Proceso_Registros-> SimboloCorchete'+str(CountSimboloCorchete)+'->CorcheteA'+str(CountSimboloCorchete)+'\n'
                    CountSimboloCorchete+=1
                    i+=1
                    NodosCrear+='ListRegistros'+str(CountListRegistro)+'[label="ListRegistros"]\n'
                    NodeData+='Proceso_Registros-> ListRegistros'+str(CountListRegistro)+'\n'
                    self.lista_Registros()
                    if self.listaTokens[i].lexema== 'corchete2':
                        NodosCrear+='SimboloCorchete'+str(CountSimboloCorchete)+'[label="SimboloCorchete"]\n'
                        NodosCrear+='CorcheteC'+str(CountSimboloCorchete)+'[label="]"]\n'
                        NodeData+='Proceso_Registros-> SimboloCorchete'+str(CountSimboloCorchete)+'->CorcheteC'+str(CountSimboloCorchete)+'\n'
                        i+=1
                        CountSimboloCorchete+=1
                        print('finalizaron registros')
                    else:
                        e='Error sintactico en fila '+str(self.listaTokens[i].Fila)+' y columna '+str(self.listaTokens[i].Columna)+" revisar"
                        self.listaErrores.append(Errores(self.listaTokens[i].Fila, self.listaTokens[i].Columna, e, "]"))
                else:
                        e='Error sintactico en fila '+str(self.listaTokens[i].Fila)+' y columna '+str(self.listaTokens[i].Columna)+" revisar"
                        self.listaErrores.append(Errores(self.listaTokens[i].Fila, self.listaTokens[i].Columna, e, "["))
            else:
                        e='Error sintactico en fila '+str(self.listaTokens[i].Fila)+' y columna '+str(self.listaTokens[i].Columna)+" revisar"
                        self.listaErrores.append(Errores(self.listaTokens[i].Fila, self.listaTokens[i].Columna, e, "="))
        else:
                        e='Error sintactico en fila '+str(self.listaTokens[i].Fila)+' y columna '+str(self.listaTokens[i].Columna)+" revisar"
                        self.listaErrores.append(Errores(self.listaTokens[i].Fila, self.listaTokens[i].Columna, e, "registros"))
    
    def lista_Registros(self):
        global NodeData, CountListRegistro, CountRegistro, NodosCrear,CountValue
        NodosCrear+='Registro'+str(CountRegistro)+'[label="Registro"]\n'
        NodeData+='ListRegistros'+str(CountListRegistro)+'->Registro'+str(CountRegistro)+'\n'
        CountListRegistro+=1
        self.registro()

    def registro(self):
        global i, NodeData, CountClave, NodosCrear, CountCadena, CountEntero, CountReal, CountLlave, CountRegistro, CountValue
        global register
        if self.listaTokens[i].lexema == 'ComillaDoble':
            i+=1
            self.SeparadorRegistros()
        elif self.listaTokens[i].token == 'cadena':
            cadena = self.listaTokens[i].lexema
            NodosCrear+='Cadena'+str(CountCadena)+'[label="Cadena"]\n'
            NodosCrear+='CadenaTexto'+str(CountCadena)+'[label="'+cadena+'"]\n'
            NodeData+='Value'+str(CountValue-1)+'->Cadena'+str(CountCadena)+'->CadenaTexto'+str(CountCadena)+'\n'
            CountCadena+=1
            register.append(cadena)
            i+=1
            self.SeparadorRegistros()
        elif self.listaTokens[i].token == 'entero':
            numeroEntero = self.listaTokens[i].lexema
            NodosCrear+='Entero'+str(CountEntero)+'[label="Entero"]\n'
            NodosCrear+='NumE'+str(CountEntero)+'[label="'+numeroEntero+'"]\n'
            NodeData+='Value'+str(CountValue-1)+'->Entero'+str(CountEntero)+'->NumE'+str(CountEntero)+'\n'
            CountEntero+=1
            register.append(numeroEntero)
            i+=1
            self.SeparadorRegistros()
            self.registro()
        elif self.listaTokens[i].token == 'real':
            numeroEntero = self.listaTokens[i].lexema
            NodosCrear+='Real'+str(CountReal)+'[label="Real"]\n'
            NodosCrear+='NumR'+str(CountReal)+'[label="'+numeroEntero+'"]\n'
            NodeData+='Value'+str(CountValue-1)+'->Real'+str(CountReal)+'->NumR'+str(CountReal)+'\n'
            CountReal+=1
            register.append(numeroEntero)
            i+=1
            self.SeparadorRegistros()
        elif self.listaTokens[i].lexema == 'llave1':
            i+=1
            CountRegistro+=1
            NodosCrear+='SimbolollaveA'+str(CountLlave)+'[label="SimboloLlave_A"]\n'
            NodosCrear+='llaveA'+str(CountLlave)+'[label="{"]\n'
            NodosCrear+='Registro'+str(CountRegistro)+'[label="Registro"]\n'
            NodosCrear+='listValues'+str(CountRegistro-1)+'[label="ListaValues"]\n'
            NodosCrear+='Value'+str(CountValue)+'[label="Value"]\n'
            NodeData+='Registro'+str(CountRegistro-1)+'->SimbolollaveA'+str(CountLlave)+'->llaveA'+str(CountLlave)+'\n'
            NodeData+='Registro'+str(CountRegistro-1)+'->listValues'+str(CountRegistro-1)+'->Value'+str(CountValue)+'\n'
            CountLlave+=1
            CountValue+=1
            self.registro()
        elif self.listaTokens[i].lexema == 'llave2':
            i+=1
            NodosCrear+='SimbolollaveC'+str(CountLlave)+'[label="SimboloLlave_C"]\n'
            NodosCrear+='llaveC'+str(CountLlave)+'[label="}"]\n'
            NodeData+='Registro'+str(CountRegistro-1)+'->SimbolollaveC'+str(CountLlave)+'->llaveC'+str(CountLlave)+'\n'
            NodeData+='Registro'+str(CountRegistro-1)+'-> Registro'+str(CountRegistro)+'\n'
            CountLlave+=1
            self.listRegisters.append(register)
            register=[]
            self.registro()
        else:
            e='Error sintactico en fila '+str(self.listaTokens[i].Fila)+' y columna '+str(self.listaTokens[i].Columna)+" revisar"
            self.listaErrores.append(Errores(self.listaTokens[i].Fila, self.listaTokens[i].Columna, e, "simbolo, valor o cadena"))
    
    def SeparadorRegistros(self):
        global i, NodeData, NodosCrear, CountComa, CountRegistro,CountValue
        if self.listaTokens[i].lexema =='llave2':
            pass
        elif self.listaTokens[i].lexema == 'coma':
            
            
            NodosCrear+='Value'+str(CountValue)+'[label="Value"]\n'
            
            NodeData+='Value'+str(CountValue-1)+'-> Value'+str(CountValue)+'\n'
            CountValue+=1
            
            
            i+=1
            self.registro()
        else:
            self.registro()
    #Terminan las funciones de Registros

    ## EMPIEZA LA FUNCION IMPRIMIR
    def instruccion_Imprimir(self):
        global i, ReturnText, CountSimboloIgual,contadorImprimir, NodeData, NodosCrear, CountProceso, countToken, CountSimboloPa, CountCadena
        
        if self.listaTokens[i].lexema == 'imprimir':
            NodosCrear+='tokenImprimir'+str(countToken)+'[label="tokenImprimir"]\n'
            NodosCrear+='imprimir'+str(countToken)+'[label="imprimir"]\n'
            NodeData+='ProcesoImprimir'+str(CountProceso)+'->tokenImprimir'+str(countToken)+'->imprimir'+str(countToken)+'\n'
            i+=1
            if self.listaTokens[i].lexema == 'parentesis1':
                NodosCrear+='SimboloparentesisA'+str(CountSimboloPa)+'[label="SimboloparentesisA"]\n'
                NodosCrear+='parentesisA'+str(CountSimboloPa)+'[label="("]\n'
                NodeData+='ProcesoImprimir'+str(CountProceso)+'->SimboloparentesisA'+str(CountSimboloPa)+'->parentesisA'+str(CountSimboloPa)+'\n'
                CountSimboloPa+=1
                i+=1
                if self.listaTokens[i].lexema == 'ComillaDoble':
                    i+=1
                    if self.listaTokens[i].token == 'cadena':
                        text =  self.listaTokens[i].lexema
                        NodosCrear+='Cadena'+str(CountCadena)+'[label="Cadena"]\n'
                        NodosCrear+='CadenaText'+str(CountCadena)+'[label="\''+text+'\'"]\n'
                        NodeData+='ProcesoImprimir'+str(CountProceso)+'->Cadena'+str(CountCadena)+'->CadenaText'+str(CountCadena)+'\n'
                        CountCadena+=1
                        i+=1
                        if self.listaTokens[i].lexema == 'ComillaDoble':
                            i+=1
                            if self.listaTokens[i].lexema== 'parentesis2':
                                NodosCrear+='SimboloparentesisC'+str(CountSimboloPa)+'[label="SimboloparentesisC"]\n'
                                NodosCrear+='parentesisC'+str(CountSimboloPa)+'[label=")"]\n'
                                NodeData+='ProcesoImprimir'+str(CountProceso)+'->SimboloparentesisC'+str(CountSimboloPa)+'->parentesisC'+str(CountSimboloPa)+'\n'
                                CountSimboloPa+=1
                                i+=1
                                if self.listaTokens[i].lexema== 'puntoycoma':
                                    NodosCrear+='SimboloPuntoyComa'+str(CountSimboloIgual)+'[label="SimboloPuntoYComa"]\n'
                                    NodosCrear+='puntoYComa'+str(CountSimboloIgual)+'[label=";"]\n'
                                    NodeData+='ProcesoImprimir'+str(CountProceso)+'->SimboloPuntoyComa'+str(CountSimboloIgual)+'->puntoYComa'+str(CountSimboloIgual)+'\n'
                                    CountSimboloIgual+=1
                                    i+=1
                                    if contadorImprimir==0:
                                        ReturnText+=text
                                    else:
                                        ReturnText+='-->'+text
                                        contadorImprimir=0
                                else:
                                    e='Error sintactico en fila '+str(self.listaTokens[i].Fila)+' y columna '+str(self.listaTokens[i].Columna)+" revisar"
                                    self.listaErrores.append(Errores(self.listaTokens[i].Fila, self.listaTokens[i].Columna, e, ";"))
                            else:
                                e='Error sintactico en fila '+str(self.listaTokens[i].Fila)+' y columna '+str(self.listaTokens[i].Columna)+" revisar"
                                self.listaErrores.append(Errores(self.listaTokens[i].Fila, self.listaTokens[i].Columna, e, "]"))
                        else:
                            e='Error sintactico en fila '+str(self.listaTokens[i].Fila)+' y columna '+str(self.listaTokens[i].Columna)+" revisar"
                            self.listaErrores.append(Errores(self.listaTokens[i].Fila, self.listaTokens[i].Columna, e, "ComillaDoble"))
                    else:
                        e='Error sintactico en fila '+str(self.listaTokens[i].Fila)+' y columna '+str(self.listaTokens[i].Columna)+" revisar"
                        self.listaErrores.append(Errores(self.listaTokens[i].Fila, self.listaTokens[i].Columna, e, "Cadena"))
                else:
                    e='Error sintactico en fila '+str(self.listaTokens[i].Fila)+' y columna '+str(self.listaTokens[i].Columna)+" revisar"
                    self.listaErrores.append(Errores(self.listaTokens[i].Fila, self.listaTokens[i].Columna, e, "ComillaDoble"))
            else:
                e='Error sintactico en fila '+str(self.listaTokens[i].Fila)+' y columna '+str(self.listaTokens[i].Columna)+" revisar"
                self.listaErrores.append(Errores(self.listaTokens[i].Fila, self.listaTokens[i].Columna, e, "("))
        else:
            e='Error sintactico en fila '+str(self.listaTokens[i].Fila)+' y columna '+str(self.listaTokens[i].Columna)+" revisar"
            self.listaErrores.append(Errores(self.listaTokens[i].Fila, self.listaTokens[i].Columna, e, "imprimir"))
        countToken+=1                              
        CountProceso+=1
    ## Aquí Termina La Funcion Imprimir

    ##EMPIEZA LA FUNCION IMPRIMIRLN
    def instruccion_Imprimirln(self):
        global i, ReturnText,contadorImprimir, NodeData, NodosCrear, CountSimboloPa, CountCadena, CountSimboloIgual,CountProceso, countToken
        
        if self.listaTokens[i].lexema == 'imprimirln':
            i+=1
            NodosCrear+='tokenImprimirln'+str(countToken)+'[label="tokenImprimirln"]\n'
            NodosCrear+='imprimirln'+str(countToken)+'[label="imprimirln"]\n'
            NodeData+='ProcesoImprimirln'+str(CountProceso)+'->tokenImprimirln'+str(countToken)+'->imprimirln'+str(countToken)+'\n'
            if self.listaTokens[i].lexema == 'parentesis1':
                NodosCrear+='SimboloparentesisA'+str(CountSimboloPa)+'[label="SimboloparentesisA"]\n'
                NodosCrear+='parentesisA'+str(CountSimboloPa)+'[label="("]\n'
                NodeData+='ProcesoImprimirln'+str(CountProceso)+'->SimboloparentesisA'+str(CountSimboloPa)+'->parentesisA'+str(CountSimboloPa)+'\n'
                CountSimboloPa+=1
                i+=1
                if self.listaTokens[i].lexema == 'ComillaDoble':
                    i+=1
                    if self.listaTokens[i].token == 'cadena':
                        text = self.listaTokens[i].lexema
                        NodosCrear+='Cadena'+str(CountCadena)+'[label="SimboloparentesisA"]\n'
                        NodosCrear+='CadenaText'+str(CountCadena)+'[label="\''+text+'\'"]\n'
                        NodeData+='ProcesoImprimirln'+str(CountProceso)+'->Cadena'+str(CountCadena)+'->CadenaText'+str(CountCadena)+'\n'
                        CountCadena+=1
                        i+=1
                        if self.listaTokens[i].lexema == 'ComillaDoble':
                            
                            i+=1
                            if self.listaTokens[i].lexema== 'parentesis2':
                                NodosCrear+='SimboloparentesisC'+str(CountSimboloPa)+'[label="SimboloparentesisC"]\n'
                                NodosCrear+='parentesisC'+str(CountSimboloPa)+'[label=")"]\n'
                                NodeData+='ProcesoImprimirln'+str(CountProceso)+'->SimboloparentesisC'+str(CountSimboloPa)+'->parentesisC'+str(CountSimboloPa)+'\n'
                                CountSimboloPa+=1
                                i+=1
                                if self.listaTokens[i].lexema== 'puntoycoma':
                                    NodosCrear+='SimboloPuntoyComa'+str(CountSimboloIgual)+'[label="SimboloPuntoYComa"]\n'
                                    NodosCrear+='puntoYComa'+str(CountSimboloIgual)+'[label=";"]\n'
                                    NodeData+='ProcesoImprimirln'+str(CountProceso)+'->SimboloPuntoyComa'+str(CountSimboloIgual)+'->puntoYComa'+str(CountSimboloIgual)+'\n'
                                    CountSimboloIgual+=1
                                    i+=1
                                    if contadorImprimir==0:
                                        ReturnText+=text
                                    else:
                                        ReturnText+='\n-->'+text+'\n'
                                        contadorImprimir=1
                                else:
                                    e='Error sintactico en fila '+str(self.listaTokens[i].Fila)+' y columna '+str(self.listaTokens[i].Columna)+" revisar"
                                    self.listaErrores.append(Errores(self.listaTokens[i].Fila, self.listaTokens[i].Columna, e, ";"))
                            else:
                                e='Error sintactico en fila '+str(self.listaTokens[i].Fila)+' y columna '+str(self.listaTokens[i].Columna)+" revisar"
                                self.listaErrores.append(Errores(self.listaTokens[i].Fila, self.listaTokens[i].Columna, e, "]"))
                        else:
                            e='Error sintactico en fila '+str(self.listaTokens[i].Fila)+' y columna '+str(self.listaTokens[i].Columna)+" revisar"
                            self.listaErrores.append(Errores(self.listaTokens[i].Fila, self.listaTokens[i].Columna, e, "ComillaDoble"))
                    else:
                        e='Error sintactico en fila '+str(self.listaTokens[i].Fila)+' y columna '+str(self.listaTokens[i].Columna)+" revisar"
                        self.listaErrores.append(Errores(self.listaTokens[i].Fila, self.listaTokens[i].Columna, e, "Cadena"))
                else:
                    e='Error sintactico en fila '+str(self.listaTokens[i].Fila)+' y columna '+str(self.listaTokens[i].Columna)+" revisar"
                    self.listaErrores.append(Errores(self.listaTokens[i].Fila, self.listaTokens[i].Columna, e, "ComillaDoble"))
            else:
                e='Error sintactico en fila '+str(self.listaTokens[i].Fila)+' y columna '+str(self.listaTokens[i].Columna)+" revisar"
                self.listaErrores.append(Errores(self.listaTokens[i].Fila, self.listaTokens[i].Columna, e, "("))
        else:
            e='Error sintactico en fila '+str(self.listaTokens[i].Fila)+' y columna '+str(self.listaTokens[i].Columna)+" revisar"
            self.listaErrores.append(Errores(self.listaTokens[i].Fila, self.listaTokens[i].Columna, e, "imprimirln"))
        countToken+=1
        CountProceso+=1
    ##TERMINA LA FUNCION IMPRIMIRLN

    def instruccion_Conteo(self):
        global i, ReturnText, contadorImprimir, NodeData, NodosCrear, countToken, CountProceso, CountSimboloPa, CountSimboloIgual
        
        if self.listaTokens[i].lexema == 'conteo':
            NodosCrear+='tokenConteo'+str(countToken)+'[label="tokenConteo"]\n'
            NodosCrear+='Conteo'+str(countToken)+'[label="Conteo"]\n'
            NodeData+='ProcesoConteo'+str(CountProceso)+'->tokenConteo'+str(countToken)+'->Conteo'+str(countToken)+'\n'
            i+=1
            if self.listaTokens[i].lexema == 'parentesis1':
                NodosCrear+='SimboloparentesisA'+str(CountSimboloPa)+'[label="SimboloparentesisA"]\n'
                NodosCrear+='parentesisA'+str(CountSimboloPa)+'[label="("]\n'
                NodeData+='ProcesoConteo'+str(CountProceso)+'->SimboloparentesisA'+str(CountSimboloPa)+'->parentesisA'+str(CountSimboloPa)+'\n'
                CountSimboloPa+=1
                i+=1
                if self.listaTokens[i].lexema== 'parentesis2':
                    NodosCrear+='SimboloparentesisC'+str(CountSimboloPa)+'[label="SimboloparentesisC"]\n'
                    NodosCrear+='parentesisC'+str(CountSimboloPa)+'[label=")"]\n'
                    NodeData+='ProcesoConteo'+str(CountProceso)+'->SimboloparentesisC'+str(CountSimboloPa)+'->parentesisC'+str(CountSimboloPa)+'\n'
                    CountSimboloPa+=1
                    i+=1
                    if self.listaTokens[i].lexema== 'puntoycoma':
                        NodosCrear+='SimboloPuntoyComa'+str(CountSimboloIgual)+'[label="SimboloPuntoYComa"]\n'
                        NodosCrear+='puntoYComa'+str(CountSimboloIgual)+'[label=";"]\n'
                        NodeData+='ProcesoConteo'+str(CountProceso)+'->SimboloPuntoyComa'+str(CountSimboloIgual)+'->puntoYComa'+str(CountSimboloIgual)+'\n'
                        CountSimboloIgual+=1
                        i+=1
                        print("cantidad de registros: "+str(len(self.listRegisters)))
                        ReturnText+='\n-->'+str(len(self.listRegisters))
                        contadorImprimir=1
                    else:
                        e='Error sintactico en fila '+str(self.listaTokens[i].Fila)+' y columna '+str(self.listaTokens[i].Columna)+" revisar"
                        self.listaErrores.append(Errores(self.listaTokens[i].Fila, self.listaTokens[i].Columna, e, ";"))
                else:
                    e='Error sintactico en fila '+str(self.listaTokens[i].Fila)+' y columna '+str(self.listaTokens[i].Columna)+" revisar"
                    self.listaErrores.append(Errores(self.listaTokens[i].Fila, self.listaTokens[i].Columna, e, ")"))
            else:
                e='Error sintactico en fila '+str(self.listaTokens[i].Fila)+' y columna '+str(self.listaTokens[i].Columna)+" revisar"
                self.listaErrores.append(Errores(self.listaTokens[i].Fila, self.listaTokens[i].Columna, e, "("))
        else:
            e='Error sintactico en fila '+str(self.listaTokens[i].Fila)+' y columna '+str(self.listaTokens[i].Columna)+" revisar"
            self.listaErrores.append(Errores(self.listaTokens[i].Fila, self.listaTokens[i].Columna, e, "conteo"))
        countToken+=1                
        CountProceso+=1
    ## empieza instrucciones promedio
    def instruccion_Promedio(self):
        global i, ReturnText, contadorImprimir, NodeData,countToken, NodosCrear, CountSimboloPa, CountCadena, CountSimboloIgual, CountReal, CountProceso
        
        if self.listaTokens[i].lexema == 'promedio':
            NodosCrear+='tokenPromedio'+str(countToken)+'[label="tokenPromedio"]\n'
            NodosCrear+='Promedio'+str(countToken)+'[label="Promedio"]\n'
            NodeData+='ProcesoPromedio'+str(CountProceso)+'->tokenPromedio'+str(countToken)+'->Promedio'+str(countToken)+'\n'
            i+=1
            if self.listaTokens[i].lexema == 'parentesis1':
                NodosCrear+='SimboloparentesisA'+str(CountSimboloPa)+'[label="SimboloparentesisA"]\n'
                NodosCrear+='parentesisA'+str(CountSimboloPa)+'[label="("]\n'
                NodeData+='ProcesoPromedio'+str(CountProceso)+'->SimboloparentesisA'+str(CountSimboloPa)+'->parentesisA'+str(CountSimboloPa)+'\n'
                CountSimboloPa+=1
                i+=1
                if self.listaTokens[i].lexema == 'ComillaDoble':
                    i+=1
                    if self.listaTokens[i].token == 'cadena':
                        field = self.listaTokens[i].lexema
                        NodosCrear+='Cadena'+str(CountCadena)+'[label="SimboloparentesisA"]\n'
                        NodosCrear+='CadenaText'+str(CountCadena)+'[label="'+field+'"]\n'
                        NodeData+='ProcesoPromedio'+str(CountProceso)+'->Cadena'+str(CountCadena)+'->CadenaText'+str(CountCadena)+'\n'
                        CountCadena+=1
                        i+=1
                        if self.listaTokens[i].lexema == 'ComillaDoble':
                            i+=1
                            if self.listaTokens[i].lexema== 'parentesis2':
                                NodosCrear+='SimboloparentesisC'+str(CountSimboloPa)+'[label="SimboloparentesisC"]\n'
                                NodosCrear+='parentesisC'+str(CountSimboloPa)+'[label=")"]\n'
                                NodeData+='ProcesoPromedio'+str(CountProceso)+'->SimboloparentesisC'+str(CountSimboloPa)+'->parentesisC'+str(CountSimboloPa)+'\n'
                                CountSimboloPa+=1
                                i+=1
                                if self.listaTokens[i].lexema== 'puntoycoma':
                                    NodosCrear+='SimboloPuntoyComa'+str(CountSimboloIgual)+'[label="SimboloPuntoYComa"]\n'
                                    NodosCrear+='puntoYComa'+str(CountSimboloIgual)+'[label=";"]\n'
                                    NodeData+='ProcesoPromedio'+str(CountProceso)+'->SimboloPuntoyComa'+str(CountSimboloIgual)+'->puntoYComa'+str(CountSimboloIgual)+'\n'
                                    CountSimboloIgual+=1
                                    i+=1
                                    for p in range(len(self.listClaves)):
                                        if self.listClaves[p] == field:
                                            posicion = p
                                    promedio = self.sacarPromedio(posicion)
                                    NodosCrear+='PromedioCampo'+str(CountReal)+'[label="'+str(promedio)+'"]\n'
                                    print('el promedio es: '+str(promedio))
                                    NodeData+='Promedio'+str(countToken)+'->PromedioCampo'+str(CountReal)+'\n'
                                    CountReal+=1
                                    countToken+=1
                                    ReturnText+='\n-->'+str(promedio)
                                    contadorImprimir=1
                                else:
                                    e='Error sintactico en fila '+str(self.listaTokens[i].Fila)+' y columna '+str(self.listaTokens[i].Columna)+" revisar"
                                    self.listaErrores.append(Errores(self.listaTokens[i].Fila, self.listaTokens[i].Columna, e, ";"))
                            else:
                                e='Error sintactico en fila '+str(self.listaTokens[i].Fila)+' y columna '+str(self.listaTokens[i].Columna)+" revisar"
                                self.listaErrores.append(Errores(self.listaTokens[i].Fila, self.listaTokens[i].Columna, e, ")"))
                        else:
                            e='Error sintactico en fila '+str(self.listaTokens[i].Fila)+' y columna '+str(self.listaTokens[i].Columna)+" revisar"
                            self.listaErrores.append(Errores(self.listaTokens[i].Fila, self.listaTokens[i].Columna, e, "ComillaDoble"))
                    else:
                        e='Error sintactico en fila '+str(self.listaTokens[i].Fila)+' y columna '+str(self.listaTokens[i].Columna)+" revisar"
                        self.listaErrores.append(Errores(self.listaTokens[i].Fila, self.listaTokens[i].Columna, e, "cadena"))
                else:
                    e='Error sintactico en fila '+str(self.listaTokens[i].Fila)+' y columna '+str(self.listaTokens[i].Columna)+" revisar"
                    self.listaErrores.append(Errores(self.listaTokens[i].Fila, self.listaTokens[i].Columna, e, "ComillaDoble"))
            else:
                e='Error sintactico en fila '+str(self.listaTokens[i].Fila)+' y columna '+str(self.listaTokens[i].Columna)+" revisar"
                self.listaErrores.append(Errores(self.listaTokens[i].Fila, self.listaTokens[i].Columna, e, "("))
        else:
            e='Error sintactico en fila '+str(self.listaTokens[i].Fila)+' y columna '+str(self.listaTokens[i].Columna)+" revisar"
            self.listaErrores.append(Errores(self.listaTokens[i].Fila, self.listaTokens[i].Columna, e, "promedio"))
        CountProceso+=1
    def sacarPromedio(self,posicion):
        summation=0
        totalRegisters=len(self.listRegisters)
        for i in self.listRegisters:
            summation+=float(i[posicion])
        promedio = summation/totalRegisters
        return promedio
    ## termina instrucciones promedio

    def instruccion_Sumar(self):
        global i, ReturnText, contadorImprimir, NodeData, NodosCrear, CountCadena, countToken, CountSimboloPa, CountProceso, CountSimboloIgual
        if self.listaTokens[i].lexema == 'sumar':
            NodosCrear+='tokenSumar'+str(countToken)+'[label="tokenSumar"]\n'
            NodosCrear+='Sumar'+str(countToken)+'[label="Sumar"]\n'
            NodeData+='ProcesoSumar'+str(CountProceso)+'->tokenSumar'+str(countToken)+'->Sumar'+str(countToken)+'\n'
            i+=1
            if self.listaTokens[i].lexema == 'parentesis1':
                NodosCrear+='SimboloparentesisA'+str(CountSimboloPa)+'[label="SimboloparentesisA"]\n'
                NodosCrear+='parentesisA'+str(CountSimboloPa)+'[label="("]\n'
                NodeData+='ProcesoSumar'+str(CountProceso)+'->SimboloparentesisA'+str(CountSimboloPa)+'->parentesisA'+str(CountSimboloPa)+'\n'
                CountSimboloPa+=1
                i+=1
                if self.listaTokens[i].lexema == 'ComillaDoble':
                    i+=1
                    if self.listaTokens[i].token == 'cadena':
                        field = self.listaTokens[i].lexema
                        NodosCrear+='Cadena'+str(CountCadena)+'[label="Cadena"]\n'
                        NodosCrear+='CadenaText'+str(CountCadena)+'[label="'+field+'"]\n'
                        NodeData+='ProcesoSumar'+str(CountProceso)+'->Cadena'+str(CountCadena)+'->CadenaText'+str(CountCadena)+'\n'
                        CountCadena+=1
                        i+=1
                        if self.listaTokens[i].lexema == 'ComillaDoble':
                            i+=1
                            if self.listaTokens[i].lexema== 'parentesis2':
                                NodosCrear+='SimboloparentesisC'+str(CountSimboloPa)+'[label="SimboloparentesisC"]\n'
                                NodosCrear+='parentesisC'+str(CountSimboloPa)+'[label=")"]\n'
                                NodeData+='ProcesoSumar'+str(CountProceso)+'->SimboloparentesisC'+str(CountSimboloPa)+'->parentesisC'+str(CountSimboloPa)+'\n'
                                CountSimboloPa+=1
                                i+=1
                                if self.listaTokens[i].lexema== 'puntoycoma':
                                    NodosCrear+='SimboloPuntoyComa'+str(CountSimboloIgual)+'[label="SimboloPuntoYComa"]\n'
                                    NodosCrear+='puntoYComa'+str(CountSimboloIgual)+'[label=";"]\n'
                                    NodeData+='ProcesoSumar'+str(CountProceso)+'->SimboloPuntoyComa'+str(CountSimboloIgual)+'->puntoYComa'+str(CountSimboloIgual)+'\n'
                                    CountSimboloIgual+=1
                                    i+=1
                                    for p in range(len(self.listClaves)):
                                        if self.listClaves[p] == field:
                                            position = p
                                        
                                    summation = self.Sumar(position)
                                    NodosCrear+='Sumatoria'+str(CountReal)+'[label="'+str(summation)+'"]\n'
                                    print('La sumatoria en '+self.listClaves[position]+' es: '+str(summation))
                                    NodeData+='Sumar'+str(countToken)+'->Sumatoria'+str(CountReal)+'\n'
                                    ReturnText+='\n-->'+str(summation)
                                    contadorImprimir=1
                                else:
                                    e='Error sintactico en fila '+str(self.listaTokens[i].Fila)+' y columna '+str(self.listaTokens[i].Columna)+" revisar"
                                    self.listaErrores.append(Errores(self.listaTokens[i].Fila, self.listaTokens[i].Columna, e, ";"))
                            else:
                                e='Error sintactico en fila '+str(self.listaTokens[i].Fila)+' y columna '+str(self.listaTokens[i].Columna)+" revisar"
                                self.listaErrores.append(Errores(self.listaTokens[i].Fila, self.listaTokens[i].Columna, e, ")"))
                        else:
                            e='Error sintactico en fila '+str(self.listaTokens[i].Fila)+' y columna '+str(self.listaTokens[i].Columna)+" revisar"
                            self.listaErrores.append(Errores(self.listaTokens[i].Fila, self.listaTokens[i].Columna, e, "ComillaDoble"))
                    else:
                        e='Error sintactico en fila '+str(self.listaTokens[i].Fila)+' y columna '+str(self.listaTokens[i].Columna)+" revisar"
                        self.listaErrores.append(Errores(self.listaTokens[i].Fila, self.listaTokens[i].Columna, e, "cadena"))
                else:
                    e='Error sintactico en fila '+str(self.listaTokens[i].Fila)+' y columna '+str(self.listaTokens[i].Columna)+" revisar"
                    self.listaErrores.append(Errores(self.listaTokens[i].Fila, self.listaTokens[i].Columna, e, "ComillaDoble"))
            else:
                e='Error sintactico en fila '+str(self.listaTokens[i].Fila)+' y columna '+str(self.listaTokens[i].Columna)+" revisar"
                self.listaErrores.append(Errores(self.listaTokens[i].Fila, self.listaTokens[i].Columna, e, "("))
        else:
            e='Error sintactico en fila '+str(self.listaTokens[i].Fila)+' y columna '+str(self.listaTokens[i].Columna)+" revisar"
            self.listaErrores.append(Errores(self.listaTokens[i].Fila, self.listaTokens[i].Columna, e, "sumar"))
        countToken+=1
        CountProceso+=1
    def Sumar(self, position):
        summation=0
        for i in self.listRegisters:
            summation+=float(i[position])
        return summation

    def instruccion_Contarsi(self):
        global i, ReturnText, contadorImprimir,CountComa, NodosCrear, NodeData, CountSimboloPa, CountCadena, CountSimboloIgual, CountReal, CountProceso, countToken
        if self.listaTokens[i].lexema == 'contarsi':
            i+=1
            NodosCrear+='tokenContarSi'+str(countToken)+'[label="tokenContarSi"]\n'
            NodosCrear+='ContarSi'+str(countToken)+'[label="ContarSi"]\n'
            NodeData+='ProcesoContarSi'+str(CountProceso)+'->tokenContarSi'+str(countToken)+'->ContarSi'+str(countToken)+'\n'
            if self.listaTokens[i].lexema == 'parentesis1':
                i+=1
                NodosCrear+='SimboloparentesisA'+str(CountSimboloPa)+'[label="SimboloparentesisA"]\n'
                NodosCrear+='parentesisA'+str(CountSimboloPa)+'[label="("]\n'
                NodeData+='ProcesoContarSi'+str(CountProceso)+'->SimboloparentesisA'+str(CountSimboloPa)+'->parentesisA'+str(CountSimboloPa)+'\n'
                CountSimboloPa+=1
                if self.listaTokens[i].lexema == 'ComillaDoble':
                    i+=1
                    if self.listaTokens[i].token == 'cadena':
                        field = self.listaTokens[i].lexema
                        NodosCrear+='Cadena'+str(CountCadena)+'[label="Cadena"]\n'
                        NodosCrear+='CadenaText'+str(CountCadena)+'[label="'+field+'"]\n'
                        NodeData+='ProcesoContarSi'+str(CountProceso)+'->Cadena'+str(CountCadena)+'->CadenaText'+str(CountCadena)+'\n'
                        CountCadena+=1
                        i+=1
                        if self.listaTokens[i].lexema == 'ComillaDoble':
                            i+=1
                            if self.listaTokens[i].lexema== 'coma':
                                i+=1
                                NodosCrear+='SimboloComa'+str(CountComa)+'[label="SimboloComa"]\n'
                                NodosCrear+='Coma'+str(CountComa)+'[label=","]\n'
                                NodeData+='ProcesoContarSi'+str(CountProceso)+'->SimboloComa'+str(CountComa)+'->Coma'+str(CountComa)+'\n'
                                CountComa+=1
                                if self.listaTokens[i].token== 'entero':
                                    value = self.listaTokens[i].lexema
                                    i+=1
                                    if self.listaTokens[i].lexema== 'parentesis2':
                                        i+=1
                                        NodosCrear+='SimboloparentesisC'+str(CountSimboloPa)+'[label="SimboloparentesisC"]\n'
                                        NodosCrear+='parentesisC'+str(CountSimboloPa)+'[label=")"]\n'
                                        NodeData+='ProcesoContarSi'+str(CountProceso)+'->SimboloparentesisC'+str(CountSimboloPa)+'->parentesisC'+str(CountSimboloPa)+'\n'
                                        CountSimboloPa+=1
                                        if self.listaTokens[i].lexema== 'puntoycoma':
                                            i+=1
                                            NodosCrear+='SimboloPuntoyComa'+str(CountSimboloIgual)+'[label="SimboloPuntoYComa"]\n'
                                            NodosCrear+='puntoYComa'+str(CountSimboloIgual)+'[label=";"]\n'
                                            NodeData+='ProcesoContarSi'+str(CountProceso)+'->SimboloPuntoyComa'+str(CountSimboloIgual)+'->puntoYComa'+str(CountSimboloIgual)+'\n'
                                            CountSimboloIgual+=1
                                            for p in range(len(self.listClaves)):
                                                if self.listClaves[p] == field:
                                                    position = p
                                                    ValueCount = self.ejec_ContarSi(position, value)
                                                    print('cantidad de valores con el valor '+str(value)+'son: '+str(ValueCount)) 
                                                    ReturnText+='\n-->'+str(ValueCount)
                                                    contadorImprimir=1
                                        else:
                                            e='Error sintactico en fila '+str(self.listaTokens[i].Fila)+' y columna '+str(self.listaTokens[i].Columna)+" revisar"
                                            self.listaErrores.append(Errores(self.listaTokens[i].Fila, self.listaTokens[i].Columna, e, ";"))
                                    else:
                                        e='Error sintactico en fila '+str(self.listaTokens[i].Fila)+' y columna '+str(self.listaTokens[i].Columna)+" revisar"
                                        self.listaErrores.append(Errores(self.listaTokens[i].Fila, self.listaTokens[i].Columna, e, ")"))
                                else:
                                    e='Error sintactico en fila '+str(self.listaTokens[i].Fila)+' y columna '+str(self.listaTokens[i].Columna)+" revisar"
                                    self.listaErrores.append(Errores(self.listaTokens[i].Fila, self.listaTokens[i].Columna, e, "entero"))
                            else:
                                e='Error sintactico en fila '+str(self.listaTokens[i].Fila)+' y columna '+str(self.listaTokens[i].Columna)+" revisar"
                                self.listaErrores.append(Errores(self.listaTokens[i].Fila, self.listaTokens[i].Columna, e, ","))
                        else:
                            e='Error sintactico en fila '+str(self.listaTokens[i].Fila)+' y columna '+str(self.listaTokens[i].Columna)+" revisar"
                            self.listaErrores.append(Errores(self.listaTokens[i].Fila, self.listaTokens[i].Columna, e, "ComillaDoble"))
                    else:
                        e='Error sintactico en fila '+str(self.listaTokens[i].Fila)+' y columna '+str(self.listaTokens[i].Columna)+" revisar"
                        self.listaErrores.append(Errores(self.listaTokens[i].Fila, self.listaTokens[i].Columna, e, "cadena"))
                else:
                    e='Error sintactico en fila '+str(self.listaTokens[i].Fila)+' y columna '+str(self.listaTokens[i].Columna)+" revisar"
                    self.listaErrores.append(Errores(self.listaTokens[i].Fila, self.listaTokens[i].Columna, e, "ComillaDoble"))
            else:
                e='Error sintactico en fila '+str(self.listaTokens[i].Fila)+' y columna '+str(self.listaTokens[i].Columna)+" revisar"
                self.listaErrores.append(Errores(self.listaTokens[i].Fila, self.listaTokens[i].Columna, e, "("))
        else:
            e='Error sintactico en fila '+str(self.listaTokens[i].Fila)+' y columna '+str(self.listaTokens[i].Columna)+" revisar"
            self.listaErrores.append(Errores(self.listaTokens[i].Fila, self.listaTokens[i].Columna, e, "contarsi"))
            countToken+=1
            CountProceso+=1
    def ejec_ContarSi(self, position, value):
        summation=0
        for i in self.listRegisters:
            if i[position] == value:
                summation+=1
        return summation
    
    def instruccion_Datos(self):
        global i, ReturnText, contadorImprimir, NodeData, NodosCrear, countToken, CountSimboloPa, CountSimboloIgual, CountProceso
        
        if self.listaTokens[i].lexema == 'datos':
            NodosCrear+='tokenDatos'+str(countToken)+'[label="tokenDatos"]\n'
            NodosCrear+='Datos'+str(countToken)+'[label="Datos"]\n'
            NodeData+='ProcesoDatos'+str(CountProceso)+'->tokenDatos'+str(countToken)+'->Datos'+str(countToken)+'\n'
            i+=1
            if self.listaTokens[i].lexema == 'parentesis1':
                NodosCrear+='SimboloparentesisA'+str(CountSimboloPa)+'[label="SimboloparentesisA"]\n'
                NodosCrear+='parentesisA'+str(CountSimboloPa)+'[label="("]\n'
                NodeData+='ProcesoDatos'+str(CountProceso)+'->SimboloparentesisA'+str(CountSimboloPa)+'->parentesisA'+str(CountSimboloPa)+'\n'
                CountSimboloPa+=1
                i+=1 
                if self.listaTokens[i].lexema== 'parentesis2':
                    NodosCrear+='SimboloparentesisC'+str(CountSimboloPa)+'[label="SimboloparentesisC"]\n'
                    NodosCrear+='parentesisC'+str(CountSimboloPa)+'[label=")"]\n'
                    NodeData+='ProcesoDatos'+str(CountProceso)+'->SimboloparentesisC'+str(CountSimboloPa)+'->parentesisC'+str(CountSimboloPa)+'\n'
                    CountSimboloPa+=1
                    i+=1
                    if self.listaTokens[i].lexema== 'puntoycoma':
                        NodosCrear+='SimboloPuntoyComa'+str(CountSimboloIgual)+'[label="SimboloPuntoYComa"]\n'
                        NodosCrear+='puntoYComa'+str(CountSimboloIgual)+'[label=";"]\n'
                        NodeData+='ProcesoDatos'+str(CountProceso)+'->SimboloPuntoyComa'+str(CountSimboloIgual)+'->puntoYComa'+str(CountSimboloIgual)+'\n'
                        CountSimboloIgual+=1
                        i+=1
                        datos=self.impDatos()
                        print(datos)
                        ReturnText+='\n-->\n'+str(datos)+'\n'
                        contadorImprimir=1
                    else:
                        e='Error sintactico en fila '+str(self.listaTokens[i].Fila)+' y columna '+str(self.listaTokens[i].Columna)+" revisar"
                        self.listaErrores.append(Errores(self.listaTokens[i].Fila, self.listaTokens[i].Columna, e, ";"))
                else:
                    e='Error sintactico en fila '+str(self.listaTokens[i].Fila)+' y columna '+str(self.listaTokens[i].Columna)+" revisar"
                    self.listaErrores.append(Errores(self.listaTokens[i].Fila, self.listaTokens[i].Columna, e, ")"))
            else:
                e='Error sintactico en fila '+str(self.listaTokens[i].Fila)+' y columna '+str(self.listaTokens[i].Columna)+" revisar"
                self.listaErrores.append(Errores(self.listaTokens[i].Fila, self.listaTokens[i].Columna, e, "("))
        else:
            e='Error sintactico en fila '+str(self.listaTokens[i].Fila)+' y columna '+str(self.listaTokens[i].Columna)+" revisar"
            self.listaErrores.append(Errores(self.listaTokens[i].Fila, self.listaTokens[i].Columna, e, "datos"))
        countToken+=1
        CountProceso+=1                       
    def impDatos(self):
        a = PrettyTable()
        a.field_names = self.listClaves
        for i in self.listRegisters:
            a.add_row(i)
        return a   
    
    def instruccion_max(self):
        global i, ReturnText, contadorImprimir, NodosCrear, NodeData, CountSimboloIgual, CountCadena, CountSimboloPa, countToken, CountProceso
        if self.listaTokens[i].lexema == 'max':
            i+=1
            NodosCrear+='tokenMax'+str(countToken)+'[label="tokenMax"]\n'
            NodosCrear+='Max'+str(countToken)+'[label="Max"]\n'
            NodeData+='ProcesoMax'+str(CountProceso)+'->tokenMax'+str(countToken)+'->Max'+str(countToken)+'\n'
            if self.listaTokens[i].lexema == 'parentesis1':
                i+=1
                NodosCrear+='SimboloparentesisA'+str(CountSimboloPa)+'[label="SimboloparentesisA"]\n'
                NodosCrear+='parentesisA'+str(CountSimboloPa)+'[label="("]\n'
                NodeData+='ProcesoMax'+str(CountProceso)+'->SimboloparentesisA'+str(CountSimboloPa)+'->parentesisA'+str(CountSimboloPa)+'\n'
                CountSimboloPa+=1
                if self.listaTokens[i].lexema == 'ComillaDoble':
                    i+=1
                    if self.listaTokens[i].token == 'cadena':
                        field = self.listaTokens[i].lexema
                        NodosCrear+='Cadena'+str(CountCadena)+'[label="Cadena"]\n'
                        NodosCrear+='CadenaText'+str(CountCadena)+'[label="'+field+'"]\n'
                        NodeData+='ProcesoMax'+str(CountProceso)+'->Cadena'+str(CountCadena)+'->CadenaText'+str(CountCadena)+'\n'
                        CountCadena+=1
                        i+=1
                        if self.listaTokens[i].lexema == 'ComillaDoble':
                            i+=1
                            if self.listaTokens[i].lexema== 'parentesis2':
                                i+=1
                                NodosCrear+='SimboloparentesisC'+str(CountSimboloPa)+'[label="SimboloparentesisC"]\n'
                                NodosCrear+='parentesisC'+str(CountSimboloPa)+'[label=")"]\n'
                                NodeData+='ProcesoMax'+str(CountProceso)+'->SimboloparentesisC'+str(CountSimboloPa)+'->parentesisC'+str(CountSimboloPa)+'\n'
                                CountSimboloPa+=1
                                if self.listaTokens[i].lexema== 'puntoycoma':
                                    i+=1
                                    NodosCrear+='SimboloPuntoyComa'+str(CountSimboloIgual)+'[label="SimboloPuntoYComa"]\n'
                                    NodosCrear+='puntoYComa'+str(CountSimboloIgual)+'[label=";"]\n'
                                    NodeData+='ProcesoMax'+str(CountProceso)+'->SimboloPuntoyComa'+str(CountSimboloIgual)+'->puntoYComa'+str(CountSimboloIgual)+'\n'
                                    CountSimboloIgual+=1
                                    for p in range(len(self.listClaves)):
                                        if self.listClaves[p] == field:
                                            position = p
                                            ValueMax =self.ValueMax(position)
                                            print('valor maximo en '+field+" es: "+ str(ValueMax))
                                            ReturnText+='\n-->'+str(ValueMax)
                                            contadorImprimir=1
                                else:
                                    e='Error sintactico en fila '+str(self.listaTokens[i].Fila)+' y columna '+str(self.listaTokens[i].Columna)+" revisar"
                                    self.listaErrores.append(Errores(self.listaTokens[i].Fila, self.listaTokens[i].Columna, e, ";"))
                            else:
                                e='Error sintactico en fila '+str(self.listaTokens[i].Fila)+' y columna '+str(self.listaTokens[i].Columna)+" revisar"
                                self.listaErrores.append(Errores(self.listaTokens[i].Fila, self.listaTokens[i].Columna, e, ")"))
                        else:
                            e='Error sintactico en fila '+str(self.listaTokens[i].Fila)+' y columna '+str(self.listaTokens[i].Columna)+" revisar"
                            self.listaErrores.append(Errores(self.listaTokens[i].Fila, self.listaTokens[i].Columna, e, "ComillaDoble"))
                    else:
                        e='Error sintactico en fila '+str(self.listaTokens[i].Fila)+' y columna '+str(self.listaTokens[i].Columna)+" revisar"
                        self.listaErrores.append(Errores(self.listaTokens[i].Fila, self.listaTokens[i].Columna, e, "cadena"))
                else:
                    e='Error sintactico en fila '+str(self.listaTokens[i].Fila)+' y columna '+str(self.listaTokens[i].Columna)+" revisar"
                    self.listaErrores.append(Errores(self.listaTokens[i].Fila, self.listaTokens[i].Columna, e, "ComillaDoble"))
            else:
                e='Error sintactico en fila '+str(self.listaTokens[i].Fila)+' y columna '+str(self.listaTokens[i].Columna)+" revisar"
                self.listaErrores.append(Errores(self.listaTokens[i].Fila, self.listaTokens[i].Columna, e, "("))
        else:
            e='Error sintactico en fila '+str(self.listaTokens[i].Fila)+' y columna '+str(self.listaTokens[i].Columna)+" revisar"
            self.listaErrores.append(Errores(self.listaTokens[i].Fila, self.listaTokens[i].Columna, e, "max"))
        countToken+=1
        CountProceso+=1
    def ValueMax(self, position):
        Vmax = 0
        for i in self.listRegisters:
            Vtemp = i[position]
            if float(Vtemp)>Vmax:
                Vmax = float(Vtemp)
        return Vmax

    def instruccion_min(self):
        global i, ReturnText, contadorImprimir, NodosCrear, NodeData, CountSimboloIgual, CountCadena, CountSimboloPa, countToken, CountProceso
        if self.listaTokens[i].lexema == 'min':
            i+=1
            NodosCrear+='tokenMin'+str(countToken)+'[label="tokenMin"]\n'
            NodosCrear+='Min'+str(countToken)+'[label="Min"]\n'
            NodeData+='ProcesoMin'+str(CountProceso)+'->tokenMin'+str(countToken)+'->Min'+str(countToken)+'\n'
            if self.listaTokens[i].lexema == 'parentesis1':
                i+=1
                NodosCrear+='SimboloparentesisA'+str(CountSimboloPa)+'[label="SimboloparentesisA"]\n'
                NodosCrear+='parentesisA'+str(CountSimboloPa)+'[label="("]\n'
                NodeData+='ProcesoMin'+str(CountProceso)+'->SimboloparentesisA'+str(CountSimboloPa)+'->parentesisA'+str(CountSimboloPa)+'\n'
                CountSimboloPa+=1
                if self.listaTokens[i].lexema == 'ComillaDoble':
                    i+=1
                    if self.listaTokens[i].token == 'cadena':
                        field = self.listaTokens[i].lexema
                        NodosCrear+='Cadena'+str(CountCadena)+'[label="Cadena"]\n'
                        NodosCrear+='CadenaText'+str(CountCadena)+'[label="'+field+'"]\n'
                        NodeData+='ProcesoMin'+str(CountProceso)+'->Cadena'+str(CountCadena)+'->CadenaText'+str(CountCadena)+'\n'
                        CountCadena+=1
                        i+=1
                        if self.listaTokens[i].lexema == 'ComillaDoble':
                            i+=1
                            if self.listaTokens[i].lexema== 'parentesis2':
                                i+=1
                                NodosCrear+='SimboloparentesisC'+str(CountSimboloPa)+'[label="SimboloparentesisC"]\n'
                                NodosCrear+='parentesisC'+str(CountSimboloPa)+'[label=")"]\n'
                                NodeData+='ProcesoMin'+str(CountProceso)+'->SimboloparentesisC'+str(CountSimboloPa)+'->parentesisC'+str(CountSimboloPa)+'\n'
                                CountSimboloPa+=1
                                if self.listaTokens[i].lexema== 'puntoycoma':
                                    i+=1
                                    NodosCrear+='SimboloPuntoyComa'+str(CountSimboloIgual)+'[label="SimboloPuntoYComa"]\n'
                                    NodosCrear+='puntoYComa'+str(CountSimboloIgual)+'[label=";"]\n'
                                    NodeData+='ProcesoMin'+str(CountProceso)+'->SimboloPuntoyComa'+str(CountSimboloIgual)+'->puntoYComa'+str(CountSimboloIgual)+'\n'
                                    CountSimboloIgual+=1
                                    for p in range(len(self.listClaves)):
                                        if self.listClaves[p] == field:
                                            position = p
                                            ValueMin =self.ValueMin(position)
                                            print('valor minimo en '+field+" es: "+ str(ValueMin))
                                            ReturnText+='\n-->'+str(ValueMin)
                                            contadorImprimir=1
                                else:
                                    e='Error sintactico en fila '+str(self.listaTokens[i].Fila)+' y columna '+str(self.listaTokens[i].Columna)+" revisar"
                                    self.listaErrores.append(Errores(self.listaTokens[i].Fila, self.listaTokens[i].Columna, e, ";"))
                            else:
                                e='Error sintactico en fila '+str(self.listaTokens[i].Fila)+' y columna '+str(self.listaTokens[i].Columna)+" revisar"
                                self.listaErrores.append(Errores(self.listaTokens[i].Fila, self.listaTokens[i].Columna, e, ")"))
                        else:
                            e='Error sintactico en fila '+str(self.listaTokens[i].Fila)+' y columna '+str(self.listaTokens[i].Columna)+" revisar"
                            self.listaErrores.append(Errores(self.listaTokens[i].Fila, self.listaTokens[i].Columna, e, "ComillaDoble"))
                    else:
                        e='Error sintactico en fila '+str(self.listaTokens[i].Fila)+' y columna '+str(self.listaTokens[i].Columna)+" revisar"
                        self.listaErrores.append(Errores(self.listaTokens[i].Fila, self.listaTokens[i].Columna, e, "cadena"))
                else:
                    e='Error sintactico en fila '+str(self.listaTokens[i].Fila)+' y columna '+str(self.listaTokens[i].Columna)+" revisar"
                    self.listaErrores.append(Errores(self.listaTokens[i].Fila, self.listaTokens[i].Columna, e, "ComillaDoble"))
            else:
                e='Error sintactico en fila '+str(self.listaTokens[i].Fila)+' y columna '+str(self.listaTokens[i].Columna)+" revisar"
                self.listaErrores.append(Errores(self.listaTokens[i].Fila, self.listaTokens[i].Columna, e, "("))
        else:
            e='Error sintactico en fila '+str(self.listaTokens[i].Fila)+' y columna '+str(self.listaTokens[i].Columna)+" revisar"
            self.listaErrores.append(Errores(self.listaTokens[i].Fila, self.listaTokens[i].Columna, e, "min"))
        countToken+=1
        CountProceso+=1
    def ValueMin(self, position):
        Vmin = self.ValueMax(position)
        
        for i in self.listRegisters:
            if float(i[position])<Vmin:
                Vmin = float(i[position])
        return Vmin
    
    def instruccion_Exportar(self):
        global i, ReturnText, contadorImprimir, NodosCrear, NodeData, CountSimboloIgual, CountCadena, CountSimboloPa, countToken, CountProceso
        if self.listaTokens[i].lexema == 'exportar':
            i+=1
            NodosCrear+='tokenExportar'+str(countToken)+'[label="tokenExportar"]\n'
            NodosCrear+='Exportar'+str(countToken)+'[label="Exportar"]\n'
            NodeData+='ProcesoExportar'+str(CountProceso)+'->tokenExportar'+str(countToken)+'->Exportar'+str(countToken)+'\n'
            if self.listaTokens[i].lexema == 'parentesis1':
                i+=1
                NodosCrear+='SimboloparentesisA'+str(CountSimboloPa)+'[label="SimboloparentesisA"]\n'
                NodosCrear+='parentesisA'+str(CountSimboloPa)+'[label="("]\n'
                NodeData+='ProcesoExportar'+str(CountProceso)+'->SimboloparentesisA'+str(CountSimboloPa)+'->parentesisA'+str(CountSimboloPa)+'\n'
                CountSimboloPa+=1
                if self.listaTokens[i].lexema == 'ComillaDoble':
                    i+=1
                    if self.listaTokens[i].token == 'cadena':
                        titulo = self.listaTokens[i].lexema
                        NodosCrear+='Cadena'+str(CountCadena)+'[label="SimboloparentesisA"]\n'
                        NodosCrear+='CadenaText'+str(CountCadena)+'[label="'+titulo+'"]\n'
                        NodeData+='ProcesoExportar'+str(CountProceso)+'->Cadena'+str(CountCadena)+'->CadenaText'+str(CountCadena)+'\n'
                        CountCadena+=1
                        i+=1
                        if self.listaTokens[i].lexema == 'ComillaDoble':
                            i+=1
                            if self.listaTokens[i].lexema== 'parentesis2':
                                i+=1
                                NodosCrear+='SimboloparentesisC'+str(CountSimboloPa)+'[label="SimboloparentesisC"]\n'
                                NodosCrear+='parentesisC'+str(CountSimboloPa)+'[label=")"]\n'
                                NodeData+='ProcesoExportar'+str(CountProceso)+'->SimboloparentesisC'+str(CountSimboloPa)+'->parentesisC'+str(CountSimboloPa)+'\n'
                                CountSimboloPa+=1
                                if self.listaTokens[i].lexema== 'puntoycoma':
                                    i+=1
                                    NodosCrear+='SimboloPuntoyComa'+str(CountSimboloIgual)+'[label="SimboloPuntoYComa"]\n'
                                    NodosCrear+='puntoYComa'+str(CountSimboloIgual)+'[label=";"]\n'
                                    NodeData+='ProcesoExportar'+str(CountProceso)+'->SimboloPuntoyComa'+str(CountSimboloIgual)+'->puntoYComa'+str(CountSimboloIgual)+'\n'
                                    CountSimboloIgual+=1
                                    self.generarReporteHtml(titulo)
                                    ReturnText+='\n-->Revisar Reporte'
                                    contadorImprimir=1
                                    countToken+=1
                                else:
                                    e='Error sintactico en fila '+str(self.listaTokens[i].Fila)+' y columna '+str(self.listaTokens[i].Columna)+" revisar"
                                    self.listaErrores.append(Errores(self.listaTokens[i].Fila, self.listaTokens[i].Columna, e, ";"))
                            else:
                                e='Error sintactico en fila '+str(self.listaTokens[i].Fila)+' y columna '+str(self.listaTokens[i].Columna)+" revisar"
                                self.listaErrores.append(Errores(self.listaTokens[i].Fila, self.listaTokens[i].Columna, e, ")"))
                        else:
                            e='Error sintactico en fila '+str(self.listaTokens[i].Fila)+' y columna '+str(self.listaTokens[i].Columna)+" revisar"
                            self.listaErrores.append(Errores(self.listaTokens[i].Fila, self.listaTokens[i].Columna, e, "ComillaDoble"))
                    else:
                        e='Error sintactico en fila '+str(self.listaTokens[i].Fila)+' y columna '+str(self.listaTokens[i].Columna)+" revisar"
                        self.listaErrores.append(Errores(self.listaTokens[i].Fila, self.listaTokens[i].Columna, e, "cadena"))
                else:
                    e='Error sintactico en fila '+str(self.listaTokens[i].Fila)+' y columna '+str(self.listaTokens[i].Columna)+" revisar"
                    self.listaErrores.append(Errores(self.listaTokens[i].Fila, self.listaTokens[i].Columna, e, "ComillaDoble"))
            else:
                e='Error sintactico en fila '+str(self.listaTokens[i].Fila)+' y columna '+str(self.listaTokens[i].Columna)+" revisar"
                self.listaErrores.append(Errores(self.listaTokens[i].Fila, self.listaTokens[i].Columna, e, "("))
        else:
            e='Error sintactico en fila '+str(self.listaTokens[i].Fila)+' y columna '+str(self.listaTokens[i].Columna)+" revisar"
            self.listaErrores.append(Errores(self.listaTokens[i].Fila, self.listaTokens[i].Columna, e, "promedio"))
        CountProceso+=1
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

    def ArbolDeDerivacion(self):
        global NodeData, NodosCrear
        f = open('ArchivosDots/archivoArbolDerivacion.dot', 'w', encoding='utf-8')
        edgeData=''
        graph=''

        contenidoDot=(
            'digraph Arbol{\n'
            '{\n'
            'node [margin=0 fontsize=20 width=0.5 style=filleed]\n'
            +NodosCrear+
            '}'
            +NodeData+'}'
        )


        f.write(contenidoDot)
        f.close()
        os.system("dot -Tpdf ArchivosDots/archivoArbolDerivacion.dot -o ./Reportes/Arbol_De_Derivacion.pdf")
        webbrowser.open("file:///"+os.getcwd()+"/Reportes/Arbol_De_Derivacion.pdf")

