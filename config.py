directories = dict(
    app='../'
    # , xl_prog_absolute='P:\\Marketing&Vertrieb\\4_Controlling\\01_ADM_Prämierung\\Programm_Praemierung\\Programm_Dokumentation_Excel\\Programm_Praemien_Doku.xlsm'
    # , xl_prog_optionen_absolute='P:\\Marketing&Vertrieb\\4_Controlling\\01_ADM_Prämierung\\Programm_Praemierung\\Programm_Dokumentation_Excel\\Programm_Optionen.xlsx'
    , xl_prog_rel="/../../Programm_Dokumentation_Excel/Programm_Praemien_Doku.xlsm"
    #, xl_prog_optionen_rel="/../../Programm_Dokumentation_Excel/Programm_Optionen.xlsx"
    , xl_prog_optionen_rel="/../../Programm_Dokumentation_Excel/config.json"
)


system_files = dict(
    infolog = '../info.log'
)



#*********************************
# Für Datenbank
#*********************************

db_connections = dict(
    osdbProd = """
        Driver={SQL Server};
        Server=serv-gusdb;
        Database=osdbProd;
        Trusted_Connection=yes;""",
    bi_protina = """
        Driver={SQL Server};
        Server=servsql03;
        Database=BI_Protina;
        Trusted_Connection=yes;"""
)



