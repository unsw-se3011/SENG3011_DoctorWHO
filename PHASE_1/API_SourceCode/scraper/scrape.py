import sys
import requests
import json
from bs4 import BeautifulSoup
import filter

"""
News scan + year + page number=> scrape for latest dates
b.delaney@unsw.edu.au
"""

# spoof some headers so the request appears to be coming from a browser, not a bot
headers = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5)",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "accept-charset": "ISO-8859-1,utf-8;q=0.7,*;q=0.3",
    "accept-encoding": "gzip,deflate,sdch",
    "accept-language": "en-US,en;q=0.8",
}

host = "http://www.cidrap.umn.edu"

# scrape for a specific article on CIDRAP
def scrape_link(url):
    r = requests.get(url, headers)
    if r.status_code != 200:
        print("Error in scraping: " + url)
        return None
    
    start = r.text.find("<!-- Article Start -->")
    end   = r.text.find("<!-- Article End -->")
    
    soup = BeautifulSoup(r.text[start:end+1], "lxml")
    scraped = []
    
    result = soup.find("div", {"class":"field-item even"}).findAll("p")
    for res in result:
        for s in res.contents:
            scraped.append(s)
    
    return scraped

# read in options/criteria/filters to search/filter
def get_options():
    options = {}
    
    content_type = input("Content type (scan, ss_news[article]): ").strip()
    if len(content_type) > 0:
        options["type"] = content_type
    
    topic = input("Topic (disease id): ").strip()
    if len(topic) > 0:
        options["topic"] = topic
    
    year = input("Date (in year): ").strip()
    if len(year) > 0:
        options["year"] = year
    
    place = input("Country: ").strip()
    if len(place) > 0:
        options["country"] = place
    
    org = input("Organisation (in id): ").strip()
    if len(org) > 0:
        options["organization"] = org
    
    return options

# take cidrap home url
# and dictionary of options
def scrape_news(url, options):
    query = "?"
    count = 0
    for i in options:
        # content type (scan or article)
        if i == "type":
            query += "f[" + str(count) + "]=type%3A" + options[i] + "&"
            count += 1
            continue
        # topic (by id)
        if i == "topic":
            query += "f[" + str(count) + "]=field_related_topics%3A" + options[i] + "&"
            count += 1
            continue
        # date (in year)
        if i == "year":
            query += "f[" + str(count) + "]=field_date%3A" + options[i] + "&"
            count += 1
            continue
        # country
        if i == "country":
            query += "f[" + str(count) + "]=field_country%3A" + options[i] + "&"
            count += 1
            continue
        # organisation (by id)
        if i == "organization":
            query += "f[" + str(count) + "]=field_organization%3A" + options[i] + "&"
            count += 1
            continue
        
    r = requests.get(url + query, headers)
    if r.status_code != 200:
        print("Error in getting news from: " + url + query)
        return None
    
    soup = BeautifulSoup(r.text, "lxml")
    searches = []
    news = []
    
    result = soup.find("div", {"class":"view-content"}).findAll("a")
    for res in result:
        if res['href'] not in searches:
            searches.append(res['href'])
    
    for i in searches:
        news.append(scrape_link(host + i))
    
    return news
    
# search for specific topic/disease
def scrape_topics(url):
    r = requests.get(url, headers)
    if r.status_code != 200:
        print("Error in getting topics from: " + url)
        return None
    
    soup = BeautifulSoup(r.text, "lxml")
    searches = []
    topics = []
    
    result = soup.find("div", {"class":"view-content"}).findAll("a")
    for res in result:
        if res['href'] not in searches:
            searches.append(res['href'])
    
    for i in searches:
        topics.append(scrape_link(host + i))
    
    return topics

if __name__ == "__main__":
    args = {}
    
    query = input("Scrape a link (scrape) or search by news (news) or search by topics (topics): ").strip()
    if query == "scrape":
        link = input("Scrape for link: ").strip()
        
        result = scrape_link(link)
        print(result)
    elif query == "news":
        args = get_options()
        
        result = scrape_news(host + "/news-perspective", args)
        print(result)
    elif query == "topics":
        topic = input("Topic/Disease to search: ").strip()
        
        result = scrape_topics(host + "/infectious-disease-topics/" + topic + "#news")
        print(result)
