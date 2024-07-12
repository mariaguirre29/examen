import random 
import statistics
import csv

trabajadores = [
    "Juan Perez", "María García", "Carlos López", "Ana Martinez", "Pedro Rodriguez", "Laura Hernandéz", "Miguel Sanchéz", "Isabel Goméz", "Francisco Díaz", "Elena Fernandéz"
]


def menu():
    print("1. Asignar sueldos aleatorios")
    print("2. Clasificar sueldos")
    print("3. Ver estadísticas")
    print("4. Reporte de sueldos")
    print("5. Salir del programa")

def asignar_sueldos():
    sueldos = [random.randint(300000, 2500000) for trabajadores in range (10)]
    return 
# clasificar los sueldos segun monto 

def clasificar_sueldos(asignar_sueldos):
    if asignar_sueldos <= 800000:
        pass
        

def ver_estadisticas(clasificar_sueldos):
    if sueldos:
        max_sueldo = max(sueldos.values)
        pass

# SUBIR A CSV

def importe_csv(trabajadores, filename='sueldos.csv'):
    
    if trabajadores:
        keys = trabajadores[0].keys()
        with open(filename, 'w', newline='') as output_file:
            dict_writer = csv.DictWriter(output_file, fieldnames=keys)
            dict_writer.writeheader()
            dict_writer.writerows(trabajadores)
        print(f"clasificaciones guardadas en el archivo {filename}")
    else:
        print("No hay archivos para guardar.")