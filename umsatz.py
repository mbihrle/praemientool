# import pyodbc
# import os
# import inspect
import sys
import config
import tool_utils as tu
from sql import umsatz_u_T_PRT_AD_Umsatz_replace_null
from sql import umsatz_u_T_PRT_AD_Umsatz_reset_all
import sql.umsatz_u_T_PRT_AD_Umsatz_Istwerte as umsatz_u_T_PRT_AD_Umsatz_Istwerte
# from sql import umsatz_u_T_PRT_AD_Umsatz_Istwerte
from sql import umsatz_u_T_PRT_AD_Umsatz_Quartalssummen
from sql import umsatz_u_T_PRT_AD_Umsatz_Jahressummen
from sql import umsatz_u_T_PRT_AD_Umsatz_Abweichungen
from sql import umsatz_u_T_PRT_AD_Umsatz_Abschluss as umsatz_u_T_PRT_AD_Umsatz_Abschluss

# Definition eigener Logger
log = tu.mylog('info')
tablename = "T_PRT_AD_Umsatz" 


def replace_Nullfields():
    tu.format_delimiter(log)
    log.info(f'Umsatztabelle "{tablename}" wird zurückgesetzt')
    # Statement-Import
    sql = umsatz_u_T_PRT_AD_Umsatz_replace_null.statement
    status_execution = tu.execute_sql('osdbProd', sql)
    tu.log_status_execution(status_execution)
    tu.format_delimiter(log)


def reset_table():
    tu.format_delimiter(log)
    log.info(f'Umsatztabelle "{tablename}" wird zurückgesetzt')
    # Statement-Import
    sql = umsatz_u_T_PRT_AD_Umsatz_reset_all.statement
    status_execution = tu.execute_sql('osdbProd', sql)
    tu.log_status_execution(status_execution)
    tu.format_delimiter(log)


def update_istumsatz(year):
    tu.format_delimiter(log)
    log.info(f'Ist-Umsatz wird in die Tabelle "{tablename}" geschrieben')
     # Parametrierte Abfrage
    sql = umsatz_u_T_PRT_AD_Umsatz_Istwerte.get_sql(str(year))
    status_execution = tu.execute_sql('osdbProd', sql)
    tu.log_status_execution(status_execution)
    tu.format_delimiter(log)


def update_summen_quartal():
    tu.format_delimiter(log)
    log.info(f'Kumulierte Monate für das Quartal werden in die Tabelle "{tablename}" geschrieben')
    # Statement-Import
    sql = umsatz_u_T_PRT_AD_Umsatz_Quartalssummen.statement
    status_execution = tu.execute_sql('osdbProd', sql)
    tu.log_status_execution(status_execution)
    tu.format_delimiter(log)


def update_summen_jahr():
    tu.format_delimiter(log)
    log.info(f'Kumulierte Monate für das Jahr in die Tabelle "{tablename}" geschrieben')
    # Statement-Import
    sql = umsatz_u_T_PRT_AD_Umsatz_Jahressummen.statement
    status_execution = tu.execute_sql('osdbProd', sql)
    tu.log_status_execution(status_execution)
    tu.format_delimiter(log)


def update_abweichung():
    tu.format_delimiter(log)
    log.info(f'Abweichungen werden in die Tabelle "{tablename}" geschrieben')
    # Statement-Import
    sql = umsatz_u_T_PRT_AD_Umsatz_Abweichungen.statement
    status_execution = tu.execute_sql('osdbProd', sql)
    tu.log_status_execution(status_execution)
    tu.format_delimiter(log)

def update_abschluss(year):
    tu.format_delimiter(log)
    log.info(f'Die Tabelle "{tablename}" wird für das Jahr {year} abgeschlossen')
    # Parametrierte Abfrage
    sql = umsatz_u_T_PRT_AD_Umsatz_Abschluss.get_sql(str(year))
    status_execution = tu.execute_sql('osdbProd', sql)
    tu.log_status_execution(status_execution)
    tu.format_delimiter(log)






