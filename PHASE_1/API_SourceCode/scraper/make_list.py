import json, requests, sys
from bs4 import BeautifulSoup

month = [
    {"name":"January"  , "value": 1},
    {"name":"February" , "value": 2},
    {"name":"March"    , "value": 3},
    {"name":"April"    , "value": 4},
    {"name":"May"      , "value": 5},
    {"name":"June"     , "value": 6},
    {"name":"July"     , "value": 7},
    {"name":"August"   , "value": 8},
    {"name":"September", "value": 9},
    {"name":"October"  , "value": 10},
    {"name":"November" , "value": 11},
    {"name":"December" , "value": 12},
    {"name":"Jan", "value": 1},
    {"name":"Feb", "value": 2},
    {"name":"Mar", "value": 3},
    {"name":"Apr", "value": 4},
    {"name":"May", "value": 5},
    {"name":"Jun", "value": 6},
    {"name":"Jul", "value": 7},
    {"name":"Aug", "value": 8},
    {"name":"Sep", "value": 9},
    {"name":"Oct", "value": 10},
    {"name":"Nov", "value": 11},
    {"name":"Dec", "value": 12}
]
def update_list(filename, data):
    try:
        with open("datasets/" + filename + ".json", "r") as outfile:
            source = json.loads(outfile.read())
            for d in data:
                if d not in source:
                    source.append(d)
        with open("datasets/" + filename + ".json", "w") as outfile:
            json.dump(source, outfile, indent=4, sort_keys=True)
    except:
        with open("datasets/" + filename + ".json", "w") as outfile:
            json.dump(data, outfile, indent=4, sort_keys=True)


update_list("month_list", month)

headers = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5)",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "accept-charset": "ISO-8859-1,utf-8;q=0.7,*;q=0.3",
    "accept-encoding": "gzip,deflate,sdch",
    "accept-language": "en-US,en;q=0.8",
}
url = "http://www.cidrap.umn.edu/news-perspective"

country = []
topic = []
location = []

r = requests.get(url, headers)

if r.status_code != 200:
    print("Error getting: " + url)
    sys.exit()

# Getting topic (disease) names and ids
topic_start = r.text.find("<span class=\"last\">Topic</span>")
topic_end   = r.text.find("<span class=\"last\">date</span>")
topic_soup  = BeautifulSoup(r.text[topic_start:topic_end+1], "lxml")
topic_result= topic_soup.findAll("li", {"class":"leaf"})
for res in topic_result:
    t = {}
    content = str(res.contents[0])
    start_id = content.find("topics%3A")
    end_id = content.find("\" id=\"")
    t["id"] = content[start_id+len("topics%3A"):end_id]
    start_name = content.find("Apply ")
    end_name = content.find(" filter </span>")
    t["name"] = content[start_name+len("Apply "):end_name]
    if t not in topic:
        topic.append(t)
update_list("topic_list", topic)

# Getting country from country_code
country_names = {}
with open("datasets/countryInfo.txt", "r") as inf:
    country_info = inf.read().split('\n')
    for index in range(51, len(country_info)):
        if len(country_info[index]) == 0:
            continue
        entry = country_info[index].split('\t')
        country_names[entry[0]] = entry[4]

# Getting geonames_id of cities
cityfile = open("datasets/cities500.txt", "r")
geosource = cityfile.read().split('\n')
cityfile.close()
"""
geonames_id = [0]
ascii name  = [2]
alter. name = [3] with ,
country code= [9]
"""
for s in geosource:
    if len(s) == 0:
        continue
    l = {}
    i = s.split('\t')
    l['geonames_id'] = i[0]
    l['location_name'] = i[2]
    l['alternatives'] = i[3].split(',')
    l['country_code'] = i[8]
    l['country'] = country_names[i[8]]
    location.append(l)
update_list("geonames_list", location)

# Getting country names and ids
country_start= r.text.find("<span class=\"last\">country</span>")
country_end  = r.text.find("<span class=\"last\">organization</span>")
country_soup = BeautifulSoup(r.text[country_start:country_end+1], "lxml")
country_result = country_soup.findAll("li", {"class":"leaf"})
for res in country_result:
    c = {"location":[]}
    content = str(res.contents[0])
    start_id = content.find("country%3A")
    end_id = content.find("\" id=\"")
    c["id"] = content[start_id+len("country%3A"):end_id]
    start_name = content.find("Apply ")
    end_name = content.find(" filter </span>")
    c["name"] = content[start_name+len("Apply "):end_name]
    if c not in topic:
        country.append(c)
update_list("country_list", country)

