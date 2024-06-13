from Clase_producto import Producto #Importamos la clase producto

class Electronico(Producto): #Creamos la clase Electrónico y le damos como parametro la clase padre Producto.

    def __init__(self, nombre, precio, cantidad, marca, modelo):  #Metodo constructor con los atributos heredados de la clase padre y agregamos los atributos marca y modelo.
        super().__init__(nombre, precio, cantidad)
        self.marca = marca 
        self.modelo = modelo 
    
    #Metodos especiales de la clase Electrónico.

    def get_marca(self):
        return self.marca
    
    def get_modelo(self):
        return self.modelo
    
    def mostrar_info(self):  #Mostrar información completa del producto electronico.
        super().mostrar_info()  #Muestra los atributos de la clase padre.
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")