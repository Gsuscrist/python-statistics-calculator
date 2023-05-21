import math
from decimal import Decimal
from prettytable import PrettyTable

def tabla_distribucion():
    # creacion de tabla
    table = PrettyTable()
    table.field_names = ["Clase", "Lim sup", "Lim inf", "frecuencia", "lim inf ex", "lim sup ex", "marca de clase",
                         "frec relativa en proporcion", "frec relativa en porcentaje", "frec acumulada",
                         "frec complementaria"]

    unit_variable = 0
    lim_sup = 0
    lim_inf = 0
    lim_sup_ex = 0
    lim_inf_ex = 0
    class_mark = 0
    frec_ab = 0
    frec_ac = 0
    frec_co = 0
    frec_re_pr = 0
    frec_re_po = 0

    # ingrese datos
    data_arr = []
    data = input("ingrese datos:")


    # get every item
    data_str_arr = data.split(',')


    # funcion para saber el max de decimales
    def get_decimals_of(data):
        max_count = 0
        for x in data:
            count = len(x) - x.index('.') - 1
            if count > max_count:
                max_count = count
        return max_count - 1


    # funcion para convertir datos en su tipo de dato correcto
    def set_type_of(data):
        if '.' in data:
            data_arr = list(map(float, data_str_arr))
        else:
            data_arr = list(map(int, data_str_arr))
        return data_arr


    # funcion para tener la unidad de variacion
    def set_unit_variable(data):
        if type(data_arr[1]) == float:
            count = get_decimals_of(data)
            return Decimal(f'0.{"0" * count}1')
        else:
            return 1


    def get_classes_amount(size):
        number_of_classes = (1 + 3.322) * (math.log10(size))
        return int(number_of_classes)


    # funcion para obtener el lim_sup
    def get_sup_lim(number):
        lim_sup = number + amplitud - unit_variable
        return lim_sup


    # funcion para obtener frecuencia
    def get_frecuency(number_inf, number_sup):
        count = 0
        for x in data_arr_sort:
            if number_inf <= x <= number_sup:
                count += 1
        return count


    def get_inf_lim_ex(lim_inf):
        return lim_inf - (unit_variable / 2)


    def get_sup_lim_ex(lim_sup):
        return lim_sup + (unit_variable / 2)


    def get_class_mark(lim_inf, lim_sup):
        return (lim_inf + lim_sup) / 2


    def get_frec_proporcion(frec):
        return frec / len(data_arr_sort)


    def get_frec_porcentaje(frec):
        return frec * 100


    def get_frec_acumulada(frec_ac, frec_ab):
        return frec_ac + frec_ab


    def get_frec_complementaria(total, frec_ab):
        return total - frec_ab


    # llamada de todas las funciones
    # asignar tipo
    data_arr = set_type_of(data)
    # saber unidad de variacion
    unit_variable = set_unit_variable(data_str_arr)
    print('la unidad de variacion es', unit_variable)

    # number of elements (size)
    size_of_data = len(data_arr)
    print(size_of_data)

    # sort data
    data_arr_sort = sorted(data_arr)
    print(sorted(data_arr))

    # get classes number
    k = get_classes_amount(len(data_arr))
    print('the number of clases are: ', k)

    # get rango
    rango = (data_arr_sort[size_of_data - 1] - data_arr_sort[0])
    print('el rango es:', rango)

    # get amplitud
    numero_amp = rango / k
    amplitud = int(numero_amp+1)
    print('la amplitud es:', amplitud)




    #tecnically this what gives form to the
    i = 0
    while i < k:
        if i == 0:
            lim_inf = data_arr_sort[0]
            lim_sup = get_sup_lim(lim_inf)
            frec_ac = get_frecuency(lim_inf,lim_sup)
            total = len(data_arr_sort) - frec_ab
        else:
            lim_inf = lim_sup + unit_variable
            lim_sup = get_sup_lim(lim_inf)
            frec_ac = get_frec_acumulada(frec_ac, get_frecuency(lim_inf,lim_sup))
            total = total - frec_ab

        frec_ab = get_frecuency(lim_inf, lim_sup)
        class_mark = get_class_mark(lim_inf,lim_sup)
        lim_inf_ex = get_inf_lim_ex(lim_inf)
        lim_sup_ex = get_sup_lim_ex(lim_sup)
        frec_re_pr = get_frec_proporcion(frec_ab)
        frec_re_po = get_frec_porcentaje(frec_re_pr)

        frec_co = get_frec_complementaria(total, frec_ab)

        table.add_row([i + 1, lim_inf, lim_sup, frec_ab,lim_inf_ex,lim_sup_ex,class_mark,
                       frec_re_pr,frec_re_po,frec_ac,frec_co ])
        i += 1

    print(table)
