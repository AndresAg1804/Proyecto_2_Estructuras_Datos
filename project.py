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
    0: 'valor de retorno invalido',
    1: 'asignacion de valor invalida hacia una variable', 
    2: 'comparacion invalida con string en condicional ',
    3: 'valor de retorno invalido'
}
#---------------------------------Error Class----------------------------------------------
class Error:
    def _init_(self,nl="",e=-1):
        self.nl=nl
        self.codeError=e
    def get_string2lookUP(self):
        return self.nl
    def get_codeError(self):
        return self.e
    def toString(self):
        print(f"ERROR: Linea: #"+{nL}+" Tipo de Error: ["+{dict_ERRORES.get(self.e,"that error code# is not in [dict_ERRORES]")}+"]")
#---------------------------------Error Class----------------------------------------------

    #nota: how can I get the dict value with out a KeyError: 
    #like so...
print(dict_ERRORES.get(9,"Key not in dict_ERRORES"))
print(dict_ERRORES.get(10,"Key not in dict_ERRORES"))
print("-----------------------------------Lista para saber el # de linea---------------------------------------")
pprint(LineaXLinea)
print("--------------------------------------------------------------------------------------------------------")
dict_code={}
Fun_key=''
InFUN=False
nL=1
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
                j=j[:posi]
                j=j.removeprefix('=')
            j=j.split(' ')
            dict_code[Fun_key][j[1]]=str(nL)+"#"+j[0]
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
                posi=j.find('=')    #int x=40
                j=j[:posi]
                j=j.removeprefix('=')
            j=j.split(' ')
            dict_code[j[1]]=str(nL)+"#"+j[0]
    nL=nL+1
#for para leer errors   
list_de_errores=[]
for j in dict_code:
    if (j.find('int')!=-1 or j.find('string')!=-1 or j.find('float')!=-1 or j.find('void')!=-1):
        numLF=j.split('#')
        print(numLF[0])
        print(numLF[1])
        for fj in dict_code[j]:#vaya iterando por todas las llaves del dict interno
            if(fj=="if" or fj=="while"):
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
                        list_de_errores.append(Error(numeroLinea[0],0))
                    elif(c2DOS[1]=='string' and c1UNO[1]!='string'):
                        list_de_errores.append(Error(numeroLinea[0],0))
                elif (c1UNO!=None and c4CUATRO!=None):
                    print()
                elif (c2DOS!=None and c3TRES!=None):
                    print()
                elif (c4CUATRO!=None and c3TRES!=None):
                    c4CUATRO=c4CUATRO.split("#")
                    c3TRES=c3TRES.split("#")
                    if(c3TRES[1]=='string' and c4CUATRO[1]!='string'):
                        list_de_errores.append(Error(numeroLinea[0],2))
                    elif(c4CUATRO[1]=='string' and c3TRES[1]!='string'):
                        list_de_errores.append(Error(numeroLinea[0],2))
                elif(c1UNO!=None):#encontro global
                    print()
                elif(c2DOS!=None ):#encontro global
                    print()
                elif(c3TRES!=None):#encontro local
                    print()
                elif(c4CUATRO!=None ):#encontro local
                    print()
            if(fj=='return'):
               varReturn=dict_code[j][fj]
               print(varReturn)
            if ( ((dict_code[j][fj]).split('#'))[0]!= (j.split('#'))[0]):
                if( ((dict_code[j][fj]).split('#'))[1].find('float')!=-1):#errores de locales
                    print("Se encontro un var float")
    else:
        #errores de globales
        print()


print("-----------------------------------Diccionario Principal del Codigo---------------------------------------")
pprint(dict_code)
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