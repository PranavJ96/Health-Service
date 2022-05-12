from multiprocessing.sharedctypes import Value
import sys
from bson import ObjectId
from pymongo import MongoClient
import pymongo;
from bson.json_util import dumps
import redis



redis = redis.Redis(
host= 'localhost',
port= '6379')
redis.flushdb() #Use this to flush all data.
#service : list of Ambulance data(folder name)
#patient: data name(data name)


try:
    client = pymongo.MongoClient("mongodb+srv://smruti16:smruti@emergency.oauwo.mongodb.net/myFirstDatabase?retryWrites=true&w=majority", connect=False)
    #database
    change_stream = client.Emergency_Record.Patient_Data.watch([{

    '$match': {

        'operationType': { '$in': ['insert'] }

    }

    }])

    for change in change_stream:
        print(change)
        redis.geoadd("Service",[(float)(change['fullDocument']['Coordinates']['lon']),(float)(change['fullDocument']['Coordinates']['lat']),"Patient"])
        print('') # for readability only
        data=client.Emergency_Record.Ambulance_Data.find({"Availability" : "True"})
        for i in data:
            print(i)
            redis.geoadd("Service",[(float)(i.get('Coordinates').get('lon')),(float)(i.get('Coordinates').get('lat')),(str)(i.get('_id'))])

        # print(redis.georadius("Service",8.65597413022748,49.41330512376113,5,"km",True))
        list=redis.georadius("Service",change['fullDocument']['Coordinates']['lon'],change['fullDocument']['Coordinates']['lat'],5,"km",True)
        print(list) #printing the list of nearby ambulances
        oneoutput = sorted(list, key=lambda x: x[1])
        print(oneoutput) #sorting the ambulances as per the kmsm       
        print((str)(oneoutput[1][0])[2:-1])
        selectedAmbulanceData=client.Emergency_Record.Ambulance_Data.find_one({"_id" : ObjectId((str)(oneoutput[1][0])[2:-1])})
        print(selectedAmbulanceData)
        EmergencyRecord= {
            "PatientName" : change['fullDocument']['PatientName'],
            "ContactNumber" : change['fullDocument']['ContactNumber'],
            "Coordinates" : change['fullDocument']['Coordinates'],
            "AmbulanceNo": selectedAmbulanceData.get('AmbulanceNo.')
        }
        client.Emergency_Record.History.insert_one(EmergencyRecord)
            
        query = { "_id": ObjectId((str)(oneoutput[1][0])[2:-1]) }
        newvalues = { "$set": { "Availability": "False" } }
        client.Emergency_Record.Ambulance_Data.update_one(query, newvalues)

except :

    print("Database connection Error ")
    sys.exit(1)













 


