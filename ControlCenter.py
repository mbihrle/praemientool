import tkinter as tk
import os
import json
from openpyxl import load_workbook
# from openpyxl import Workbook

import tool_utils as tu
import sys
import config
import kaufkunden
import umsatz
import displayabsatz
import rabatt



class ControlCenter(tk.Frame):
    def __init__(self, parent):
        self.log = tu.mylog('info')
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.month='MM'
        self.year='YYYY'
        self.period = 'YYYYMM'
        self.initialize_user_interface()


    def initialize_user_interface(self):
        # self.root = tk.Tk()
        self.parent.title('ADM Prämienabrechnung')
        self.parent.geometry('700x500') # x-Achse x y-Achse

        #************************************************************************************************************
        # Allgemeine Steuerelemente
        #************************************************************************************************************        
        
        # self.grid_rowconfigure(1, weight=1)
        # self.grid_columnconfigure(1, weight=1)
        
        self.praemierung_label = tk.Label(self.parent, text='Prämierung\n', font='Tahoma 12 bold')
        self.praemierung_label.grid(row=0, column=0, padx='5', pady='5')
        
        self.period_label = tk.Label(self.parent, text='Periode:')
        self.period_label.grid(row=1, column=0, padx='5', pady='5', sticky='w')

        self.period_entry = tk.Entry(self.parent)
        self.period_entry.grid(row = 1, column = 0, padx='5', pady='5')
        self.period_entry.config(bg='deep sky blue')
        self.period_entry.insert(0, self.period)
        # self.period_entry.insert(0, "YYYYMM")

        self.kaufkunden_label = tk.Label(self.parent, text='Prämierung Kaufkunden\n Einzelschritte', font='Tahoma 12 bold')
        self.kaufkunden_label.grid(row=0, column=1, padx='5', pady='5')

        self.umsatz_label = tk.Label(self.parent, text='Prämierung Umsatz\n Einzelschritte', font='Tahoma 12 bold')
        self.umsatz_label.grid(row=0, column=2, padx='5', pady='5')

        self.button_open_xlprog = tk.Button(self.parent, height=2, width=30, text='Programm\nPrämien-Dokumentation', command= self.open_xlprog)
        self.button_open_xlprog.config(bg='deep sky blue')
        self.button_open_xlprog.grid(row=7, column=0, padx='5', pady='5')

        self.button_end = tk.Button(
            self.parent, height=2, width=30, text='Ende', command=self.ende)
        self.button_end.grid(row=10, column=0, padx='5', pady='5')


        #************************************************************************************************************
        # Buttons Kaufkunden
        #************************************************************************************************************

        self.button_kaufkunden_all_steps = tk.Button(
            self.parent, height=2, width=30, text='Prämierung Kaufkunden', command=self.praemierung_kaufkunden_all_steps)
        self.button_kaufkunden_all_steps.config(bg='deep sky blue')
        self.button_kaufkunden_all_steps.grid(row=2, column=0, padx='5', pady='5')

        self.button_delete_kaufkunden = tk.Button(
            self.parent, height=2, width=30, text='0) Alle Kaufkunden löschen', command=self.kaufkunden_loeschen)
        self.button_delete_kaufkunden.config(bg='firebrick1')
        self.button_delete_kaufkunden.grid(row=2, column=1, padx='5', pady='5')

        self.button_insert_kaufkunden = tk.Button(
            self.parent, height=2, width=30, text='1) Kaufkunden speichern', command=self.kaufkunden_speichern)
        self.button_insert_kaufkunden.grid(row=3, column=1, padx='5', pady='5')

        self.button_delete_kaufkunden_auszahlung = tk.Button(
            self.parent, height=2, width=30, text='2) Kaufkunden Auszahlung löschen', command=self.kaufkunden_auszahlung_loeschen)
        self.button_delete_kaufkunden_auszahlung.grid(row=4, column=1, padx='5', pady='5')

        self.button_insert_kaufkunden_auszahlung = tk.Button(
            self.parent, height=2, width=30, text='3) Kaufkunden Auszahlung speichern', command=self.kaufkunden_auszahlung_speichern)
        self.button_insert_kaufkunden_auszahlung.grid(row=5, column=1, padx='5', pady='5')        

        self.button_close_kaufkunden = tk.Button(
            self.parent, height=2, width=30, text='Jahresabschluss Kaufkunden', command=self.kaufkunden_abschluss)
        self.button_close_kaufkunden.config(bg='orange')
        self.button_close_kaufkunden.grid(row=8, column=1, padx='5', pady='5')      
        

        #************************************************************************************************************
        # Buttons Umsatz
        #************************************************************************************************************  

        self.button_umsatz_all_steps = tk.Button(
            self.parent, height=2, width=30, text='Prämierung Umsatz', command=self.praemierung_umsatz_all_steps)
        self.button_umsatz_all_steps.config(bg='deep sky blue')
        self.button_umsatz_all_steps.grid(row=3, column=0, padx='5', pady='5')

        self.button_reset_umsatz_tabelle = tk.Button(
            self.parent, height=2, width=30, text='0) Umsatz-Tabelle zurücksetzen', command=self.reset_umsatz_tabelle)
        self.button_reset_umsatz_tabelle.config(bg='firebrick1')
        self.button_reset_umsatz_tabelle.grid(row=2, column=2, padx='5', pady='5')           

        self.button_replace_umsatz_null = tk.Button(
            self.parent, height=2, width=30, text='1) Nullfelder beseitigen', command=self.replace_null)
        self.button_replace_umsatz_null.grid(row=3, column=2, padx='5', pady='5') 

        self.button_update_istumsatz = tk.Button(
            self.parent, height=2, width=30, text='2) Aktualisierung Ist-Umsatz', command=self.update_istumsatz)
        self.button_update_istumsatz.grid(row=4, column=2, padx='5', pady='5')  

        self.button_update_qsum = tk.Button(
            self.parent, height=2, width=30, text='3) Kum. Monate für Quartal', command=self.update_qsum)
        self.button_update_qsum.grid(row=5, column=2, padx='5', pady='5')                    

        self.button_update_ysum = tk.Button(
            self.parent, height=2, width=30, text='4) Kum. Monate für Jahr', command=self.update_ysum)
        self.button_update_ysum.grid(row=6, column=2, padx='5', pady='5')    

        self.button_update_deviation = tk.Button(
            self.parent, height=2, width=30, text='5) Ermittlung Abweichungen', command=self.update_deviation)
        self.button_update_deviation.grid(row=7, column=2, padx='5', pady='5') 

        self.button_close_umsatz = tk.Button(
            self.parent, height=2, width=30, text='Jahresabschluss Umsatz', command=self.umsatz_abschluss)
        self.button_close_umsatz.config(bg='orange')
        self.button_close_umsatz.grid(row=8, column=2, padx='5', pady='5')      


        #************************************************************************************************************
        # Buttons Displayabsatz
        #************************************************************************************************************  
        self.button_displayabsatz = tk.Button(
            self.parent, height=2, width=30, text='Prämierung Displayabsatz', command=self.praemierung_displayabsatz)
        self.button_displayabsatz.config(bg='deep sky blue')
        self.button_displayabsatz.grid(row=4, column=0, padx='5', pady='5')


        #************************************************************************************************************
        # Buttons Rabatt
        #************************************************************************************************************  
        self.button_rabatt = tk.Button(
            self.parent, height=2, width=30, text='Prämierung Rabatt', command=self.praemierung_rabatt)
        self.button_rabatt.config(bg='deep sky blue')
        self.button_rabatt.grid(row=5, column=0, padx='5', pady='5')


    #************************************************************************************************************
    # Allgemeine Methoden
    #************************************************************************************************************  
    def validate_period(self):
        self.period =  self.period_entry.get()
        if self.period == 'YYYYMM':
            return 'error'
        self.year = int(self.period[:4])
        self.month = int(self.period[4:])
        return 'success' 

    def error_message_period(self):
        self.log.info('Zur Prämienermittlung wurde eine ungültige Periode erfasst')
        self.log.info('Das Programm wird beendet')

    def open_xlprog(self):
        period_validation = self.validate_period()
        if period_validation == 'success':
            self.period_entry.config(bg='SeaGreen1')

            # Pfad zum Programm Prämiendokumentation relativ
            filepath_prog_rel = config.directories['xl_prog_rel']
            # Pfad zu den Optionen für Prämiendokumentation relativ
            filepath_opt_rel = config.directories['xl_prog_optionen_rel']            
            
            filepath_prog_abs = os.path.abspath(__file__ + filepath_prog_rel)
            filepath_opt_abs = os.path.abspath(__file__ + filepath_opt_rel)
            # print(f'filepath_prog_abs: {filepath_prog_abs}')
            # print(f'filepath_opt_abs: {filepath_opt_abs}')

            # Aktualisierung der Auswertungs-Periode in den Optionsdaten in config.json
            with open(filepath_opt_abs, "r") as json_file:
                json_object = json.load(json_file)

            json_object['options']['Periode:'] = self.period 
            print(json_object['options']['Periode:'])

            with open(filepath_opt_abs, "w") as json_file:
                json.dump(json_object, json_file)

            # Programmaufruf
            os.system(f'start excel.exe "{filepath_prog_abs}"')
        else:
            self.error_message_period()
            self.period_entry.config(bg='red')


    def ende(self):
        self.parent.destroy()


    # def run_test(self):
    #     period =  self.period_entry.get()
    #     year = period[:4]
    #     month = period[4:]
    #     print(f'Periode: {period}, Jahr: {year}, Monat: {month}')
    #     test(period)    

    #************************************************************************************************************
    # Methoden Kaufkunden
    #************************************************************************************************************    

    def praemierung_kaufkunden_all_steps(self):
        self.kaufkunden_speichern()
        self.kaufkunden_auszahlung_loeschen()
        self.kaufkunden_auszahlung_speichern()
        self.button_kaufkunden_all_steps.config(bg='SeaGreen1')

    def kaufkunden_loeschen(self):
        kaufkunden.delete_kaufkunden_all()

    def kaufkunden_speichern(self):
        period_validation = self.validate_period()
        if period_validation == 'success':
            self.period_entry.config(bg='SeaGreen1')
            kaufkunden.insert_kaufkunden(self.month, self.year)
        else:
            self.error_message_period()
            self.period_entry.config(bg='red')

    def kaufkunden_auszahlung_loeschen(self):
        kaufkunden.delete_kaufkunden_auszahlung()

    def kaufkunden_auszahlung_speichern(self):
        kaufkunden.insert_kaufkunden_auszahlung()

    def kaufkunden_abschluss(self):
        period_validation = self.validate_period()
        if period_validation == 'success':
            self.period_entry.config(bg='SeaGreen1')
            kaufkunden.update_kaufkunden_abschluss(self.year)
        else:
            self.error_message_period()

    #************************************************************************************************************
    # Methoden Umsatz
    #************************************************************************************************************  

    def praemierung_umsatz_all_steps(self):
        self.replace_null()
        self.update_istumsatz()
        self.update_qsum()
        self.update_ysum()
        self.update_deviation()
        self.button_umsatz_all_steps.config(bg='SeaGreen1')


    def replace_null(self):
        umsatz.replace_Nullfields()

    def reset_umsatz_tabelle(self):
        umsatz.reset_table()

    def update_istumsatz(self):
        period_validation = self.validate_period()
        if period_validation == 'success':
            self.period_entry.config(bg='SeaGreen1')
            umsatz.update_istumsatz(self.year)
        else:
            self.error_message_period()
            self.period_entry.config(bg='red')

    def update_qsum(self):
        umsatz.update_summen_quartal()

    def update_ysum(self):
        umsatz.update_summen_jahr()

    def update_deviation(self):
        umsatz.update_abweichung()

    def umsatz_abschluss(self):
        period_validation = self.validate_period()
        if period_validation == 'success':
            self.period_entry.config(bg='SeaGreen1')
            umsatz.update_abschluss(self.year)
        else:
            self.error_message_period()

    #************************************************************************************************************
    # Methoden Displayabsatz
    #************************************************************************************************************  
    def praemierung_displayabsatz(self):
        period_validation = self.validate_period()
        if period_validation == 'success':
            self.period_entry.config(bg='SeaGreen1')
            displayabsatz.update_displayabsatz_auswertung_jahr(self.year)
            self.button_displayabsatz.config(bg='SeaGreen1')
        else:
            self.error_message_period()


    #************************************************************************************************************
    # Methoden Rabatt
    #************************************************************************************************************  
    def praemierung_rabatt(self):
        period_validation = self.validate_period()
        if period_validation == 'success':
            self.period_entry.config(bg='SeaGreen1')
            rabatt.update_rabatt_auswertungsjahr(self.year)
            self.button_rabatt.config(bg='SeaGreen1')
        else:
            self.error_message_period()




