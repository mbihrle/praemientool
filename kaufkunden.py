# import pyodbc
# import os
# import logging
import sys
import config
import tool_utils as tu
import sql.kaufkunden_i_T_PRT_AD_SVK_Praemie_Kaufkunden as kaufkunden_i_T_PRT_AD_SVK_Praemie_Kaufkunden
# from sql import kaufkunden_i_T_PRT_AD_SVK_Praemie_Kaufkunden
from sql import kaufkunden_d_T_PRT_AD_SVK_Praemie_Kaufkunden
import sql.kaufkunden_u_T_PRT_AD_SVK_Praemie_Kaufkunden as kaufkunden_u_T_PRT_AD_SVK_Praemie_Kaufkunden
# from sql import kaufkunden_u_T_PRT_AD_SVK_Praemie_Kaufkunden
from sql import kaufkunden_i_T_PRT_AD_SVK_Praemie_Kaufkunden_Auszahlung
from sql import kaufkunden_d_T_PRT_AD_SVK_Praemie_Kaufkunden_Auszahlung

# Definition eigener Logger
log = tu.mylog('info')

#************************************************************************************************************
# Funktionen zur Tabelle T_PRT_AD_SVK_Praemie_Kaufkunden
#************************************************************************************************************

def delete_kaufkunden_all():
    tablename = "T_PRT_AD_SVK_Praemie_Kaufkunden"
    tu.format_delimiter(log)
    log.info(f'Alle Kaufkunden werden aus Tabelle "{tablename}" gelöscht')
    # Statement-Import
    sql = kaufkunden_d_T_PRT_AD_SVK_Praemie_Kaufkunden.statement
    status_execution = tu.execute_sql('osdbProd', sql)
    tu.log_status_execution(status_execution)
    tu.format_delimiter(log)  


def insert_kaufkunden(month, year):
    tablename = "T_PRT_AD_SVK_Praemie_Kaufkunden"
    tu.format_delimiter(log)
    log.info(f'Kaufkunden werden in die Tabelle "{tablename}" geschrieben')
    # Parametrierte Abfrage
    sql = kaufkunden_i_T_PRT_AD_SVK_Praemie_Kaufkunden.get_sql(str(month), str(year))
    status_execution = tu.execute_sql('osdbProd', sql)
    tu.log_status_execution(status_execution)
    tu.format_delimiter(log)


def update_kaufkunden_abschluss(year):
    tablename = "T_PRT_AD_SVK_Praemie_Kaufkunden"
    tu.format_delimiter(log)
    log.info(f'Kaufkunden werden in der Tabelle "{tablename}" für das Jahr {year} als prämiert abgeschlossen')
    # Parametrierte Abfrage
    sql = kaufkunden_u_T_PRT_AD_SVK_Praemie_Kaufkunden.get_sql(str(year))
    status_execution = tu.execute_sql('osdbProd', sql)
    tu.log_status_execution(status_execution)
    tu.format_delimiter(log)       

#************************************************************************************************************        
# Funktionen zur Tabelle PRT_AD_SVK_Praemie_Kaufkunden_Auszahlung
#************************************************************************************************************

def delete_kaufkunden_auszahlung():
    tablename = "T_PRT_AD_SVK_Praemie_Kaufkunden_Auszahlung"
    tu.format_delimiter(log)
    log.info(f'Auswertungsdaten der Tabelle "{tablename}" werden gelöscht')
    # Statement-Import
    sql = kaufkunden_d_T_PRT_AD_SVK_Praemie_Kaufkunden_Auszahlung.statement
    status_execution = tu.execute_sql('osdbProd', sql)
    tu.log_status_execution(status_execution)
    tu.format_delimiter(log)     
 

def insert_kaufkunden_auszahlung():
    tablename = "T_PRT_AD_SVK_Praemie_Kaufkunden_Auszahlung"
    tu.format_delimiter(log)
    log.info(f'Kaufkunden werden in die Tabelle "{tablename}" geschrieben')
    # Statement-Import
    sql = kaufkunden_i_T_PRT_AD_SVK_Praemie_Kaufkunden_Auszahlung.statement
    status_execution = tu.execute_sql('osdbProd', sql)
    tu.log_status_execution(status_execution)
    tu.format_delimiter(log)     









