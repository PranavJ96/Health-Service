import pymongo

from bson.json_util import dumps

client = pymongo.MongoClient("mongodb+srv://smruti16:smruti@emergency.oauwo.mongodb.net/myFirstDatabase?retryWrites=true&w=majority", connect=False)

change_stream = client.Emergency_Record.PatientRequest.watch([{

    '$match': {

        'operationType': { '$in': ['insert'] }

    }

}])

for change in change_stream:

    print(dumps(change))

    print('') # for readability only