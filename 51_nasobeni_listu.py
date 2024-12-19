#Vynasob list
#
#Varianta 1
def vynasob_list(data, nasobek=3):
    vynasobena_data = []
    for cislo in data:
        vynasobena_data.append(cislo*nasobek)
    return vynasobena_data

#Varianta 2
def vynasob_list2(data, nasobek=3):
    for index, cislo in enumerate(data):
        data[index] = cislo*nasobek
    return data


print(vynasob_list2([3,4,1,2])) #[9,12,3,6]
print(vynasob_list2([1,4,1,2])) #[3,12,3,6]
print(vynasob_list2([1,4,1,2], 2)) #[2,8,2,4]


def pocet_parametru(*args):
    pocet_argumentu = len(args)
    if pocet_argumentu == 1:
        return f"{pocet_argumentu} argument"
    #elif pocet_argumentu == 2 or pocet_argumentu == 3 or pocet_argumentu == 4: #
    #elif pocet_argumentu in [2,3,4]:
    elif 2 <= pocet_argumentu <= 4:
        return f"{pocet_argumentu} argumenty"
    else:
        return f"{pocet_argumentu} argumentů"

print(pocet_parametru()) #3 prametry
print(pocet_parametru(3)) #3 prametry
print(pocet_parametru(2,3,4)) #3 prametry
print(pocet_parametru(2,3,4,2,2)) #5 parametrů  !!! POZOR, MUSÍ TO BÝT ČESKY