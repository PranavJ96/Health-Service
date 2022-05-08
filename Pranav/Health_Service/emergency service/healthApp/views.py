import pymongo
from django.shortcuts import render
from bson.json_util import dumps
client = pymongo.MongoClient("mongodb+srv://Pranav:FraleGipvvP6JzHk@emergencyservice.16zhn.mongodb.net/myFirstDatabase?retryWrites=true&w=majority", connect=False)

def index(request):
    change_stream = client.EmergencyService.SOS_Request.watch([{
    '$match': {
        'operationType': { '$in': ['insert'] }
    }
    }])
    for change in change_stream:
        print(dumps(change))
        print('') # for readability only
    return render(request, 'home.html')