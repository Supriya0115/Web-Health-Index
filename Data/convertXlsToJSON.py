#-----------------Import Dependencies----------------------------# 
import xlrd
import csv
from glob2 import glob
import os
import pandas as pd
import json
from pymongo import MongoClient
from bson.binary import Binary
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
                sh = wb.sheet_by_name('OutcomesFactorsSubRankings') 
                CountyList = []
                if (sh != None): 

                    for row_index in range(sh.nrows):
                        HealthyCounty = {}
                        if(row_index > 2 ):
                            
                            StateName = sh.cell(row_index, 1 ).value #---unused at the moment

                            QualityofLife = { 
                                "Z-Score" : sh.cell(row_index, 3 ).value,
                                "Rank" : sh.cell(row_index, 4 ).value,
                            }   

                            HealthBehaviours = {
                                "Z-Score" : sh.cell(row_index, 5 ).value,
                                "Rank" : sh.cell(row_index, 6 ).value,
                            }                         

                            ClinicalCare = {
                                "Z-Score" : sh.cell(row_index, 7 ).value,
                                "Rank" : sh.cell(row_index, 8 ).value,
                            }

                            EconomicFactors = {
                                "Z-Score" : sh.cell(row_index, 9 ).value,
                                "Rank" : sh.cell(row_index, 10 ).value,
                            }


                            PhysicalEnvironment = { 
                                "Z-Score" : sh.cell(row_index, 11 ).value,
                                "Rank" : sh.cell(row_index, 12 ).value,
                            }


                            HealthyCounty = {
                                "CountyName" : sh.cell(row_index, 2 ).value,
                                "QualityofLife": QualityofLife,
                                "HealthBehaviours" : HealthBehaviours,
                                "ClinicalCare" : ClinicalCare,
                                "EconomicFactors" : EconomicFactors,
                                "PhysicalEnvironment" : PhysicalEnvironment
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
        jsonfile = "StateCountyData" + '.json'
        with open(jsonfile, 'w') as f:
            json.dump(StateList, f, indent = 4)

        client = MongoClient('localhost',27017) # need to find for Heroku
        db = client.Category
        Category = ["QualityofLife","EconomicFactors","ClinicalCare","HealthBehaviours","PhysicalEnvironment"]
        dropdown = {"cat" : Category }
        db.Category.drop()

        db.Category.insert(dropdown)

        db = client.State
        state = db.State
        db.State.drop()
        result = state.insert_many(StateList)
        print("Multiple States {0}".format(result.inserted_ids))
       
        for item in db.State.find():
            # if ('StateName' in item and 'Counties' in item):
            print(item)
        # db.State.find().pretty()
        
JSON_from_excel()

        



