from Clase_producto import Producto #Importamos la clase producto

class Alimento(Producto): #Creamos la clase Alimento y le damos como parametro la clase padre Producto.

    def __init__(self, nombre, precio, cantidad, fecha_expiración): #Metodo constructor con los atributos heredados de la clase padre y agregamos el atributo de fecha de expiración.
        super().__init__(nombre, precio, cantidad)
        self.fecha_expiración = fecha_expiración
    
    #Metodos especiales de la clase Alimento.

    def get_fecha_expiración(self):
        return self.fecha_expiración
    
    def mostrar_info(self):  #Mostrar información completa del producto alimenticio.
        super().mostrar_info()  #Muestra los atributos de la clase padre.
        print(f"Fecha de expiración: {self.fecha_expiración}")