# Definir una clase a elección. con 3 atributos/getters/setters
# añadir el archivo ejercicio_02.py al aread de preparacion.abs (git add <nombre_archivo>)
# Hacer un commit con una breve descripción (git commit -m "descripcion")
# Subir los cambios al repositorio remotos "fundamentos-de-python" (git push)

class Images:

    def __init__(self,id: str,scr,trigeable: bool,alpha_cn: int,xPos: int,yPos: int,isBG: bool = False):
        self.__id = id
        self.__scr = scr
        self.__trigeable = trigeable
        self.__alpha = alpha_cn
        self.__x = xPos
        self.__y = yPos
        self.__rect = None
        self.__isBG = isBG

    # -----------------------------
    # Getters
    # -----------------------------

    def get_id(self):
        return self.__id

    def get_scr(self):
        return self.__scr

    def get_trigeable(self):
        return self.__trigeable

    def get_alpha(self):
        return self.__alpha

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def get_rect(self):
        return self.__rect

    def get_subid(self):
        return self.__subid

    def get_surface_width(self):
        return self.__scr.get_width()

    def get_surface_height(self):
        return self.__scr.get_height()

    def get_size(self):
        return self._size

    def is_BG(self):
        return self.__isBG

    # -----------------------------
    # Setters
    # -----------------------------

    def set_scr(self, scr):
        self.__scr = scr

    def set_rect(self, rect):
        self.__rect = rect

    def set_x(self, x):
        self.__x = x

    def set_y(self, y):
        self.__y = y

    def set_trigeable(self, trigger):
        self.__trigeable = trigger

    def set_alpha(self, alpha):
        self.__alpha = max(0, min(255, int(alpha)))