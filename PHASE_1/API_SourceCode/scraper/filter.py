import json

def read_json_list(filename):
    infile = open(filename, "r")
    data = infile.read()
    infile.close()
    return json.loads(data)

def new_report(url):
    r = {
        "url": url,
        "date_of_publication":"", #yyyy-mm-ddThh:mm:ss
        "headline":"",
        "main_text":"",
        "reports":[] # disease dictionary
    }
    
    return r

def new_disease():
    d = {
        "disease":[], # disease_list.json
        "syndrome":[], # sundrome_list.json
        "reported_events":[], # event dictionary
        "comments":""
    }

def new_event():
    e = {
        "type":"", # event_list.json
        "date":"", #yyyy-mm-ddThh:mm:ss to yyyy-mm-ddThh:mm:ss
        "location":{
            "country":"",
            "location":"",
            "geonames-id":0
        },
        "number-affected":0
    }
"""
def get_time(text, dataset):

def get_location(text, dataset):

def get_type(text, dataset):

def get_disease(text, dataset):

def get_syndrome(text, dataset):

def get_affected(text, dataset):
"""
# by 'name'
disease_list    = read_json_list("datasets/disease_list.json")
syndrome_list   = read_json_list("datasets/syndrome_list.json")
# by 'event-type'
event_list      = read_json_list("datasets/event_list.json")
# by 'month'
month_list      = read_json_list("datasets/month_list.json")
# by 'name' and 'id'
topic_list      = read_json_list("datasets/topic_list.json")
country_list    = read_json_list("datasets/country_list.json")

