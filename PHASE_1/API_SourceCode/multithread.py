from scraper import scrape, update_db
from threading import Thread
from datetime import datetime
import time

class historyThread(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.daemon = True
        self.start()
    def run(self):
        page = 0
        last = scrape.get_last_page()
        while page <= last:
            res = scrape.scrape_news("http://www.cidrap.umn.edu/news-perspective?page=" + str(page), [])
            if update_db.add_result(res) == False:
                break
            page += 1

class dailyThread(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.daemon = True
        self.start()
    def run(self):
        print("Start scraping")
        page = 0
        while page < 5:
            res = scrape.scrape_news("http://www.cidrap.umn.edu/news-perspective?page=" + str(page), [])
            if update_db.add_result(res) == False:
                break
            page += 1
        print("Finish scraping")
            
class checkThread(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.daemon = True
        self.start()
    def run(self):
        i = 0
        while i < 10:
            current_time = str(datetime.now())
            index = current_time.find(' ')
            if current_time[index+1:index+9] == "06:00:00":
                dailyThread()
                time.sleep(1)


