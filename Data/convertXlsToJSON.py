#-----------------Import Dependencies----------------------------# 
import xlrd
import csv
from glob2 import glob
import os
import pandas as pd
import json
#---------------------------------------------#

def JSON_from_excel():
        wb = xlrd.open_workbook('2017 County Health Rankings New Jersey DataUnFreez - v2.xls',ragged_rows = True)
        print("Hi 1 ")
        StateList = []
        if (wb != None):    
            sh = wb.sheet_by_name('Ranked Measure Data') 
            StateName = ""
            CountyList = []
            if (sh != None): 

                for row_index in range(sh.nrows):
                    HealthyCounty = {}
                    if(row_index > 2 ):
                        StateName = sh.cell(row_index, 1 ).value
                        HealthBehaviours = {
                            "PercentageSmokers" : sh.cell(row_index, 27 ).value, # 
                            "FoodEnvironmentIndex" : sh.cell(row_index, 35 ).value,
                            "DrivingDeaths" :sh.cell(row_index, 48 ).value
                        }

                        ClinicalCare = {
                            "Uninsured" : sh.cell(row_index, 62 ).value,
                            "MedicareEnrollees" : sh.cell(row_index, 79 ).value,
                            "PrimaryCarePhysicians" :sh.cell(row_index, 67 ).value
                        }

                        EconomicFactors = {
                            "GraduationRate" : sh.cell(row_index, 101 ).value,
                            "PercentageUnemployed" : sh.cell(row_index, 111 ).value,
                            "TopPercentileIncome" :sh.cell(row_index, 120 ).value
                        }

                        PhysicalEnvironment = { 
                            "AirPollution" : sh.cell(row_index, 141 ).value,
                            "WaterViolations" : sh.cell(row_index, 144 ).value,
                            "HouseholdProblems" :sh.cell(row_index, 145 ).value
                        }

                        HealthyCounty = {
                            "CountyName" : sh.cell(row_index, 2 ).value,
                            "PhysicalEnvironment": PhysicalEnvironment,
                            "EconomicFactors" : EconomicFactors,
                            "ClinicalCare" : ClinicalCare,
                            "HealthBehaviours" : HealthBehaviours
                        }

                        
                        CountyList.append(HealthyCounty)

                State = {
                            "StateName":sh.cell(row_index, 1 ).value,
                            "FIPS":sh.cell(row_index, 0 ).value,
                            "Counties" : CountyList                      
                        }
                StateList.append(State)
                print(State)
        jsonfile = StateName + '.json'
        with open(jsonfile, 'w') as f:
            json.dump(StateList, f, indent = 4)

JSON_from_excel()

        



