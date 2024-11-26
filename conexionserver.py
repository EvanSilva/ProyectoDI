from datetime import datetime

import mysql.connector
from mysql.connector import Error


class ConexionServer():
    def crear_conexion(self):

        try:
            conexion = mysql.connector.connect(
            host='192.168.10.66', # Cambia esto a la IP de tu servidor user='dam', # Usuario creado
            #host='192.168.1.49',
            user='dam',
            password='dam2425',
            database='bbdd',
            charset="utf8mb4",
            collation="utf8mb4_general_ci"  # Asegúrate de que aquí esté configurado
            # Contraseña del usuario database='bbdd' # Nombre de la base de datos
            )
            if conexion.is_connected():
                pass
                #print("Conexión exitosa a la base de datos")
            return conexion
        except Error as e:
            print(f"Error al conectar a la base de datos: {e}")
            return None
        return None

    @staticmethod
    def listaProv(self=None):
        listaprov = []
        conexion = ConexionServer().crear_conexion()
        if conexion:
            try:
                cursor = conexion.cursor()
                cursor.execute("SELECT * FROM provincias")
                resultados = cursor.fetchall()
                for fila in resultados:
                    listaprov.append(fila[1])  # Asumiendo que el nombre de la provincia está en la segunda columna
                cursor.close()
                conexion.close()
            except Error as e:
                print(f"Error al ejecutar la consulta: {e}")
        return listaprov

    @staticmethod
    def listaMuniProv(provincia):
        try:
            conexion = ConexionServer().crear_conexion()
            listamunicipios = []
            cursor = conexion.cursor()
            cursor.execute(
                "SELECT * FROM municipios WHERE idprov = (SELECT idprov FROM provincias WHERE provincia = %s)",
                (provincia,)
            )
            resultados = cursor.fetchall()
            for fila in resultados:
                listamunicipios.append(fila[1])  # Asumiendo que el nombre de la provincia está en la segunda columna
            cursor.close()
            conexion.close()
            return listamunicipios
        except Exception as error:
            print("error lista muni", error)

    def listadoClientes(self):
        try:
            conexion = ConexionServer().crear_conexion()
            listadoclientes = []
            cursor = conexion.cursor()
            cursor.execute("SELECT dnicli, altacli, apelcli, nomecli, dircli, emailcli, movilcli, provcli, municli, bajacli FROM clientes ORDER BY apelcli, nomecli ASC")
            resultados = cursor.fetchall()
            for fila in resultados:      # Procesar cada fila de los resultados y crea una lista con valores de la fila
                listadoclientes.append(list(fila))  # Convierte la tupla en una lista y la añade a listadoclientes
            cursor.close()    # Cerrar el cursor y la conexión si no los necesitas más
            conexion.close()
            return listadoclientes
        except Exception as e:
            print("error listado en conexion", e)

    def altaCliente(cliente):
        try:
            conexion = ConexionServer().crear_conexion()
            if conexion:
                cursor = conexion.cursor()
                query = """
                INSERT INTO clientes (dnicli, altacli, apelcli, nomecli, dircli, emailcli, movilcli, provcli, municli)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                """
                cursor.execute(query, cliente)          # Ejecutar la consulta pasando la lista directamente
                conexion.commit()  # Confirmar la transacción
                cursor.close()   # Cerrar el cursor y la conexión
                conexion.close()
                return True
        except Error as e:
            print(f"Error al insertar el cliente: {e}")

    def bajaCliente(dni):
        try:
            # Crear conexión
            conexion = ConexionServer().crear_conexion()
            if conexion:
                cursor = conexion.cursor()
                query = """
                UPDATE clientes
                SET bajacli = %s
                WHERE dnicli = %s
                """
                bajahoy = datetime.now().strftime("%d/%m/%Y")
                cursor.execute(query, (bajahoy, dni))
                conexion.commit()
                cursor.close()
                conexion.close()
                return True
        except Error as e:
            print(f"Error al dar de baja el cliente: {e}")
            return False

    def modifCliente(cliente):

        try:
            conexion = ConexionServer().crear_conexion()
            if conexion:
                cursor = conexion.cursor()
                query = """
                UPDATE clientes
                SET altacli = %s, apelcli = %s, nomecli = %s, emailcli = %s, movilcli = %s,
                    dircli = %s, provcli = %s, municli = %s, bajacli = %s
                WHERE dnicli = %s
                """
                cursor.execute(query, cliente)
                conexion.commit()
                cursor.close()
                conexion.close()
                return True
        except Error as e:
            print(f"Error al modificar el cliente: {e}")
            return False

    def datosOneCliente(dni):
        registro = []  # Inicializa la lista para almacenar los datos del cliente
        try:
            conexion = ConexionServer().crear_conexion()
            if conexion:
                cursor = conexion.cursor()
                # Definir la consulta de selección
                query = '''SELECT * FROM clientes WHERE dnicli = %s'''
                cursor.execute(query, (dni,))
                # Recuperar los datos de la consulta
                for row in cursor.fetchall():
                    registro.extend([str(col) for col in row])
            return registro

        except Exception as e:
            print("Error al obtener datos de un cliente:", e)
            return None  # Devolver None en caso de error





 # PROPIEDADES ---------------------------------------------------------------------------------------






    def listadoPropiedades(self):
        try:
            conexion = ConexionServer().crear_conexion()
            listadoclientes = []
            cursor = conexion.cursor()
            cursor.execute("SELECT codigo, altaprop, bajaprop, dirprop, provprop, muniprop, tipoprop, habprop, banprop, superprop, prealquiprop, prevenprop, cpprop, obserprop, tipooper, estadoprop, nomeprop, movilprop FROM propiedades ORDER BY codigo")
            resultados = cursor.fetchall()
            for fila in resultados:
                listadoclientes.append(list(fila))
            cursor.close()
            conexion.close()
            return listadoclientes
        except Exception as e:
            print("error listado en conexion", e)


    def datosOnePropiedad(id):
        registro = []
        try:
            conexion = ConexionServer().crear_conexion()
            if conexion:
                cursor = conexion.cursor()
                query = '''SELECT * FROM propiedades WHERE codigo = %s'''
                cursor.execute(query, (id,))
                for row in cursor.fetchall():
                    registro.extend([str(col) for col in row])
            return registro

        except Exception as e:
            print("Error al obtener datos de una propiedad:", e)
            return None  # Devolver None en caso de error

    def altaProp(cliente):
        try:
            conexion = ConexionServer().crear_conexion()
            if conexion:
                cursor = conexion.cursor()
                query = """
                INSERT INTO propiedades (codigo, altaprop, bajaprop, dirprop, provprop, muniprop, tipoprop, habprop, banprop, superprop, prealquiprop, prevenprop, cpprop, obserprop, tipooper, estadoprop, nomeprop, movilprop)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """
                cursor.execute(query, cliente)
                conexion.commit()
                cursor.close()
                conexion.close()
                return True
        except Error as e:
            print(f"Error al insertar el cliente: {e}")

    def cargarTipoprop():
        registro = []
        try:
            conexion = ConexionServer().crear_conexion()
            if conexion:
                cursor = conexion.cursor()
                query = '''SELECT tipo FROM tipopropiedad'''
                cursor.execute(query)
                for row in cursor.fetchall():
                    registro.extend([str(col) for col in row])
            return registro

        except Exception as e:
            print("Error al obtener datos de un cliente:", e)
            return None  # Devolver None en caso de error

