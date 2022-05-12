import sys
from pymongo import MongoClient
import pymongo;

try:

    client = pymongo.MongoClient("mongodb+srv://smruti16:smruti@emergency.oauwo.mongodb.net/myFirstDatabase?retryWrites=true&w=majority", connect=False)
    #database
    db=client.Emergency_Record 
    collection1 = db.Patient_Data
    collection2  = db.Ambulance_Data
    print("Connected to MongoDB")
except :

    print("Database connection Error ")
    sys.exit(1)


# patient_rec1= {
#     "PatientName" : "Smruti",
#     "ContactNumber" : "017658142906",
#     "Coordinates" : {"lat":"49.42678373623796", "lon":"8.681369907812924"},
# }
#49.4072493988704, 8.668251833326691
#49.412107947674095, 8.658638796150782
#49.40775202966585, 8.676920732922824
#49.40546222547807, 8.665848574032713


ambulance_rec1 = {
    "AmbulanceNo." : "2882",
    "Coordinates": {"lat":"49.40166426601752", "lon":"8.641386827647587"},
    "Availability" : "True",
}  

#inserting data
# collection1.insert_one(patient_rec1)
collection2.insert_one(ambulance_rec1)

