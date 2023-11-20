#-Import-----------------------------------
from pprint import pprint
#-Import-----------------------------------


LineaXLinea=[]
with open('codet1.txt', encoding='utf-8') as file:
        content2 = file.readlines()
LineaXLinea=[]
for i in content2:
    i=i.strip()
    LineaXLinea.append(i)

dict_ERRORES = {
    0: 'valor de retorno invalido(no existe la variable en el diccionario)',
    1: 'asignacion de valor invalida hacia una variable', 
    2: 'comparacion invalida de tipo de variable en condicional ',
    3: 'valor de retorno invalido(El tipo de retorno no coincide con el tipo de la funcion)',
    4: 'asignacion de valor invalida hacia una variable Global', 
    5: 'variable no decalrda' 
}
#---------------------------------Error Class----------------------------------------------
class Error:
    def __init__(self, nul='', er=-1):
        self.nl=nul
        self.codeError = er
    def get_string2lookUP(self):
        return self.nl
    def get_codeError(self):
        return self.codeError
    def toString(self):
        error_type = dict_ERRORES.get(self.codeError, "that error code is not in dict_ERRORES")
        print(f"ERROR: Linea: #{str(self.nl)} Tipo de Error: [{error_type}]")
#---------------------------------Error Class----------------------------------------------
def verificar_congruencia_de_tipo(tipo,linea):
    if linea!='':
        if(tipo=='float'):
            try:
                sera_float_value = float(linea)
            except ValueError:
                list_de_errores.append(Error(numeroLinea[0],4))
        elif(tipo=='int'):
            if(linea.isdecimal()!=True):
                list_de_errores.append(Error(numeroLinea[0],4))
        else:
            single_quotes = ''+linea+''
            if '\"' in single_quotes:
                None
            else:
                list_de_errores.append(Error(numeroLinea[0],4))

    #nota: how can I get the dict value with out a KeyError: 
    #like so...
