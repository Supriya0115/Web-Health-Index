#-----------------Import Dependencies----------------------------# 
# import json
import pymongo
from pymongo import MongoClient
#--------------------------------------------------------------------------------#
def mongodbset():

        #Connection for local host
        # conn = 'mongodb://localhost:27017'
        # client = pymongo.MongoClient(conn)
        # db=client.healthi_db
        
        #Connection for remote host
        # conn = 'mongodb://healthi_admin:healthisrs9=@ds255332.mlab.com:55332/healthi_db'
        # client = pymongo.MongoClient(conn,ConnectTimeoutMS=30000)
        # db = client.get_default_database()
        
        Ranks = [
                    {
                        "State": "New York",
                        "FIPS": 36000,
                        "CountyDetails":
                        [
                            {
                            
                            "FIPS": 36001,
                            "County": "Albany",
                            "Z-Score": -0.55,
                            "Rank": 8
                            },
                            {
                            "FIPS": 36003,
                            "County": "Allegany",
                            "Z-Score": 0.34,
                            "Rank": 48
                            },
                            {
                            "FIPS": 36005,
                            "County": "Bronx",
                            "Z-Score": 1.43,
                            "Rank": 62
                            },
                            {
                            "FIPS": 36007,
                            "County": "Broome",
                            "Z-Score": 0.06,
                            "Rank": 34
                            },
                            {
                            "FIPS": 36009,
                            "County": "Cattaraugus",
                            "Z-Score": 0.55,
                            "Rank": 60
                            },
                            {
                            "FIPS": 36011,
                            "County": "Cayuga",
                            "Z-Score": 0.25,
                            "Rank": 43
                            },
                            {
                            "FIPS": 36013,
                            "County": "Chautauqua",
                            "Z-Score": 0.48,
                            "Rank": 57
                            },
                            {
                            "FIPS": 36015,
                            "County": "Chemung",
                            "Z-Score": 0.39,
                            "Rank": 53
                            },
                            {
                            "FIPS": 36017,
                            "County": "Chenango",
                            "Z-Score": 0.07,
                            "Rank": 35
                            },
                            {
                            "FIPS": 36019,
                            "County": "Clinton",
                            "Z-Score": 0.21,
                            "Rank": 42
                            },
                            {
                            "FIPS": 36021,
                            "County": "Columbia",
                            "Z-Score": -0.33,
                            "Rank": 13
                            },
                            {
                            "FIPS": 36023,
                            "County": "Cortland",
                            "Z-Score": 0.04,
                            "Rank": 32
                            },
                            {
                            "FIPS": 36025,
                            "County": "Delaware",
                            "Z-Score": 0.35,
                            "Rank": 49
                            },
                            {
                            "FIPS": 36027,
                            "County": "Dutchess",
                            "Z-Score": -0.53,
                            "Rank": 9
                            },
                            {
                            "FIPS": 36029,
                            "County": "Erie",
                            "Z-Score": 0.03,
                            "Rank": 31
                            },
                            {
                            "FIPS": 36031,
                            "County": "Essex",
                            "Z-Score": -0.15,
                            "Rank": 21
                            },
                            {
                            "FIPS": 36033,
                            "County": "Franklin",
                            "Z-Score": 0.52,
                            "Rank": 59
                            },
                            {
                            "FIPS": 36035,
                            "County": "Fulton",
                            "Z-Score": 0.41,
                            "Rank": 55
                            },
                            {
                            "FIPS": 36037,
                            "County": "Genesee",
                            "Z-Score": -0.09,
                            "Rank": 27
                            },
                            {
                            "FIPS": 36039,
                            "County": "Greene",
                            "Z-Score": 0.16,
                            "Rank": 39
                            },
                            {
                            "FIPS": 36041,
                            "County": "Hamilton",
                            "Z-Score": -0.15,
                            "Rank": 20
                            },
                            {
                            "FIPS": 36043,
                            "County": "Herkimer",
                            "Z-Score": 0.39,
                            "Rank": 54
                            },
                            {
                            "FIPS": 36045,
                            "County": "Jefferson",
                            "Z-Score": 0.33,
                            "Rank": 46
                            },
                            {
                            "FIPS": 36047,
                            "County": "Kings",
                            "Z-Score": 0.38,
                            "Rank": 52
                            },
                            {
                            "FIPS": 36049,
                            "County": "Lewis",
                            "Z-Score": 0.25,
                            "Rank": 44
                            },
                            {
                            "FIPS": 36051,
                            "County": "Livingston",
                            "Z-Score": -0.13,
                            "Rank": 25
                            },
                            {
                            "FIPS": 36053,
                            "County": "Madison",
                            "Z-Score": -0.13,
                            "Rank": 23
                            },
                            {
                            "FIPS": 36055,
                            "County": "Monroe",
                            "Z-Score": -0.13,
                            "Rank": 22
                            },
                            {
                            "FIPS": 36057,
                            "County": "Montgomery",
                            "Z-Score": 0.52,
                            "Rank": 58
                            },
                            {
                            "FIPS": 36059,
                            "County": "Nassau",
                            "Z-Score": -1.17,
                            "Rank": 1
                            },
                            {
                            "FIPS": 36061,
                            "County": "New York",
                            "Z-Score": -0.34,
                            "Rank": 12
                            },
                            {
                            "FIPS": 36063,
                            "County": "Niagara",
                            "Z-Score": 0.37,
                            "Rank": 51
                            },
                            {
                            "FIPS": 36065,
                            "County": "Oneida",
                            "Z-Score": 0.19,
                            "Rank": 41
                            },
                            {
                            "FIPS": 36067,
                            "County": "Onondaga",
                            "Z-Score": -0.23,
                            "Rank": 15
                            },
                            {
                            "FIPS": 36069,
                            "County": "Ontario",
                            "Z-Score": -0.38,
                            "Rank": 11
                            },
                            {
                            "FIPS": 36071,
                            "County": "Orange",
                            "Z-Score": -0.21,
                            "Rank": 17
                            },
                            {
                            "FIPS": 36073,
                            "County": "Orleans",
                            "Z-Score": 0.47,
                            "Rank": 56
                            },
                            {
                            "FIPS": 36075,
                            "County": "Oswego",
                            "Z-Score": 0.61,
                            "Rank": 61
                            },
                            {
                            "FIPS": 36077,
                            "County": "Otsego",
                            "Z-Score": -0.21,
                            "Rank": 18
                            },
                            {
                            "FIPS": 36079,
                            "County": "Putnam",
                            "Z-Score": -0.82,
                            "Rank": 4
                            },
                            {
                            "FIPS": 36081,
                            "County": "Queens",
                            "Z-Score": -0.02,
                            "Rank": 28
                            },
                            {
                            "FIPS": 36083,
                            "County": "Rensselaer",
                            "Z-Score": -0.29,
                            "Rank": 14
                            },
                            {
                            "FIPS": 36085,
                            "County": "Richmond",
                            "Z-Score": -0.13,
                            "Rank": 24
                            },
                            {
                            "FIPS": 36087,
                            "County": "Rockland",
                            "Z-Score": -0.6,
                            "Rank": 6
                            },
                            {
                            "FIPS": 36089,
                            "County": "St. Lawrence",
                            "Z-Score": 0.35,
                            "Rank": 50
                            },
                            {
                            "FIPS": 36091,
                            "County": "Saratoga",
                            "Z-Score": -0.84,
                            "Rank": 2
                            },
                            {
                            "FIPS": 36093,
                            "County": "Schenectady",
                            "Z-Score": -0.18,
                            "Rank": 19
                            },
                            {
                            "FIPS": 36095,
                            "County": "Schoharie",
                            "Z-Score": 0.02,
                            "Rank": 30
                            },
                            {
                            "FIPS": 36097,
                            "County": "Schuyler",
                            "Z-Score": 0.31,
                            "Rank": 45
                            },
                            {
                            "FIPS": 36099,
                            "County": "Seneca",
                            "Z-Score": 0.15,
                            "Rank": 37
                            },
                            {
                            "FIPS": 36101,
                            "County": "Steuben",
                            "Z-Score": 0.16,
                            "Rank": 38
                            },
                            {
                            "FIPS": 36103,
                            "County": "Suffolk",
                            "Z-Score": -0.58,
                            "Rank": 7
                            },
                            {
                            "FIPS": 36105,
                            "County": "Sullivan",
                            "Z-Score": 0.33,
                            "Rank": 47
                            },
                            {
                            "FIPS": 36107,
                            "County": "Tioga",
                            "Z-Score": -0.1,
                            "Rank": 26
                            },
                            {
                            "FIPS": 36109,
                            "County": "Tompkins",
                            "Z-Score": -0.76,
                            "Rank": 5
                            },
                            {
                            "FIPS": 36111,
                            "County": "Ulster",
                            "Z-Score": -0.22,
                            "Rank": 16
                            },
                            {
                            "FIPS": 36113,
                            "County": "Warren",
                            "Z-Score": -0.41,
                            "Rank": 10
                            },
                            {
                            "FIPS": 36115,
                            "County": "Washington",
                            "Z-Score": 0.04,
                            "Rank": 33
                            },
                            {
                            "FIPS": 36117,
                            "County": "Wayne",
                            "Z-Score": 0.17,
                            "Rank": 40
                            },
                            {
                            "FIPS": 36119,
                            "County": "Westchester",
                            "Z-Score": -0.82,
                            "Rank": 3
                            },
                            {
                            "FIPS": 36121,
                            "County": "Wyoming",
                            "Z-Score": 0.15,
                            "Rank": 36
                            },
                            {
                            "FIPS": 36123,
                            "County": "Yates",
                            "Z-Score": 0.01,
                            "Rank": 29
                            }
                        ]
                    }
                ]
        print(Ranks)
        print(len(Ranks))        
        # #drop/create collection CR.
        # db.CountyRanksZscores.drop()
        # CR = db.CountyRanksZscores
        # #insert into CR collection
        # result = CR.insert_many(Ranks)
        # # print("Multiple States {0}".format(result.inserted_ids))        

mongodbset()
