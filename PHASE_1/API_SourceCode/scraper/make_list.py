import json, requests, sys
from bs4 import BeautifulSoup

month = [
    {"month":"January"},
    {"month":"February"},
    {"month":"March"},
    {"month":"April"},
    {"month":"May"},
    {"month":"June"},
    {"month":"July"},
    {"month":"August"},
    {"month":"September"},
    {"month":"October"},
    {"month":"November"},
    {"month":"December"},
    {"month":"Jan"},
    {"month":"Feb"},
    {"month":"Mar"},
    {"month":"Apr"},
    {"month":"May"},
    {"month":"Jun"},
    {"month":"Jul"},
    {"month":"Aug"},
    {"month":"Sep"},
    {"month":"Oct"},
    {"month":"Nov"},
    {"month":"Dec"}
]
def update_list(filename, data):
    try:
        with open("datasets/" + filename + ".json", "r") as outfile:
            source = json.loads(outfile.read())
            for d in data:
                if d not in source:
                    source.append(d)
        with open("datasets/" + filename + ".json", "w") as outfile:
            json.dump(source, outfile)
    except:
        with open("datasets/" + filename + ".json", "w") as outfile:
            json.dump(data, outfile)


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
    t["name"] = content[start_name+len("Apply "):end_name+1]
    if t not in topic:
        topic.append(t)
update_list("topic_list", topic)

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
    c["name"] = content[start_name+len("Apply "):end_name+1]
    if c not in topic:
        country.append(c)
update_list("country_list", country)
