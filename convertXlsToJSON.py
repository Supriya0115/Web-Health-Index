#-----------------Import Dependencies----------------------------# 
import xlrd
import csv
from glob2 import glob
import os
import pandas as pd
import json
from pymongo import MongoClient
from bson.binary import Binary
import pickle
#----------------------------------------------------------------#

def JSON_from_excel():
        filePath = ""
        xlsFilesOnly = glob(filePath+"*.xls")# parse all xls file(s) only
        StateList = []
        for xlsfile in xlsFilesOnly:
            # xlsfilename = xlsfile.split(" ") # get the year of the file
            # year = xlsfilename[0]
            yearReported = xlsfile[:4]
            wb = xlrd.open_workbook(xlsfile,ragged_rows = True)
            
            if (wb != None):    
                sh = wb.sheet_by_name('Ranked Measure Data') 
                CountyList = []
                if (sh != None): 

                    for row_index in range(sh.nrows):
                        HealthyCounty = {}
                        if(row_index > 2 ):
                            
                            StateName = sh.cell(row_index, 1 ).value #---unused at the moment
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

                            County = {
                                "County" : HealthyCounty
                            }
                            
                            CountyList.append(County)
                    if(row_index == sh.nrows - 1):
                        State = {
                                    "StateName":StateName,
                                    "Year" : yearReported,
                                    "FIPS":sh.cell(row_index, 0 ).value,
                                    "Counties" : CountyList                      
                                }
                        StateList.append(State)
                        # print(State)
        jsonfile = "StateData" + '.json'
        with open(jsonfile, 'w') as f:
            json.dump(StateList, f, indent = 4)

        client = MongoClient('localhost',27017)
        db = client.Category
        Category = ["PhysicalEnvironment","EconomicFactors","ClinicalCare","HealthBehaviours"]
        dropdown = {"cat" : Category }
        db.Category.drop()

        db.Category.insert(dropdown)

        db = client.State
        state = db.State
        db.State.drop()
        result = state.insert_many(StateList)
        print("Multiple States {0}".format(result.inserted_ids))
        # result.save(filename="test.mongodb")
        thebytes = pickle.dumps(StateList)
        state.insert({'bin-data': Binary(thebytes)})
        print("test 1")
        for item in db.State.find():
            if ('StateName' in item and 'Counties' in item):
                print(item)
        # db.State.find().pretty()
        
JSON_from_excel()

        



