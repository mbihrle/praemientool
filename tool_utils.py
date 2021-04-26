
import pyodbc
import logging
import config
import inspect
import sys

loggers = {}

def mylog(name):
    global loggers

    if loggers.get(name):
        return loggers.get(name)
    else:
        logFormatter = logging.Formatter(
            "%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s")
        logger = logging.getLogger()
        fileHandler = logging.FileHandler(
            "{0}/{1}.log".format(config.directories['app'], 'info'))
        fileHandler.setFormatter(logFormatter)
        logger.addHandler(fileHandler)
        consoleHandler = logging.StreamHandler()
        consoleHandler.setFormatter(logFormatter)
        logger.addHandler(consoleHandler)
        logger.setLevel(logging.DEBUG)

        loggers[name] = logger

        return logger

def format_delimiter(log, print_count=1, sign='+', sign_length=100):
    output_string = sign_length * sign
    for _ in range(0, print_count):
        log.info(output_string)


def execute_sql(connection_name, sql):
    try:
        conn_string = config.db_connections[connection_name]
        conn = pyodbc.connect(conn_string)
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
        conn.close()
        return 'success'
    except:
        conn.close()
        return 'error'


def log_status_execution(status_execution):
    # # infos running functions
    # running_module = __name__
    # running_function = inspect.stack()[0][3]

    # infos calling functions
    frame_records = inspect.stack()[1]
    calling_module = inspect.getmodulename(frame_records[1])
    calling_function = inspect.stack()[1][3]

    if status_execution == 'success':
         log.info(f'Funktion \"{calling_module}.{calling_function}\" erfolgreich abgeschlossen.')
    else:

        # log.info(f'Funktion \"{__name__}.{inspect.stack()[1][3]}\" mit Fehler abgebrochen.')
        log.info(f'Funktion \"{calling_module}.{calling_function}\" mit Fehler abgebrochen.')



log = mylog('info')


