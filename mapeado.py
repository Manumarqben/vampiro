import parser
import items

class Conexion:
    def __init__(self, direccion, destino):
        self.set_direccion(direccion)
        self.set_destino(destino)

    def __repr__(self):
        return self.direccion() + ' => ' + str(self.destino())

    def direccion(self):
        return self._direccion

    def set_direccion(self, direccion):
        self._direccion = direccion

    def destino(self):
        return self._destino

    def set_destino(self, destino):
        self._destino = destino

class GrupoConexiones:
    def __init__(self, iterable = None):
        self._conexiones = set()
        if iterable is not None:
            for elem in iterable:
                self.insertar(elem)

    def insertar(self, conexion):
        self._conexiones.add(conexion)

    def conecta_con(self, direccion):
        for conexion in self._conexiones:
            if conexion.direccion() == direccion:
                return conexion.destino()
        return localidad_nula

conexiones_vacio = GrupoConexiones()

class Localidad:
    def __init__(self, nombre, descripcion, conexiones = conexiones_vacio):
        self.set_nombre(nombre)
        self.set_descripcion(descripcion)
        self.set_conexiones(conexiones)

    def __repr__(self):
        return self.nombre()

    def nombre(self):
        return self._nombre

    def set_nombre(self, nombre):
        self._nombre = nombre

    def descripcion(self):
        return self._descripcion

    def set_descripcion(self, descripcion):
        self._descripcion = descripcion

    def conexiones(self):
        return self._conexiones

    def set_conexiones(self, conexiones):
        self._conexiones = conexiones

    def describir(self):
        pass

    def conecta_con(self, direccion):
        return self.conexiones().conecta_con(direccion)

    def insertar_conexion(self, conexion):
        self.conexiones().insertar(conexion)

vestibulo = Localidad(
    'VESTIBULO',
    'Estás en el vestíbulo del castillo...'
)

pasillo = Localidad(
    'PASILLO',
    'Te encuentras en medio del pasillo principal...'
)

cocina = Localidad(
    'COCINA',
    'Estás en la cocina del castillo...'
)

biblioteca = Localidad(
    'BIBLIOTECA',
    'Te hallas en la biblioteca del castillo...'
)

localidad_nula = Localidad('VACÍA', 'Localidad vacía.')

vestibulo.set_conexiones(GrupoConexiones([
    Conexion(parser.NORTE, pasillo)
]))
pasillo.set_conexiones(GrupoConexiones([
    Conexion(parser.SUR, vestibulo),
    Conexion(parser.ESTE, biblioteca),
    Conexion(parser.OESTE, cocina)
]))
biblioteca.set_conexiones(GrupoConexiones([
    Conexion(parser.OESTE, pasillo)
]))
cocina.set_conexiones(GrupoConexiones([
    Conexion(parser.ESTE, pasillo)
]))

actual = localidad_nula

"""
def describir():
    print(actual[NOMBRE])
    print(actual[DESCR])
    if actual[ITEMS] != []:
        # Visualiza la lista de ítems que hay en la localidad actual
        print('También puedes ver:')
        for item in actual[ITEMS]:
            print(item[0])
"""
