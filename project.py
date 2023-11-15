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
    0: 'Error A',
    1: 'Error B', 
    2: 'Error C',
    3: 'Error D',
    4: 'Error E', 
    5: 'Error F',
    6: 'Error G',
    7: 'Error H', 
    8: 'Error I',
    9: 'Error J'
}
#---------------------------------Error Class----------------------------------------------
class Errores:
    def __init__(self,s="",e=-1):
        self.string2lookUP=s
        self.codeError=e
    def get_string2lookUP(self):
        return self.string2lookUP
    def get_codeError(self):
        return self.e
    def toString(self):
        print(f"ERROR: Linea: #"+{LineaXLinea.index(self.s)}+" Tipo de Error:"+{dict_ERRORES.get(self.e,"that error code is not in [dict_ERRORES]")})
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
                dict_code[Fun_key]['if']=str(nL)+"-"+izq+'_'+der 
            elif( valores.find('>')!=-1):#case >
                posi = valores.find('>')
                izq=valores[:posi].strip()
                der=valores[posi:].removeprefix('>').strip()
                dict_code[Fun_key]['if']=str(nL)+"-"+izq+'_'+der 
            elif( valores.find('<')!=-1 ):#case <
                posi = valores.find('<')
                izq=valores[:posi].strip()
                der=valores[posi:].removeprefix('<').strip()
                dict_code[Fun_key]['if']=str(nL)+"-"+izq+'_'+der 
            elif( valores.find('<=')!=-1 ):#case <=
                posi = valores.find('<=')
                izq=valores[:posi].strip()
                der=valores[posi:].removeprefix('<=').strip()
                dict_code[Fun_key]['if']=str(nL)+"-"+izq+'_'+der 
            else:                          #case >= 
                posi = valores.find('>=')
                izq=valores[:posi].strip()
                der=valores[posi:].removeprefix('>=').strip()
                dict_code[Fun_key]['if']=str(nL)+"-"+izq+'_'+der
        # Operator of assigning value '=' in the function
        if (j.find('=')!=-1):
            posi=j.find('=') 
            antes_de_char=j[:posi]
            despues_de_char=j[posi:].removeprefix('=')
            despues_de_char=despues_de_char.strip() 
            dict_code[Fun_key][despues_de_char.strip()]=str(nL)+"-"+j[:posi].strip()# Key's in a dict must be unique 
        if (j.find('return')!=-1):
            posi=j.find('return')
            despues_de_char=j[posi:].removeprefix('return')
            despues_de_char=despues_de_char.strip() 
            dict_code[Fun_key]['return']=str(nL)+"-"+despues_de_char.strip()# Key's in a dict must be unique
        #(if)----------------------------------------------------------

    # Note: the next 'if' will only check for a function because...
    # because we will never going to find the key word='if' out of a function     
    # (function)-------------------------------------------------------
    if(InFUN==False):            
        if(j.find(')')!=-1 or j.find('(')!=-1):
            InFUN=True
            #adding return value:
            posi=j.find(' ')
            #Function key
            Fun_key=str(nL)+"-"+j[:posi].strip()
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
                print(two[1])
                print(two[0])
                dict_code[Fun_key][two[1]]=str(nL)+"-"+two[0]
                dict_code[Fun_key][one[1]]=str(nL)+"-"+one[0]
        # (function)-------------------------------------------------------  


            
         
    #(if) 4 global varibles
    if(InFUN==False):
        if (j.find('int')!=-1):
            if (j.find('=')!=-1):
                posi=j.find('=')
                j=j[:posi]
                j=j.removeprefix('=')
            j=j.split(' ')
            dict_code[j[1]]=str(nL)+"-"+j[0]

        elif (j.find('float')!=-1):
            if (j.find('=')!=-1):
                posi=j.find('=')
                j=j[:posi]
                j=j.removeprefix('=')
            j=j.split(' ')
            dict_code[j[1]]=str(nL)+"-"+j[0]
            #str(nL)+"-"{CASTING}
        elif (j.find('string')!=-1): #safer to not put else 
            if (j.find('=')!=-1):
                posi=j.find('=')
                j=j[:posi]
                j=j.removeprefix('=')
            j=j.split(' ')
            dict_code[j[1]]=str(nL)+"-"+j[0]
    nL=nL+1

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
