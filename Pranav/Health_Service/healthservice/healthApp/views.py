
from asyncio.windows_events import NULL
from django.shortcuts import render
from turtle import distance
import geocoder
from googleplaces import GooglePlaces, types
from pymongo import MongoClient
from operator import itemgetter
from geopy.geocoders import Nominatim
from bson.json_util import dumps
from threading import Thread
class Hospitals:
    def __init__(self):
        # Use your own API key for making api request calls
        API_KEY = 'AIzaSyCvbG9yfqQbs9NG0nCxz4bIduFxpSPyph4'
        # Initialising the GooglePlaces constructor
        self.google_places = GooglePlaces(API_KEY)
        g = geocoder.ip('me')
        self.client = MongoClient("mongodb+srv://user:QkSR7FzEQXs2hX0Y@emergencyservice.16zhn.mongodb.net/myFirstDatabase?retryWrites=true&w=majority", connect=False)
        # Create the database
        db = self.client['EmergencyService']  
        # Create the Collection
        self.collection = db['SOS_Request']
            
        self.latitude = g.latlng[0] #current latitude of the user
        self.longitude = g.latlng[1] #current longitude of the user
    def searchNearByHospitals(self):
        import redis
        redis = redis.Redis(
            host= 'localhost',
            port= '6379')
            
        self.nearbyHospitalList = []
        redis.flushdb() #Use this to flush all data.
        # call the function nearby search with
        # the parameters as longitude, latitude,
        # radius and type of place which needs to be searched 
        query_result = self.google_places.nearby_search(
                lat_lng ={'lat': self.latitude, 'lng': self.longitude},
                radius = 5000,
                types =[types.TYPE_HOSPITAL])

        # If any attributions related
        # with search results print them
        if query_result.has_attributions:
            print (query_result.html_attributions)

        # Add the current geo location
        redis.geoadd("Hospitals",[(float)(self.longitude),(float)(self.latitude),"Current"])
        # Iterate over the search results
        for place in query_result.places:
            redis.geoadd("Hospitals",[(float)(place.geo_location['lng']),(float)(place.geo_location['lat']),place.name])
            dist = redis.geodist("Hospitals","Current",place.name,"km")
            temp = {"name":place.name,"distance":(str)(dist)+" Kms","lat":(float)(place.geo_location['lat']),"lon":(float)(place.geo_location['lng']),"link":"https://www.google.com/maps/search/?api=1&query="+(str)(place.geo_location['lat'])+"%2C"+(str)(place.geo_location['lng'])}
            self.nearbyHospitalList.append(temp)

    def sendSOS(self):
            import redis
            redis = redis.Redis(
                host= 'localhost',
                port= '6379')
            redis.flushdb() #Use this to flush all data.
            query_result = self.google_places.nearby_search(
                    lat_lng ={'lat': self.latitude, 'lng': self.longitude},
                    radius = 5000,
                    types =[types.TYPE_HOSPITAL])

            # If any attributions related
            # with search results print them
            if query_result.has_attributions:
                print (query_result.html_attributions)
            self.nearbyHospitalList= []
            # Add the current geo location
            redis.geoadd("Hospitals",[(float)(self.longitude),(float)(self.latitude),"Current"])
            for place in query_result.places:
                redis.geoadd("Hospitals",[(float)(place.geo_location['lng']),(float)(place.geo_location['lat']),place.name])
                dist = redis.geodist("Hospitals","Current",place.name,"km") 
                temp = {"name":place.name,"distance":(str)(dist)+" Kms","link":"https://www.google.com/maps/search/?api=1&query="+(str)(place.geo_location['lat'])+"%2C"+(str)(place.geo_location['lng'])}
                self.nearbyHospitalList.append(temp)
            self.nearbyHospitalList = sorted(self.nearbyHospitalList, key=itemgetter('distance'))

            # calling the nominatim tool
            geoLoc = Nominatim(user_agent="GetLoc")

            # passing the coordinates
            currentlocation = (str)(self.latitude)+', '+(str)(self.longitude)
            locname = geoLoc.reverse(currentlocation)
            mydict = { "lattitude": self.latitude, "longitude": self.longitude,"address":locname.address,"location": "https://www.google.com/maps/search/?api=1&query="+(str)(self.latitude)+"%2C"+(str)(self.longitude),"nearByHospitals":self.nearbyHospitalList}
            self.collection.insert_one(mydict)


    def getNearbyHospitals(self):
        self.nearbyHospitalList = sorted(self.nearbyHospitalList, key=itemgetter('distance'))
        return self.nearbyHospitalList
        
def index(request):
    return render(request, 'home.html')
def list(request):
    obj = Hospitals()
    obj.searchNearByHospitals()
    return render(request, 'list.html',{'data':obj.getNearbyHospitals()})
def sos(request):
    obj1 = Hospitals()
    obj1.sendSOS()
    return render(request, 'sos.html')