from scraper import scrape

if __name__ == "__main__":
    args = {}
    
    query = input("Scrape article (article), scan (scan) or search by news (news) or search by topics (topics): ").strip()
    if query == "article":
        link = input("Scrape for article: ").strip()
        
        result = scrape.scrape_article(link)
        print(result)
    elif query == "scan":
        link = input("Scrape for scan: ").strip()
        
        result = scrape.scrape_scan(link)
        print(result)
    elif query == "news":
        args = get_options()
        
        result = scrape.scrape_news(host + "/news-perspective", args)
        print(result)
    elif query == "topics":
        topic = input("Topic/Disease to search: ").strip()
        
        result = scrape.scrape_topics(host + "/infectious-disease-topics/" + topic + "#news")
        print(result)
