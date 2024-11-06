import turtle
import pandas as pd
import csv

screen = turtle.Screen()
# screen.title("Coordenadas provincias")
image = "blank_spain_provinces.gif"
screen.addshape(image)
turtle.shape(image)

# Cargar lista de provincias
provinces_list = pd.read_csv("provinces.csv")
print(provinces_list)
provincias = provinces_list["provincia"].to_list()
print(provincias)

# Crear archivo CSV y escribir encabezado fuera del evento
file = open("provinces_coordinates.csv", mode="w", newline='')
writer = csv.writer(file)
writer.writerow(["provincia", "x", "y"])

# Índice de la provincia actual
index = 0

# screen.title(f"Haz click en {provincias[index]}")

# # Función para capturar las coordenadas
# def get_coordinates(x, y):
#     global index
#     if index < len(provincias):
#         nombre_provincia = provincias[index]
#         writer.writerow([nombre_provincia, x, y])
#         print(f"{nombre_provincia}: ({x}, {y})")
#         index += 1
#         if index < len(provincias):
#             screen.title(f"Haz click en {provincias[index]}")
#         else:
#             screen.title("Captura completa")
#             file.close()  # Cierra el archivo solo al final
#
# # Inicializar título de la primera provincia
#
#
# # Llamar a la función cuando se hace clic en la pantalla
# screen.onscreenclick(get_coordinates)
screen.exitonclick()
