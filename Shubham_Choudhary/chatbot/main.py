import re
import sys
from tkinter import messagebox
import random_responses
from pymongo import MongoClient
import requests
import json

url = "https://covid-19-live-vaccination-finder.p.rapidapi.com/locations/list-avail-vax-man"



querystring = {"med_name":"Janssen, COVID-19 Vaccine, 0.5 mL"}
headers = {

    "X-RapidAPI-Host": "covid-19-live-vaccination-finder.p.rapidapi.com",

    "X-RapidAPI-Key": "98c3102b95msh4e77551bd3b9ca9p14b4fcjsn572f0dbd4eab"

}
responseVaccines = requests.request("GET", url, headers=headers, params=querystring)
try:

    client = MongoClient(port=27017)

    db=client.Chatbot

    print("Connected to MongoDB")
  
    col = db["intents"]

except :

    print("Database connection Error ")

    print("No connection could be made because the target machine actively refused it ")

    messagebox.showerror("Error", "Connection Error")

    sys.exit(1)




# Store JSON data
cursor= col.find()
docs=list(cursor)
response_data =  docs
def get_response(input_string):
    split_message = re.split(r'\s+|[,;?!.-]\s*', input_string.lower())
    score_list = []

    # Check all the responses
    for response in response_data:
        response_score = 0
        required_score = 0
        showVaccineCount = 0
        required_words = response["required_words"]
        
        test = ['vaccine','center']
        # Check if there are any required words
        if required_words:
            for word in split_message:
                for i in test:
                    if word == i:
                        showVaccineCount += 1
                if word in required_words:
                    required_score += 1

        # Amount of required words should match the required score
        if showVaccineCount == 2:
            for i in json.loads(responseVaccines.text):
                print(i)
                print("\n\n\n")
            showVaccineCount = 0
            return "Here is the list"
        if required_score == len(required_words):
            # print(required_score == len(required_words))
            # Check each word the user has typed
            for word in split_message:
                # If the word is in the response, add to the score
                if word in response["user_input"]:
                    response_score += 1

        # Add score to list
        score_list.append(response_score)
        # Debugging: Find the best phrase
        # print(response_score, response["user_input"])

    # Find the best response and return it if they're not all 0
    best_response = max(score_list)
    response_index = score_list.index(best_response)

    # Check if input is empty
    if input_string == "":
        return "Please type something so we can chat :("

    # If there is no good response, return a random one.
    if best_response != 0:
        return response_data[response_index]["bot_response"]

    return random_responses.random_string()
    

while True:
    user_input = input("You: ")
    print("Bot:", get_response(user_input))

    
