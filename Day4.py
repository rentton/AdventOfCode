#PRIMERA PARTE
#-------------

name = "Day4.txt"

def Input(name):
    
    data_list = []
    data = ""
    
    f = open(name,"r")
    for line in f:
        if line == "\n":                    #Cuando encontremos una separación entre pasaporte
            data = data.split()             #Separamos todos los campos
            data_list.append(data)          #Lo introducimos en una posición de la lista final
            data = ""
        else:
            data += line            #Introducimos cada línea en un string

    #Como se perdería la última iteración:
    data = data.split()             
    data_list.append(data) 

    return data_list

fields = {
    "byr": False,
    "iyr": False,
    "eyr": False,
    "hgt": False,
    "hcl": False,
    "ecl": False,
    "pid": False
}

salida2 = []

def TestCount(final_fields):
    for f in final_fields.values():
        if not f:
            return False
    return True 
    
def Valids(data_list, fields):
    valids_passport = 0
    
    for data in range(len(data_list)):
        fields_copy = fields.copy()
        prueba = []
        for f in data_list[data]:
           act_field = f[0:3]
           if act_field != "cid":
            fields_copy[act_field] = True
            
        if TestCount(fields_copy):
            valids_passport += 1
            
    return valids_passport
                  
d = Input(name)
print(Valids(d,fields))


#SEGUNDA PARTE
#-------------