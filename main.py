from logic.topicOne import tabla_distribucion
from logic.topicThree import tendencia_central
from logic.topicTwo import valores_intermedios


def menu():
    print("                            Menu de Opciones                         ")
    print('''1 >> Crear tabla de distribucion de frecuencia.''')
    print('''2 >> Determinar cantidad que cumple con un valor condicional .''')
    print('''3 >> Determinar valores de medida de tendencia central).''')
    opc = int(input("ingrese el numero de opcion a realizar: "))
    return opc


def choose_option(number):
    if number == 1:
        tabla_distribucion()
    elif number == 2:
        valores_intermedios()
    elif number == 3:
        tendencia_central()
    else:
        print("[ERROR] - digite una opcion valida")


opc = menu()
choose_option(opc)