print("-----------------------------------Lista para saber el # de linea---------------------------------------")
pprint(LineaXLinea)
print("--------------------------------------------------------------------------------------------------------")
dict_code={}
Fun_key=''
InFUN=False
nL=1
tipoFun=''
for j in LineaXLinea:
    #function key = Fun_key
    # if the varible 'INFUN'==Treu we are in a function so we will add values to... 
    # to the 'dict_code={}' like this= 'dict_code[Fun_key]['inner_dictKYE']=value
    if(InFUN==True):
        #in the dict of the function in the dict 'dict_code={}'
        #(while)----------------------------------------------------
        if(j.find('while')!=-1 ):
            posi = j.find('{')
            if posi != -1:
                valores = j[:posi].removeprefix('{')
                posi = valores.find('(')
            if posi != -1:
                valores = valores[posi:].removeprefix('(')
                posi = valores.find(')')
            if posi != -1:
                valores = valores[:posi].removeprefix(')')

            if(valores.find('==')!=-1 ):#case ==
                posi = valores.find('==')
                izq=valores[:posi].strip()
                der=valores[posi:].removeprefix('==').strip()
                dict_code[Fun_key]['while']=str(nL)+"#"+izq+'_'+der 
            elif( valores.find('>')!=-1):#case >
                posi = valores.find('>')
                izq=valores[:posi].strip()
                der=valores[posi:].removeprefix('>').strip()
                dict_code[Fun_key]['while']=str(nL)+"#"+izq+'_'+der 
            elif( valores.find('<')!=-1 ):#case <
                posi = valores.find('<')
                izq=valores[:posi].strip()
                der=valores[posi:].removeprefix('<').strip()
                dict_code[Fun_key]['while']=str(nL)+"#"+izq+'_'+der 
            elif( valores.find('<=')!=-1 ):#case <=
                posi = valores.find('<=')
                izq=valores[:posi].strip()
                der=valores[posi:].removeprefix('<=').strip()
                dict_code[Fun_key]['while']=str(nL)+"#"+izq+'_'+der 
            else:                          #case >= 
                posi = valores.find('>=')
                izq=valores[:posi].strip()
                der=valores[posi:].removeprefix('>=').strip()
                dict_code[Fun_key]['while']=str(nL)+"#"+izq+'_'+der
        #(while)----------------------------------------------------
        #(if)-------------------------------------------------------
        if(j.find('if')!=-1 ):
            posi = j.find('{')
            if posi != -1:
                valores = j[:posi].removeprefix('{')
                posi = valores.find('(')
            if posi != -1:
                valores = valores[posi:].removeprefix('(')
                posi = valores.find(')')
            if posi != -1:
                valores = valores[:posi].removeprefix(')')

            if(valores.find('==')!=-1 ):#case ==
                posi = valores.find('==')
                izq=valores[:posi].strip()
                der=valores[posi:].removeprefix('==').strip()
                dict_code[Fun_key]['if']=str(nL)+"#"+izq+'_'+der 
            elif( valores.find('>')!=-1):#case >
                posi = valores.find('>')
                izq=valores[:posi].strip()
                der=valores[posi:].removeprefix('>').strip()
                dict_code[Fun_key]['if']=str(nL)+"#"+izq+'_'+der 
            elif( valores.find('<')!=-1 ):#case <
                posi = valores.find('<')
                izq=valores[:posi].strip()
                der=valores[posi:].removeprefix('<').strip()
                dict_code[Fun_key]['if']=str(nL)+"#"+izq+'_'+der 
            elif( valores.find('<=')!=-1 ):#case <=
                posi = valores.find('<=')
                izq=valores[:posi].strip()
                der=valores[posi:].removeprefix('<=').strip()
                dict_code[Fun_key]['if']=str(nL)+"#"+izq+'_'+der 
            else:                          #case >= 
                posi = valores.find('>=')
                izq=valores[:posi].strip()
                der=valores[posi:].removeprefix('>=').strip()
                dict_code[Fun_key]['if']=str(nL)+"#"+izq+'_'+der
        #(if)----------------------------------------------------------
        #return-----------------------------------------------------------------------------------------------
        if (j.find('return')!=-1):
            posi=j.find('return')
            despues_de_char=j[posi:].removeprefix('return')
            despues_de_char=despues_de_char.strip() 
            dict_code[Fun_key]['return']=str(nL)+"#"+despues_de_char.strip()# Key's in a dict must be unique
        #return----------------------------------------------------------------------------------------------
        #variables decalradas dentro de la funcion-----------------------------------------------------------
        if (j.find('int')!=-1 or j.find('float')!=-1 or j.find('string')!=-1):
            if (j.find('=')!=-1):
                posi=j.find('=')
                valor=j[posi:]
                j=j[:posi]
                j=j.removeprefix('=')
                j=j.split(' ')
                dict_code[Fun_key][j[1]]=str(nL)+"#"+j[0]+"_"+valor.removeprefix('=')
            else:
                j=j.split(' ')
                dict_code[j[1]]=str(nL)+"#"+j[0]
        #variables decalradas dentro de la funcion-----------------------------------------------------------
        # Operator of assigning value '=' y 'return' in the function
        elif (j.find('=')!=-1):
            posi=j.find('=') 
            antes_de_char=j[:posi]
            despues_de_char=j[posi:].removeprefix('=')
            despues_de_char=despues_de_char.strip() 
            dict_code[Fun_key][despues_de_char.strip()]=str(nL)+"#"+j[:posi].strip()# Key's in a dict must be unique 


    # Note: the next 'if' will only check for a function because...
    # because we will never going to find the key word='if' out of a function     
    # (function)-------------------------------------------------------
    if(InFUN==False):            
        if(j.find(')')!=-1 or j.find('(')!=-1):
            InFUN=True
            #adding return value:
            posi=j.find(' ')
            #Function key
            Fun_key=str(nL)+"#"+j[:posi].strip()
            tipoFun=j[:posi].strip()
            print(tipoFun)
            dict_code[Fun_key]={}#DONE whith the return value, adding a new inner dictionary
            #adding varibles to the new inner dictionary:
            posi = j.find('{')
            if posi != -1:
                variables = j[:posi].removeprefix('{')
                posi = variables.find('(')
            if posi != -1:
                variables = variables[posi:].removeprefix('(')
                posi = variables.find(')')
            if posi != -1:
                variables = variables[:posi].removeprefix(')')
                posi=variables.find(',')
            if posi != -1:
                vec01=variables.split(',')
                one=vec01[0]
                two=vec01[1]
                one=one.strip()
                two=two.strip()
                one=one.split(' ')
                two=two.split(' ')
                dict_code[Fun_key][two[1]]=str(nL)+"#"+two[0]
                dict_code[Fun_key][one[1]]=str(nL)+"#"+one[0]
        # (function)-------------------------------------------------------  


            
         
    #(if) 4 global varibles
    if(InFUN==False):
        if (j.find('int')!=-1 or j.find('float')!=-1 or j.find('string')!=-1):
            if (j.find('=')!=-1):
                posi=j.find('=') 
                valor=j[posi:]   #int x=40
                j=j[:posi]
                j=j.removeprefix('=')
                j=j.split(' ')
                dict_code[j[1]]=str(nL)+"#"+j[0]+"_"+valor.removeprefix('=')
            else:
                 j=j.split(' ')
                 dict_code[j[1]]=str(nL)+"#"+j[0]
                

            
    nL=nL+1
