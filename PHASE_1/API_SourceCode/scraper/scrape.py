import sys
import requests
import json
from bs4 import BeautifulSoup
from scraper import filter, update_db

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

# scrape for a specific scan
def scrape_scan(url):
    r = requests.get(url, headers)
    if r.status_code != 200:
        print("Error in scraping: " + url)
        return None
    
    start = r.text.find("<!-- Article Start -->")
    end   = r.text.find("<!-- Article End -->")
    article_content = r.text[start:end+1]
    soup = BeautifulSoup(article_content, "lxml").find("div", {"class":"field-item even"})
    scraped = []
    headlines = []
    
    result = soup.findAll("h3")
    for res in result:
        start_content = article_content.find(str(res))
        end_content = article_content[start_content:].find("<p> </p>")
        if end_content == -1:
            soup_content = BeautifulSoup(article_content[start_content:], "lxml").findAll("p")
            #content = ' '.join(i for i in (j.contents for j in soup_content))
            content = ""
            for i in soup_content:
                for j in i.text: #not .contents
                    content += str(j).replace('\\xa0', ' ').replace('\\', '')
                    #content += ' '
            #content = content.replace("\\xa0", " ")
            #content = content.replace("\\", "")
            pair = {"headline":str(res.text), "content":content}
        else:
            soup_content = BeautifulSoup(article_content[start_content:end_content], "lxml").findAll("p")
            #content = ' '.join(i.contents for i in (j.contents for j in soup_content))
            content = ""
            for i in soup_content:
                for j in i.text: #not .contents
                    content += str(j).replace('\\xa0', ' ').replace('\\', '')# \ , \xa0
                    #content += ' '
            #content = content.replace("\\xa0", " ")
            #content = content.replace("\\", "")
            pair = {"headline":str(res.text), "content":content}
        headlines.append(pair)
    
    articles = []
    for head in headlines:
    
        article = filter.new_article(url)
        report = filter.new_report()
        article['reports'].append(report)
        event = filter.new_event()
        report['reported_events'].append(event)
        
        article['date_of_publication'], article['headline'], article['topics'] = filter.get_metadata(r.text)
        article['headline'] += " - " + head['headline']
        article['main_text'] = head['content']
        
        event_type = filter.get_event_type(head['content']) # not scraped
        if event_type != None:
            event['type'] = event_type[0]['event-type']
            for i in range(1, len(event_type)):
                event['type'] += ", " + event_type[1]['event-type']
        else:
            event['type'] = "unknown"
        
        country = filter.get_location(head['content'])
        if country != None:
            event['location']['country'] = country[0]['name']
            event['location']['id'] = country[0]['id']
            for i in range(1, len(country)):
                event['location']['country'] += ", " + country[i]['name'] 
        else:
            event['location']['country'] = "unknown"
        
        syndrome = filter.get_syndrome(head['content'])
        if syndrome != None:
            for i in range(len(syndrome)):
                report['syndrome'].append(syndrome[i]['name'])
        #else:
            #report['syndrome'] = "unknown"
        
        disease = filter.get_disease(head['content'])
        if disease != None:
            for i in range(len(disease)):
                report['disease'].append(disease[i]['name'])
        #else:
            #report['disease'] = "unknown"
        
        filter.get_affected(scraped)
        filter.get_time(scraped)
        articles.append(article)
    
    return articles

# scrape for a specific article on CIDRAP
def scrape_article(url):
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
            scraped.append(str(s))
    
    article = filter.new_article(url)
    report = filter.new_report()
    article['reports'].append(report)
    event = filter.new_event()
    report['reported_events'].append(event)
    
    article['date_of_publication'], article['headline'], article['topics'] = filter.get_metadata(r.text)
    
    event_type = filter.get_event_type(scraped)
    if event_type != None:
        event['type'] = event_type[0]['event-type']
        for i in range(1, len(event_type)):
            event['type'] += ", " + event_type[1]['event-type']
    else:
        event['type'] = "unknown"
    
    country = filter.get_location(scraped)
    if country != None:
        event['location']['country'] = country[0]['name']
        event['location']['id'] = country[0]['id']
        for i in range(1, len(country)):
            event['location']['country'] += ", " + country[i]['name'] 
    else:
        event['location']['country'] = "unknown"
    
    syndrome = filter.get_syndrome(scraped)
    if syndrome != None:
        for i in range(len(syndrome)):
            report['syndrome'].append(syndrome[i]['name'])
    #else:
        #report['syndrome'] = "unknown"
    
    disease = filter.get_disease(scraped)
    if disease != None:
        for i in range(len(disease)):
            report['disease'].append(disease[i]['name'])
    #else:
        #report['disease'] = "unknown"
    
    filter.get_affected(scraped)
    filter.get_time(scraped)
    
    return article

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
        if "-scan-" in i:
            news += scrape_scan(host + i)
        else:
            news.append(scrape_article(host + i))
    
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
        if "-scan-" in i:
            topics.append(scrape_scan(host + i))
        else:
            topics.append(scrape_article(host + i))
    
    return topics

def get_last_page():
    r = requests.get("http://www.cidrap.umn.edu/news-perspective", headers)
    if r.status_code != 200:
        print("Error in getting last page: " + url)
        return None
    
    soup = BeautifulSoup(r.text, "lxml").find("li", {"class":"pager-last last"}).findAll("a")
    link = soup[0]['href']
    index = link.find("page=")
    return int(link[index+len("page="):])

if __name__ == "__main__":
    args = {}
    
    query = input("Scrape article (article), scan (scan) or search by news (news) or search by topics (topics): ").strip()
    if query == "article":
        link = input("Scrape for article: ").strip()
        
        result = scrape_article(link)
        print(result)
    elif query == "scan":
        link = input("Scrape for scan: ").strip()
        
        result = scrape_scan(link)
        print(result)
    elif query == "news":
        args = get_options()
        
        result = scrape_news(host + "/news-perspective", args)
        print(result)
    elif query == "topics":
        topic = input("Topic/Disease to search: ").strip()
        
        result = scrape_topics(host + "/infectious-disease-topics/" + topic + "#news")
        print(result)
