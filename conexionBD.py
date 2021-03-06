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
        self.conexion = dbapi.connect(self.rutaBd)
        self.cursor = self.conexion.cursor()

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

    def consultaConParametros(self, tab, campo,  *parametros):
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
                    if campos is None
                        sql = "SELECT * FROM " + tab + " "
                    else:
                        sql = "SELECT "
                        for campo in campos:
                            sql = sql + campo + ", "
                        sql = sql[:-2]
                        sql = sql + " FROM " + tab + " "
                    if parametros != None
                        sql = sql + "WHERE "
                        for clave in parametros.keys():
                            sql = sql + clave + "=?. "
                        sql = sql[-2]

                    print(sql)

                    self.cursor.execute(consultaSQL, parametros)

                    for fila in self.cursor.fetchall():
                        listaConsulta.append(fila)

        except dbapi.DatabaseError as e:
            print("Erro facendo a consulta: " + str(e))
            return None
        else:
            print("Consulta executada")
            return listaConsulta

    def insertarRexistro(self, tab, val):

        try:
            if self.conexion is None:
                print("Creando consulta: É necesario realizar a conexión a base de datos previamente")
            else:
                if self.cursor is None:
                    print("Creando consulta: É necesario realizar a creación do cursor previamente")
                else:
                    print("Insertando en tabla", tab, "con valores", val)
                    consulta = "INSERT INTO "+tab+" VALUES ('4', 'Xacobo', 'Piñeiro Cacableos', '986554775', 'calle', 'Vigo', 'Pontevedra', '36547', 'España', '1')"
                    self.cursor.execute(consulta, val)

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