#for para leer errors   
list_de_errores=[]
for j in dict_code:
    if (j.find('int')!=-1 or j.find('string')!=-1 or j.find('float')!=-1 or j.find('void')!=-1):
        numLF=j.split('#')
        for fj in dict_code[j]:#vaya iterando por todas las llaves del dict interno
            if(fj=="if" or fj=="while"):
                """
                Caso de que la linea encuetre un "if" o "while"

                Atributos:
                numeroLinea = Lista que guarda el número de línea y sus parametros
                aux = Lista que guarda los parametros de la función
                c1UNO = Variable que guarda el valor de la la variable si es global, en caso de no ser, guarda None
                c2DOS = Variable que guarda el valor de la la variable si es global, en caso de no ser, guarda None
                c3TRES = Variable que guarda el valor de la la variable si es local, en caso de no ser, guarda None
                c4CUATRO = Variable que guarda el valor de la la variable si es local, en caso de no ser, guarda None

                Los if y elif que se desarrollan más adelante son la lógica que se implementó según el tipo de la variable (global o local) y sus combinaciones.

                """

                numeroLinea=dict_code[j][fj].split("#")

                aux=numeroLinea[1].split("_")

                c1UNO=dict_code.get(aux[0],None)
                c2DOS=dict_code.get(aux[1],None)
                c3TRES=dict_code[j].get(aux[0],None)
                c4CUATRO=dict_code[j].get(aux[1],None)
 
                if (c1UNO!=None and c2DOS!=None):
                    c1UNO=c1UNO.split("#")
                    c2DOS=c2DOS.split("#")
                    if(c1UNO[1]=='string' and c2DOS[1]!='string'):
                        list_de_errores.append(Error(numeroLinea[0],2))
                    elif(c2DOS[1]=='string' and c1UNO[1]!='string'):
                        list_de_errores.append(Error(numeroLinea[0],2))

                elif (c1UNO!=None and c4CUATRO!=None):
                    c4CUATRO=c4CUATRO.split("#")
                    c1UNO=c1UNO.split("#")
                    if c4CUATRO[1].find('_')!=-1:
                        c4CUATRO[1]=c4CUATRO[1].split('_')
                        c4CUATRO[1]=c4CUATRO[1][0]
                    if c1UNO[1].find('_')!=-1:
                        c1UNO[1]=c1UNO[1].split('_')
                        c1UNO[1]=c1UNO[1][0]
                    if(c1UNO[1]=='string' and c4CUATRO[1]!='string'):
                        list_de_errores.append(Error(numeroLinea[0],2))
                    elif(c4CUATRO[1]=='string' and c1UNO[1]!='string'):
                        list_de_errores.append(Error(numeroLinea[0],2))
                    
                elif (c2DOS!=None and c3TRES!=None):
                    c3TRES=c3TRES.split("#")
                    c2DOS=c2DOS.split("#")
                    if c3TRES[1].find('_')!=-1:
                        c3TRES[1]=c3TRES[1].split('_')
                        c3TRES[1]=c3TRES[1][0]
                    if c2DOS[1].find('_')!=-1:
                        c2DOS[1]=c2DOS[1].split('_')
                        c2DOS[1]=c2DOS[1][0]
                    if(c3TRES[1]=='string' and c2DOS[1]!='string'):
                        list_de_errores.append(Error(numeroLinea[0],2))
                    elif(c2DOS[1]=='string' and c3TRES[1]!='string'):
                        list_de_errores.append(Error(numeroLinea[0],2))
                elif (c4CUATRO!=None and c3TRES!=None):
                    c4CUATRO=c4CUATRO.split("#")
                    c3TRES=c3TRES.split("#")
                    if c4CUATRO[1].find('_')!=-1:
                        c4CUATRO[1]=c4CUATRO[1].split('_')
                        c4CUATRO[1]=c4CUATRO[1][0]
                    if c3TRES[1].find('_')!=-1:
                        c3TRES[1]=c3TRES[1].split('_')
                        c3TRES[1]=c3TRES[1][0]

                    if(c3TRES[1]=='string' and c4CUATRO[1]!='string'):
                        list_de_errores.append(Error(numeroLinea[0],2))
                    elif(c4CUATRO[1]=='string' and c3TRES[1]!='string'):
                        list_de_errores.append(Error(numeroLinea[0],2))
                elif(c1UNO!=None):#encontro global
                    c1UNO=c1UNO.split("#")
                    numeroLinea=dict_code[j][fj].split("#")
                    analisisIF=numeroLinea[1].split('_')
                    analisisIF[1].isdecimal()
                    if c1UNO[1].find('_')!=-1:
                        c1UNO[1]=c1UNO[1].split('_')
                        c1UNO[1]=c1UNO[1][0]
                    if analisisIF[1].isdecimal() == False and c1UNO[1]!='string':
                        list_de_errores.append(Error(numeroLinea[0],2))
                    elif analisisIF[1].isdecimal() == True and c1UNO[1]=='string':
                        list_de_errores.append(Error(numeroLinea[0],2))
                    
                elif(c2DOS!=None ):#encontro global
                    c2DOS=c2DOS.split("#")
                    numeroLinea=dict_code[j][fj].split("#")
                    analisisIF=numeroLinea[1].split('_')
                    analisisIF[1].isdecimal()
                    if c2DOS[1].find('_')!=-1:
                        c2DOS[1]=c2DOS[1].split('_')
                        c2DOS[1]=c2DOS[1][0]
                    if analisisIF[1].isdecimal() == False and c2DOS[1]!='string':
                        list_de_errores.append(Error(numeroLinea[0],2))
                    elif analisisIF[1].isdecimal() == True and c2DOS[1]=='string':
                        list_de_errores.append(Error(numeroLinea[0],2))
                elif(c3TRES!=None):#encontro local
                    c3TRES=c3TRES.split("#")
                    numeroLinea=dict_code[j][fj].split("#")
                    analisisIF=numeroLinea[1].split('_')
                    analisisIF[1].isdecimal()
                    if c3TRES[1].find('_')!=-1:
                        c3TRES[1]=c3TRES[1].split('_')
                        c3TRES[1]=c3TRES[1][0]
                    if analisisIF[1].isdecimal() == False and c3TRES[1]!='string':
                        list_de_errores.append(Error(numeroLinea[0],2))
                    elif analisisIF[1].isdecimal() == True and c3TRES[1]=='string':
                        list_de_errores.append(Error(numeroLinea[0],2))
                elif(c4CUATRO!=None ):#encontro local
                    c4CUATRO=c4CUATRO.split("#")
                    numeroLinea=dict_code[j][fj].split("#")
                    analisisIF=numeroLinea[1].split('_')
                    analisisIF[1].isdecimal()
                    if c4CUATRO[1].find('_')!=-1:
                        c4CUATRO[1]=c4CUATRO[1].split('_')
                        c4CUATRO[1]=c4CUATRO[1][0]
                    if analisisIF[1].isdecimal() == False and c4CUATRO[1]!='string':
                        list_de_errores.append(Error(numeroLinea[0],2))
                    elif analisisIF[1].isdecimal() == True and c4CUATRO[1]=='string':
                        list_de_errores.append(Error(numeroLinea[0],2))
            elif fj == 'return':
             
             """
             Caso de que la linea encuetre un "return"

             Variables utilizadas:
             varReturn = Lista que guarda el número de linea y la variable de retorno de la función
             numLF = número de linea donde se encuentra el "return"
             cod = variable de retorno de la función
             cod_value = Lista que guarda el tipo de la variable y la variable
             cod_ValueOriginal = Guarda el tipo de de la variable, para compararlo con tipoFun
             tipoFun = Tipo de la función
             single_quotes = Pequeño truco para saber si la variable es un string que viene encerrado en " "
             """
             varReturn = dict_code[j][fj].split("#")
             numLF[0] = varReturn[0]
    
             # nombre de la variable o el tipo de retorno de la función
             cod = varReturn[1]
             # Verifica si la variable de retorno existe en el diccionario
             if cod in dict_code[j]:
                cod_value = dict_code[j][cod].split("#")

             # Compara el tipo de retorno con el tipo especificado al declarar la función
                if cod_value[1] != tipoFun:
                 list_de_errores.append(Error(numLF[0], 3))
             else:
               if cod in dict_code:
                 cod_value = dict_code[cod].split("#")
                 cod_valueOriginal = cod_value[1].split("_")
                 if cod_valueOriginal[0] != tipoFun:
                   list_de_errores.append(Error(numLF[0], 3))
               else:
                    if tipoFun =="string":
                        single_quotes = ''+cod+''
                        if '\"' in single_quotes:
                            None
                        else:
                            list_de_errores.append(Error(numLF[0],3))
                    elif tipoFun =="float":
                        
                        try:
                            cod = float(cod)
                        except ValueError:
                            list_de_errores.append(Error(numLF[0],3))

                    elif tipoFun =="int":
                        if(cod.isdecimal()!=True):
                            list_de_errores.append(Error(numLF[0],3)) 

            elif ( ((dict_code[j][fj]).split('#'))[0]!= numLF[0]):
                if( ((dict_code[j][fj]).split('#'))[1].find('float')!=-1 or ((dict_code[j][fj]).split('#'))[1].find('int')!=-1 or ((dict_code[j][fj]).split('#'))[1].find('string')!=-1):#errores de locales
                    if(((dict_code[j][fj]).split('#'))[1].find('float')!=-1 ):
                        numeroLinea=dict_code[j][fj].split("#")
                        tipoYvalor=numeroLinea[1].split('_')
                        try:
                            sera_float_value = float(tipoYvalor[1])
                        except ValueError:
                            list_de_errores.append(Error(numeroLinea[0],1))
                    elif(((dict_code[j][fj]).split('#'))[1].find('int')!=-1 ):
                        numeroLinea=dict_code[j][fj].split("#")
                        tipoYvalor=numeroLinea[1].split('_')
                        if(tipoYvalor[1].isdecimal()!=True):
                            list_de_errores.append(Error(numeroLinea[0],1))
                    else:
                        numeroLinea=dict_code[j][fj].split("#")
                        tipoYvalor=numeroLinea[1].split('_')
                        single_quotes = ''+tipoYvalor[1]+''
                        if '\"' in single_quotes:
                            None
                        else:
                            list_de_errores.append(Error(numeroLinea[0],1))
                else:
                    numeroLinea=dict_code[j][fj].split("#")

                    dict_de_funci=dict_code.get(j,None)
                    variable_asignada=dict_de_funci.get(numeroLinea[1],None)
                    if(variable_asignada!=None):#ANALISIS de asigncion a una variable local
                        print("ANALISIS de asigncion a una variable local")
                        variable_asignada=(variable_asignada.split("#"))[1]
                        posi=variable_asignada.find("_")
                        if(posi!=-1):
                            variable_asignada=variable_asignada[:posi]
                            variable_asignada=variable_asignada.removeprefix('_')

                        print(variable_asignada)
                        print(fj)
                        if (fj.find('+')!=-1) or (fj.find('-')!=-1) or (fj.find('/')!=-1) or (fj.find('%')!=-1) or (fj.find('*')!=-1):
                            lisAUX=[]
                            for c in fj:
                                '''
                                check4H= Check for hashing
                                check4H_fun= Check for hashing in funcion
                                '''
                                check4H=dict_code.get(c,None)
                                check4H_fun=dict_de_funci.get(c,None)

                                if check4H != None and  (check4H.find('string')!=-1 or check4H.find('float')!=-1 or check4H.find('int')!=-1):
                                    check4H=(check4H.split('#'))[1]
                                    check4H=(check4H.split('_'))[0]
                                    lisAUX.append(c)
                                    if variable_asignada!=check4H:
                                        list_de_errores.append(Error(numeroLinea[0],1))

                                elif check4H_fun != None  and (check4H_in_fun.find('string')!=-1 or check4H_in_fun.find('float')!=-1 or check4H_in_fun.find('int')!=-1):
                                    check4H_fun=(check4H_fun.split('#'))[1]
                                    check4H_fun=(check4H_fun.split('_'))[0]
                                    lisAUX.append(c)
                                    if variable_asignada!=check4H_fun:
                                        list_de_errores.append(Error(numeroLinea[0],1))
                            ###################################################################
                            fjaux=fj
                            for i in lisAUX:
                                 fjaux=fjaux.removeprefix(i)

                            fjaux=fjaux.replace('+','_')
                            fjaux=fjaux.replace('/','_')
                            fjaux=fjaux.replace('-','_')
                            fjaux=fjaux.replace('%','_')
                            fjaux=fjaux.replace('*','_')
                            fjaux=fjaux.split('_')
                            for i in fjaux:
                                verificar_congruencia_de_tipo(variable_asignada,i)
                        else:
                            check4H=dict_code.get(fj,None)
                            check4H_in_fun=dict_de_funci.get(fj,None)

                            if check4H !=None and  (check4H.find('string')!=-1 or check4H.find('float')!=-1 or check4H.find('int')!=-1):
                                check4H=(check4H.split('#'))[1]
                                check4H=(check4H.split('_'))[0]
                                if variable_asignada!=check4H:
                                        list_de_errores.append(Error(numeroLinea[0],1))
                            elif check4H_in_fun !=None and (check4H_in_fun.find('string')!=-1 or check4H_in_fun.find('float')!=-1 or check4H_in_fun.find('int')!=-1):
                                check4H_in_fun=(check4H_in_fun.split('#'))[1]
                                check4H_in_fun=(check4H_in_fun.split('_'))[0]
                                if variable_asignada!=check4H_in_fun:
                                        list_de_errores.append(Error(numeroLinea[0],1))
                            else:
                                print("a individual")
                                if(variable_asignada=='float'):
                                    try:
                                        sera_float_value = float(fj)
                                    except ValueError:
                                        list_de_errores.append(Error(numeroLinea[0],1))
                                elif(variable_asignada=='int'):
                                    if(fj.isdecimal()!=True):
                                        list_de_errores.append(Error(numeroLinea[0],1))
                                else:
                                    single_quotes = ''+fj+''
                                    if '\"' in single_quotes:
                                        None
                                    else:
                                        list_de_errores.append(Error(numeroLinea[0],1))

                    elif(dict_code.get(numeroLinea[1],None)!=None):#ANALISIS de asigncion a una variable global
                        
                        print("ANALISIS de asigncion a una variable global")
                        variable_asignada=dict_code.get(numeroLinea[1],None)
                        variable_asignada=(variable_asignada.split("#"))[1]
                        posi=variable_asignada.find("_")
                        if(posi!=-1):
                            variable_asignada=variable_asignada[:posi]
                            variable_asignada=variable_asignada.removeprefix('_')
                            
                        print(variable_asignada)
                        print(fj)
                        if (fj.find('+')!=-1) or (fj.find('-')!=-1) or (fj.find('/')!=-1) or (fj.find('%')!=-1 or (fj.find('*')!=-1)):
                            lisAUX=[]
                            for c in fj:
                                check4H=dict_code.get(c,None)
                                check4H_fun=dict_de_funci.get(c,None)
                                if check4H != None and  (check4H.find('string')!=-1 or check4H.find('float')!=-1 or check4H.find('int')!=-1):
                                    check4H=(check4H.split('#'))[1]
                                    check4H=(check4H.split('_'))[0]
                                    lisAUX.append(c)
                                    if variable_asignada!=check4H:
                                        list_de_errores.append(Error(numeroLinea[0],4))
                                elif check4H_fun != None  and (check4H_fun.find('string')!=-1 or check4H_fun.find('float')!=-1 or check4H_fun.find('int')!=-1):
                                    check4H_fun=(check4H_fun.split('#'))[1]
                                    check4H_fun=(check4H_fun.split('_'))[0]
                                    lisAUX.append(c)
                                    if variable_asignada!=check4H_fun:
                                        list_de_errores.append(Error(numeroLinea[0],4))
                            ##########################################33
                            fjaux=fj
                            for i in lisAUX:
                                 fjaux=fjaux.replace(i,'')

                            fjaux=fjaux.replace('+','_')
                            fjaux=fjaux.replace('/','_')
                            fjaux=fjaux.replace('-','_')
                            fjaux=fjaux.replace('%','_')
                            fjaux=fjaux.replace('*','_')
                            fjaux=fjaux.split('_')
                            for i in fjaux:
                                verificar_congruencia_de_tipo(variable_asignada,i)
                        else:
                            #ver si le estoy asignando una variable a otra
                            check4H=dict_code.get(fj,None)
                            check4H_in_fun=dict_de_funci.get(fj,None)

                            if check4H !=None and  (check4H.find('string')!=-1 or check4H.find('float')!=-1 or check4H.find('int')!=-1):
                                check4H=(check4H.split('#'))[1]
                                check4H=(check4H.split('_'))[0]
                                if variable_asignada!=check4H:
                                        list_de_errores.append(Error(numeroLinea[0],4))
                            elif check4H_in_fun !=None and (check4H_in_fun.find('string')!=-1 or check4H_in_fun.find('float')!=-1 or check4H_in_fun.find('int')!=-1):
                                check4H_in_fun=(check4H_in_fun.split('#'))[1]
                                check4H_in_fun=(check4H_in_fun.split('_'))[0]
                                if variable_asignada!=check4H_in_fun:
                                        list_de_errores.append(Error(numeroLinea[0],4))
                            else:
                                print("a individual")
                                if(variable_asignada=='float'):
                                    try:
                                        sera_float_value = float(fj)
                                    except ValueError:
                                        list_de_errores.append(Error(numeroLinea[0],4))
                                elif(variable_asignada=='int'):
                                    if(fj.isdecimal()!=True):
                                        list_de_errores.append(Error(numeroLinea[0],4))
                                else:
                                    single_quotes = ''+fj+''
                                    if '\"' in single_quotes:
                                        None
                                    else:
                                        list_de_errores.append(Error(numeroLinea[0],4))                                


                    else:
                        list_de_errores.append(Error(numeroLinea[0],5))
                    #list_de_errores.append(Error(numeroLinea[0],1))
                    # operaciones de asignacion        
                    
    else:#errores de globales
        numLF=((dict_code[j]).split('#'))[0]
        a=((dict_code[j]).split('#'))[1]

        if(a.find('float')!=-1 and a.find('_')!=-1):
            tipoYvalor=a.split('_')
            try:
                sera_float_value = float(tipoYvalor[1])
            except ValueError:
                list_de_errores.append(Error(numLF,4))

        elif(a.find('int')!=-1 and a.find('_')!=-1):
            tipoYvalor=a.split('_')
            if(tipoYvalor[1].isdecimal()!=True):
                list_de_errores.append(Error(numLF,4))

        elif (a.find('_')!=-1):
            tipoYvalor=a.split('_')
            single_quotes = ''+tipoYvalor[1]+''
            if '\"' in single_quotes:
                None
            else:
                list_de_errores.append(Error(numLF,4))



print("-----------------------------------Diccionario Principal del Codigo---------------------------------------")
pprint(dict_code)
print("----------------------------------------------------------------------------------------------------------")
print("-------------------------------------------Lista de Errores-----------------------------------------------")
for i in range(0,len(list_de_errores)):
    list_de_errores[i].toString()
print("----------------------------------------------------------------------------------------------------------")

'''
-----------------CODIGO DEL TXT-------------------------

int x = 40
int funcion(float v, string n){
 if (v > 0.0){
 n = “Mayor”
 x = x + 5
 }
 return n
 }

 -------------------------------------------------------
'''