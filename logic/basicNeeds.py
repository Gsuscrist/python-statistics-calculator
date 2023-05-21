from tabulate import tabulate

headers = ["# Clase", "lim inf", "lim sup", "frecuencia"]

def create_table(data):
    tabla = tabulate(data, headers, tablefmt="pretty")
    return tabla


