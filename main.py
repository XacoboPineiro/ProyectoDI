import conexionBD

if __name__ == '__main__':
    baseDatos = conexionBD.ConexionBD("modelosClasicos.dat")
    print(baseDatos.consultaSenParametros("Select * from CLIENTES"))
    # baseDatos.insertarRexistro("insert into CLIENTES values ('4', 'Xacobo', 'Piñeiro Cacableos', '986554775', 'calle',
    #                                                          'Vigo', 'Pontevedra', '36547', 'España', '1')")
    # print(baseDatos.consultaSenParametros("Select * from CLIENTES"))
    baseDatos.modificarRexistros("update CLIENTES set axenteComercial = '2' where numeroCliente = '1'")
    print(baseDatos.consultaSenParametros("Select * from CLIENTES"))
