import sys
import config
import tool_utils as tu
import sql.displayabsatz_u_T_Vertrieb_Prämie_Displayabsatz_Jahr_Auswertung as displayabsatz_u_T_Vertrieb_Prämie_Displayabsatz_Jahr_Auswertung

# Definition eigener Logger
log = tu.mylog('info')

#************************************************************************************************************
# Funktionen zur Tabelle T_Vertrieb_Prämie_Displayabsatz_Jahr_Auswertung in BI_Protina auf SERVSQL03
#************************************************************************************************************


def update_displayabsatz_auswertung_jahr(year):
    tablename = "T_Vertrieb_Prämie_Displayabsatz_Jahr_Auswertung"
    tu.format_delimiter(log)
    log.info(f'Auswertungsjahr "{year}" wird in die Tabelle "{tablename}" geschrieben')
    # Parametrierte Abfrage
    sql = displayabsatz_u_T_Vertrieb_Prämie_Displayabsatz_Jahr_Auswertung.get_sql(str(year))
    status_execution = tu.execute_sql('bi_protina', sql)
    tu.log_status_execution(status_execution)
    tu.format_delimiter(log)  





