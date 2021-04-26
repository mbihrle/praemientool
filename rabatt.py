
import sys
import config
import tool_utils as tu
import sql.rabatt_u_T_PRT_AD_SVK_Praemie_Auswertungsjahr as rabatt_u_T_PRT_AD_SVK_Praemie_Auswertungsjahr

# Definition eigener Logger
log = tu.mylog('info')

#************************************************************************************************************
# Funktionen zur Tabelle T_Vertrieb_Prämie_Displayabsatz_Jahr_Auswertung in BI_Protina auf SERVSQL03
#************************************************************************************************************


def update_rabatt_auswertungsjahr(year):
    tablename = "T_PRT_AD_SVK_Praemie_Auswertungsjahr"
    tu.format_delimiter(log)
    log.info(f'Auswertungsjahr "{year}" wird in die Tabelle "{tablename}" geschrieben')
    # Parametrierte Abfrage
    sql = rabatt_u_T_PRT_AD_SVK_Praemie_Auswertungsjahr.get_sql(str(year))
    status_execution = tu.execute_sql('osdbProd', sql)
    tu.log_status_execution(status_execution)
    tu.format_delimiter(log)  





