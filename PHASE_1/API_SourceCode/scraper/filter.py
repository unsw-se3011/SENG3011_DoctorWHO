import json
from bs4 import BeautifulSoup

def read_json_list(filename):
    with open(filename) as f:
        j = json.load(f)
    return j

# end/beginning of words
stoppers = [' ', ',', '.', '?', '!', '\n', '\t', ')', '(', '\'', '\"', ':']
blacklist= ['Of', 'Lab', 'See', 'Republic', 'Congress', 'East', 'West', 'South', 'North']

# by 'name'
disease_list    = read_json_list("scraper/datasets/disease_list.json")
syndrome_list   = read_json_list("scraper/datasets/syndrome_list.json")
month_list      = read_json_list("scraper/datasets/month_list.json")
# by 'event-type'
event_list      = read_json_list("scraper/datasets/event_list.json")
# by 'name' and 'id'
topic_list      = read_json_list("scraper/datasets/topic_list.json")
country_list    = read_json_list("scraper/datasets/geonames_list.json")

def new_article(url):
    a = {
        #"id": 0,
        "url": url,
        "date_of_publication":"", #yyyy-mm-ddThh:mm:ss
        "headline":"",
        "main_text":"",
        "topics":[], # extra stuff, can be referenced to disease
        "reports":[] # disease dictionary
    }

    return a

def new_report():
    r = {
        #"id": 0,
        "disease":[], # disease_list.json
        "syndrome":[], # syndrome_list.json
        "reported_events":[], # event dictionary
        "comment":""
    }

    return r

def new_event():
    e = {
        #"id": 0,
        "type":"", # event_list.json
        "date":"", #yyyy-mm-ddThh:mm:ss to yyyy-mm-ddThh:mm:ss
        "location":{
            "country":"", # country_list.json
            "location":"",
            "geonames-id":0,
            "id":0 # for reference to CIDRAP source
        },
        "number-affected":0
    }

    return e

def get_time(text):
    #print("\nGetting time")
    content = ' '.join(t for t in text)

    count_month = 0
    for m in month_list:
        if m['name'] in content:
            count_month += 1
            #print(m['name'] + " found")
    #print(str(count_month) + " times months appear\n")

    content = content.lower()
    time_sets = ["week", "weeks", "day", "days", "month", "months", "year", "years"]

    count_set = 0
    for t in time_sets:
        if t in content:
            count_set += 1
            #print(t + " found")
    #print(str(count_set) + " times time_sets appear\n")

def convert_time(string):
    s = string.split(' ')
    month = ""
    for m in month_list:
        if m['name'] == s[0]:
            month = str(m['value']).zfill(2)
            break
    date = s[1][:2]
    year = s[2]
    return year + "-" + month + "-" + date + "T00:00:00"

def get_affected(text):
    content = ' '.join(t for t in text)
    # extract just numbers (positive integers)
    numbers = [int(s) for s in content.split() if s.isdigit()]
    #print("\nNumbers for affected:")
    #print(numbers)

def get_metadata(text):
    date = ""
    headline = ""
    topics = []

    header_start = text.find("<a id=\"main-content\"></a>")
    header_end = text.find("<!-- Article Start -->")
    soup = BeautifulSoup(text[header_start:header_end], "lxml")
    headline = BeautifulSoup(text, "lxml").find("title").text
    try:
        date = soup.find("span", {"class":"date-display-single"})['content'][:19]
    except:
        if " Scan " in headline and " for " in headline:
            date = convert_time(headline[headline.find(" for") + len(" for "):])
    try:
        result = soup.find("div", {"class":"fieldlayout-inline fieldlayout node-field-filed_under"}).findAll("a")
    except:
        result = soup.find("div", {"class":" fieldlayout-inline fieldlayout node-field-filed_under"}).findAll("a")
    for res in result:
        for c in res.contents:
            if "Stewardship" not in c:
                topics.append(c)

    return date, headline[:headline.find(" | CIDRAP")], topics

def get_location(text):
    content = ' '.join(t for t in text)
    ending = content.find("See also:")
    if ending > 0:
        content = content[:ending]
    #content = content.lower()
    location = []
    print(type(country_list))
    for d in range(len(country_list)):
        l = {}
        ctry_names = []
        ctry_names.append(country_list[d]['location_name'])
        ctry_names += country_list[d]['alternatives']
        for i in range(len(ctry_names)):
            if ctry_names[i] == "" or ctry_names[i] in blacklist:
                continue
            #if ctry_names[i].lower() in content:
            name_index = content.find(ctry_names[i])
            while name_index > 0:
                prev = -1
                next = -1
                if name_index > 0:
                    prev = content[name_index - 1]
                if name_index + len(ctry_names[i]) < len(content):
                    next = content[name_index + len(ctry_names[i])]
                if (prev == -1 or prev in stoppers) and (next in stoppers or next == -1):
                    #print("Found(" + str(d) + "): " + ctry_names[i] + " --- " + country_list[d]['location_name'])
                    l['name'] = country_list[d]['location_name']
                    l['geonames'] = country_list[d]['geonames_id']
                    l['country'] = country_list[d]['country']
                    if l not in location:
                        location.append(l)
                name_index = content[name_index:].find(ctry_names[i])
            """
            if ctry_names[i] in content:
                print("Found(" + str(d) + "): " + ctry_names[i] + " --- " + country_list[d]['location_name'])
                l['name'] = country_list[d]['location_name']
                l['geonames'] = country_list[d]['geonames_id']
                l['country'] = country_list[d]['country']
                if l not in location:
                    location.append(l)
            """
        """
        if d['location_name'].lower() in content:
            print(d)
            l['name'] = d['location_name']
            l['geonames'] = d['geonames_id']
            l['country'] = d['country']
            if l not in location:
                location.append(l)
        """
    if len(location) > 0:
        return location

    return None

def get_event_type(text):
    content = ' '.join(t for t in text)
    content = content.lower()
    event = []
    for e in event_list:
        if e['event-type'].lower() in content:
            if e not in event:
                event.append(e)

    if len(event) > 0:
        return event

    return None

def get_disease(text):
    content = ' '.join(t for t in text)
    content = content.lower()
    disease = []
    for d in disease_list:
        if d['name'] == 'other' or d['name'] == 'unknown':
            continue
        if d['name'].lower() in content:
            disease.append(d)

    if len(disease) > 0:
        return disease

    return None

def get_syndrome(text):
    content = ' '.join(t for t in text)
    content = content.lower()
    syndrome = []
    for s in syndrome_list:
        if s['name'] == 'other' or s['name'] == 'unknown':
            continue
        if s['name'].lower() in content:
            syndrome.append(s)

    if len(syndrome) > 0:
        return syndrome

    return None
