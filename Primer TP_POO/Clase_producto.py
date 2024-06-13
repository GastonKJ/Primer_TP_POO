class Producto:  # Clase de los productos con los atributos de nombre, precio y cantidad.

    def __init__(self, nombre, precio, cantidad): #Metodo constructor con los atributos de nombre, precio y cantidad.
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    #Metodos de cada uno de los atributos.

    def get_nombre(self):
        return self.nombre
    
    def get_precio(self):
        return self.precio
    
    def get_cantidad(self):
        return self.cantidad
    
    def mostrar_info(self):  #Motrar información completa del producto.
        print(f"Nombre: {self.nombre}")
        print(f"Precio: {self.precio}")
        print(f"Cantidad: {self.cantidad}")