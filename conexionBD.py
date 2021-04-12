import sqlite3 as dbapi


class ConexionBD:
    """
        Clase para realizar a conexión a una base de datos SQlite.
    """

    def __init__(self, rutabd):
        """
        Crea as propiedades e as inicializa
        :param rutabd: Ruta onde se encontra o ficheiro da base de datos SQlite
        """
        self.rutaBd = rutabd
        self.conexion = None
        self.cursor = None

        """
        Codigo que crea a conexión da base de datos.
        Para realizar a conexión precisa da ruta onde está a base de datos.
        """

        try:
            if self.conexion is None:
                if self.rutaBd is None:
                    print("A ruta da base de datos é: None ")
                else:
                    self.conexion = dbapi.connect(self.rutaBd)
            else:
                print("Base de datos conectada: " + self.conexion)

        except dbapi.StandardError as e:
            print("Erro o facer a conexión a base de datos " + self.rutaBd + ": " + e)
        else:
            print("Conexión de base de datos realizada")

        """
        Codigo que crea o cursor da base de datos.
        Para realizar o cursor precísase previamente da conexión da BD, que crea a conexión a base de
        datos na ruta dada.
        """

        try:
            if self.conexion is None:
                print("Creando o cursor: É necesario realizar a conexión a base de datos previamente")
            else:
                if self.cursor is None:
                    self.cursor = self.conexion.cursor()
                else:
                    print("O cursor xa esta inicializado: " + self.cursor)

        except dbapi.Error as e:
            print(e)
        else:
            print("Cursor preparado")

    def consultaSenParametros(self, consultaSQL):
        """
            Retorna unha lista cos rexistros dunha consulta realizada sen pasarlle parámetros.
            :param consultaSQL. Código da consulta sql a executar
            :return listaConsulta
        """

        listaConsulta = list()
        try:
            if self.conexion is None:
                print("Creando consulta: É necesario realizar a conexión a base de datos previamente")
            else:
                if self.cursor is None:
                    print("Creando consulta: É necesario realizar a creación do cursor previamente")
                else:
                    self.cursor.execute(consultaSQL)

                    for fila in self.cursor.fetchall():
                        listaConsulta.append(fila)

        except dbapi.DatabaseError as e:
            print("Erro facendo a consulta: " + str(e))
            return None
        else:
            print("Consulta executada")
            return listaConsulta

    def consultaConParametros(self, consultaSQL, *parametros):
        """
        Retorna unha lista cos rexistros dunha consulta realizada pasandolle os parámetros.
        A consulta ten que estar definida con '?' na clausula where de SQL.

        :param consultaSQL. Código da consulta sql a executar
        :param *parametros. Lista de parámetros para introducir na consulta
        :return listaConsulta
        """

        listaConsulta = list()
        try:
            if self.conexion is None:
                print("Creando consulta: É necesario realizar a conexión a base de datos previamente")
            else:
                if self.cursor is None:
                    print("Creando consulta: É necesario realizar a creación do cursor previamente")
                else:
                    self.cursor.execute(consultaSQL, parametros)

                    for fila in self.cursor.fetchall():
                        listaConsulta.append(fila)

        except dbapi.DatabaseError as e:
            print("Erro facendo a consulta: " + str(e))
            return None
        else:
            print("Consulta executada")
            return listaConsulta

    def insertarRexistro(self, consultaSQL):

        try:
            if self.conexion is None:
                print("Creando consulta: É necesario realizar a conexión a base de datos previamente")
            else:
                if self.cursor is None:
                    print("Creando consulta: É necesario realizar a creación do cursor previamente")
                else:
                    self.cursor.execute(consultaSQL)
                    self.conexion.commit()

        except dbapi.DatabaseError as e:
            print("Erro facendo a insercion: " + str(e))
            return None
        else:
            print("Insercion executada")

    def modificarRexistros(self, consultaSQL):

        try:
            if self.conexion is None:
                print("Creando consulta: É necesario realizar a conexión a base de datos previamente")
            else:
                if self.cursor is None:
                    print("Creando consulta: É necesario realizar a creación do cursor previamente")
                else:
                    self.cursor.execute(consultaSQL)
                    self.conexion.commit()

        except dbapi.DatabaseError as e:
            print("Erro facendo a actualizacion: " + str(e))
            return None
        else:
            print("Actualizacion executada")
