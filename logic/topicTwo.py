from tabulate import tabulate
from logic.basicOperations import get_class_mark


def valores_intermedios():
    headers = ["# Clase", "lim inf", "lim sup", "frecuencia", "marca de clase", "frec. acumulada",
               "frec. complementaria"]
    frec_ac = 0
    frec_co = 0
    unit_variable = 0

    def get_frec_acumulada(frec_ac, frec_ab):
        return frec_ac + frec_ab

    def get_frec_complementaria(total, frec_ab):
        return total - frec_ab

    def get_total(data):
        suma = 0
        for z in data:
            suma = suma + z[3]
        return suma

    def fill_table(number):
        i = 0
        data = []
        while i < number:
            i += 1
            class_number = i
            lim_inf = input("lim inf: ")
            lim_sup = input("lim sup: ")
            frecuency = input("frecuencia: ")
            # Agrega los datos ingresados a la lista 'data'
            data.append([class_number, lim_inf, lim_sup, frecuency])
        return data

    def assign_type_of_value(data):
        format_data = []
        for x in data:
            if '.' in str(x):
                format_data.append(list(map(float, x)))
            else:
                format_data.append(list(map(int, x)))
        return format_data

    def complete_data_information(data):
        i = 0
        full_data = []
        for x in data:
            class_mark = get_class_mark(x[1], x[2])
            if i == 0:
                frec_ac = x[3]

                total = get_total(data)
                frec_co = total - x[3]
            else:
                frec_ac = frec_ac + x[3]
                frec_co = get_frec_complementaria(frec_co, x[3])

            i += 1
            x.append(class_mark)
            x.append(frec_ac)
            x.append(frec_co)
            full_data.append(x)
        return full_data

    def generate_table(data):
        tabla = tabulate(data, headers, tablefmt="pretty")
        return tabla

    def _start_function():
        data = []
        class_number = int(input('ingrese el numero total de clases: '))
        data = fill_table(class_number)
        data = assign_type_of_value(data)
        data = complete_data_information(data)
        table = generate_table(data)
        print(table)
        return data

    def set_type(number):
        if '.' in number:
            number = float(number)
        else:
            number = int(number)
        return number

    def set_unit_variable(sup_lim, inf_lim):
        unit_variable = sup_lim - inf_lim
        return unit_variable

    def get_class(number):
        i = 0
        for x in data:
            if x[2] < number:
                i += 1
        return i

    def get_frec_co_nx(class_number):
        number = 0
        for x in data:
            if x[0] > class_number:
                number = number + x[3]
        return number

    def get_frec_co_ny(class_number):
        number = 0
        for x in data:
            if x[0] <= class_number:
                number = number + x[3]
        return number

    # sacar frec entre nx y ny
    def get_frec_co_between(class_number):
        number = 0

        return number

    def get_nx(number, search_value):
        main_class = data[number]
        unit_variable = set_unit_variable(data[1][1],data[0][2])
        frec_co_nx = get_frec_co_nx(number)
        nx = ((((main_class[2] - search_value - unit_variable) / (main_class[2] - main_class[1] + unit_variable)) *
               main_class[3]) + frec_co_nx)
        print('el numero de datos con al menos el valor es de: ', nx)
        return nx

    def get_ny(number, search_value):
        main_class = data[number]
        unit_variable = set_unit_variable(data[1][1],data[0][2],)
        frec_co_ny = get_frec_co_ny(number)
        print('frec_co: ',frec_co_ny)
        ny = ((((search_value - main_class[1] + unit_variable) / (main_class[2] - main_class[1] + unit_variable)) *
               main_class[3]) + frec_co_ny)
        print('el numero de datos con un maximo al valor es de: ', ny)
        return ny

    def get_maximum_value():
        value = input('ingrese el valor maximo: ')
        value = set_type(value)
        class_number = get_class(value)
        maximum = get_ny(class_number, value)
        return maximum

    def get_minimum_value():
        value = input('ingrese el valor minimo:')
        value = set_type(value)
        class_number = get_class(value)
        minimum = get_nx(class_number, value)
        return minimum

#not sure if this is right
    def get_between_value():
        minimum_value = get_minimum_value()
        maximum_value = get_maximum_value()
        nz = maximum_value + minimum_value
        print('el numero de datos que cumplen la condicion es: ', nz-get_total(data))

    def menu():
        print("                            Menu de Opciones                         ")
        print('''1 >> determinar el numero aprox. que cumpla como minimo un valor(almenos).''')
        print('''2 >> determinar el numero aprox. que cumpla como maximo un valor(maximo).''')
        print('''3 >> determinar el numero aprox. que cumpla entre un rango(entre).''')
        opc = int(input("ingrese el numero de opcion a realizar: "))
        return opc

    def choose_option(number):
        if number == 1:
            get_minimum_value()
        elif number == 2:
            get_maximum_value()
        elif number == 3:
            get_between_value()
        else:
            print("[ERROR] - digite una opcion valida")

    # funcion de arranque
    data = _start_function()

    # logica en base a operacion
    opc = menu()
    choose_option(opc)
