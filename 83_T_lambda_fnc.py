lide = ["Ruda", "Petr", "Pavla", "Petra"]

def porovnej_delku_jmen(jmeno1, jmeno2):
    return len(jmeno1) > len(jmeno2)

print(porovnej_delku_jmen(lide[2], lide[1]))

#Zde napište lambda funkci která udělá to samé( porovnej_delku_jmen)
#porovnat = lambda lide[1], lide[2]: lide[1] > lide[2]
porovnat_lambda = lambda hodnota1, hodnota2: hodnota1 > hodnota2
print(porovnat_lambda(lide[1], lide[2]))
#---------------------------
'''
def jsou_indexy_stejne(list_polozek):
    return list_polozek[2] == list_polozek[3]

print(jsou_indexy_stejne(lide))
#zde napište lambda funkci která udělá to samé( jsou_indexy_stejne)

porovnat_indexy_lambda = lambda hodnota1, hodnota2: hodnota1 == hodnota2
print(porovnat_indexy_lambda(list_polozek[2], list_polozek[3]))
'''