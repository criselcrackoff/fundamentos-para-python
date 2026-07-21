# Definir una clase llamada Producto con los siguientes atributos:
# id
# nombre
# descripción
# precio_normal
# precio_oferta
# cantidad

# siguientes métodos:
# getters/setters según corresponda
    # validaciones: 
    # precio_normal > 0
    # precio_oferta < precio_normal
    # cantidad >= 0
# ver_info()

class Producto:
    def __init__(self,id,nombre,descripcion,precio_normal,precio_oferta,cantidad,imagen):
        self.__id = id
        self.__nombre = nombre
        self.__descripcion = descripcion
        self.__precio_normal = precio_normal
        self.__precio_oferta = precio_oferta
        self.__cantidad = cantidad
        self.__imagen = imagen
    def get_id(self):
        return self.__id
    def get_nombre(self):
        return self.__nombre
    def get_descripcion(self):
        return self.__descripcion
    def get_precio_normal(self):
        return self.__precio_normal
    def get_precio_oferta(self):
        return self.__precio_oferta
    def get_cantidad(self):
        return self.__cantidad
    def get_imagen(self):
        return self.__imagen
    def set_nombre(self,nombre):
        return self.__nombre
    def set_descripcion(self,descripcion):
        return self.__descripcion
    def set_precio_normal(self,precio_normal):
        if precio_normal > 0:
            self.__precio_normal = precio_normal
        else:
            print("La cantidad no puede ser negativa.")
    def set_precio_oferta(self,precio_oferta):
        if precio_oferta < self.__precio_normal:
            self.__precio_oferta = precio_oferta
        else:
            print("el precio de oferta no puede ser mayor que el precio normal.")
    def set_cantidad(self,cantidad):
        if cantidad >= 0:
            self.__cantidad = cantidad
        else:
            print("La cantidad de este objeto no puede ser menor a cero.")
    def set_imagen(self,imagen):
        self.__imagen = imagen
    def ver_info(self):
        print(f"ID: {self.get_id()}")
        print(f"Nombre: {self.get_nombre()}")
        print(f"Descripción: {self.get_descripcion()}")
        print(f"Precio Normal: {self.get_precio_normal()}")
        print(f"Precio Oferta: {self.get_precio_oferta()}")
        print(f"Cantidad: {self.get_cantidad()}")