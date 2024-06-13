#Importamos todas las clases para utilizarlas en el archivo MAIN.

from Clase_producto import Producto
from Clase_electronico import Electronico
from Clase_alimento import Alimento

#Llamamos a todas las clases.

producto_1 = Electronico("Celular", 700, 5, "Apple", "iPhone 13")
producto_2 = Alimento("Mandarina", 70, 100, "2024-6-25")
producto_3 = Producto("Silla", 500, 10)

#Mostramos toda la información de los distintos productos mediante el metodo "mostrar_info".
#Utilizamos el \n para separar los distintos productos y sea más legible.

print("""\nProducto Electronico:
      """)
producto_1.mostrar_info()


print("""\nProducto alimento:
      """)
producto_2.mostrar_info()


print("""\nProducto:
      """)
producto_3.mostrar_info()