import time
import os
import requests
from bs4 import BeautifulSoup
import selenium
from selenium import webdriver
from datetime import date
import requests
import m3u8
import subprocess
import moviepy
from github import Github
from github import InputGitAuthor
import schedule

op = webdriver.ChromeOptions()
op.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
op.add_argument("--headless")
op.add_argument("--no-sandbox")
op.add_argument("--disable-dev-sh-usage")
driver = webdriver.Chrome(executable_path= os.environ.get("CHROMEDRIVER_PATH"),chrome_options=op)

def serial(driver):
    todays_date = date.today()
    year = todays_date.year
    month = todays_date.strftime("%B")
    day = todays_date.day
    driver = driver
    today = f"{month} {day}, {year}"
    def santh(driver):
        rep = requests.get("http://www.keralatvbox.com/?s=santh")
        soup = BeautifulSoup(rep.content, "html5lib")
        dates = soup.find('time')
        if dates.contents[0] == today:
                print("SUCCESS")
                results = soup.findAll("a", {"rel": "bookmark"}, limit=4)
                santha , santhb = results[0]['href'], results[2]['href']
                rep = requests.get(santha)
                soup = BeautifulSoup(rep.content , "html5lib")
                links = soup.findAll('iframe')
                linked = str([link['src'] for link in links]).strip("['']")
                print(linked)
                driver.get(linked)
                time.sleep(1)
                test = driver.execute_script("var performance = window.performance || window.mozPerformance || window.msPerformance || window.webkitPerformance || {}; var network = performance.getEntries() || {}; return network;")
                link = []
                for item in test:
                   if "master.m3u8" in str(item['name']):
                     m3u8 = item['name']
                     link.append(m3u8)
                santh1 = link[0]
                rep = requests.get(santhb)
                soup = BeautifulSoup(rep.content, "html5lib")
                links = soup.findAll('iframe')
                linked = str([link['src'] for link in links]).strip("['']")
                print(linked)

                driver = webdriver.Chrome()
                driver.get(linked)
                time.sleep(1)
                test = driver.execute_script(
                    "var performance = window.performance || window.mozPerformance || window.msPerformance || window.webkitPerformance || {}; var network = performance.getEntries() || {}; return network;")
                link = []
                for item in test:
                    if "master.m3u8" in str(item['name']):
                        m3u8 = item['name']
                        link.append(m3u8)
                santh2 = link[0]
                return santh2 ,santh1

    def kudu(driver):
            rep = requests.get("http://www.keralatvbox.com/?s=kudu")
            soup = BeautifulSoup(rep.content, "html5lib")
            dates = soup.find('time')
            if dates.contents[0] == today:
                print("SUCCESS")
                results = soup.findAll("a", {"rel": "bookmark"}, limit=4)
                santha, santhb = results[0]['href'], results[2]['href']
                rep = requests.get(santha)
                soup = BeautifulSoup(rep.content, "html5lib")
                links = soup.findAll('iframe')
                linked = str([link['src'] for link in links]).strip("['']")
                print(linked)
                driver.get(linked)
                time.sleep(1)
                test = driver.execute_script(
                    "var performance = window.performance || window.mozPerformance || window.msPerformance || window.webkitPerformance || {}; var network = performance.getEntries() || {}; return network;")
                link = []
                for item in test:
                    if "master.m3u8" in str(item['name']):
                        m3u8 = item['name']
                        link.append(m3u8)
                santh1 = link[0]
                rep = requests.get(santhb)
                soup = BeautifulSoup(rep.content, "html5lib")
                links = soup.findAll('iframe')
                linked = str([link['src'] for link in links]).strip("['']")
                print(linked)

                driver = webdriver.Chrome()
                driver.get(linked)
                time.sleep(1)
                test = driver.execute_script(
                    "var performance = window.performance || window.mozPerformance || window.msPerformance || window.webkitPerformance || {}; var network = performance.getEntries() || {}; return network;")
                link = []
                for item in test:
                    if "master.m3u8" in str(item['name']):
                        m3u8 = item['name']
                        link.append(m3u8)
                santh2 = link[0]
                return santh2 ,santh1

    def mou(driver):
            rep = requests.get("http://www.keralatvbox.com/?s=mou")
            soup = BeautifulSoup(rep.content, "html5lib")
            dates = soup.find('time')
            if dates.contents[0] == today:
                print("SUCCESS")
                results = soup.findAll("a", {"rel": "bookmark"}, limit=4)
                santha, santhb = results[0]['href'], results[2]['href']
                rep = requests.get(santha)
                soup = BeautifulSoup(rep.content, "html5lib")
                links = soup.findAll('iframe')
                linked = str([link['src'] for link in links]).strip("['']")
                print(linked)
                driver.get(linked)
                time.sleep(1)
                test = driver.execute_script(
                    "var performance = window.performance || window.mozPerformance || window.msPerformance || window.webkitPerformance || {}; var network = performance.getEntries() || {}; return network;")
                link = []
                for item in test:
                    if "master.m3u8" in str(item['name']):
                        m3u8 = item['name']
                        link.append(m3u8)
                santh1 = link[0]
                rep = requests.get(santhb)
                soup = BeautifulSoup(rep.content, "html5lib")
                links = soup.findAll('iframe')
                linked = str([link['src'] for link in links]).strip("['']")
                print(linked)

                driver = webdriver.Chrome()
                driver.get(linked)
                time.sleep(1)
                test = driver.execute_script(
                    "var performance = window.performance || window.mozPerformance || window.msPerformance || window.webkitPerformance || {}; var network = performance.getEntries() || {}; return network;")
                link = []
                for item in test:
                    if "master.m3u8" in str(item['name']):
                        m3u8 = item['name']
                        link.append(m3u8)
                santh2 = link[0]
                return santh2 ,santh1

    def amm(driver):
            rep = requests.get("http://www.keralatvbox.com/?s=amm")
            soup = BeautifulSoup(rep.content, "html5lib")
            dates = soup.find('time')
            if dates.contents[0] == today:
                print("SUCCESS")
                results = soup.findAll("a", {"rel": "bookmark"}, limit=4)
                santha, santhb = results[0]['href'], results[2]['href']
                rep = requests.get(santha)
                soup = BeautifulSoup(rep.content, "html5lib")
                links = soup.findAll('iframe')
                linked = str([link['src'] for link in links]).strip("['']")
                print(linked)
                driver.get(linked)
                time.sleep(1)
                test = driver.execute_script(
                    "var performance = window.performance || window.mozPerformance || window.msPerformance || window.webkitPerformance || {}; var network = performance.getEntries() || {}; return network;")
                link = []
                for item in test:
                    if "master.m3u8" in str(item['name']):
                        m3u8 = item['name']
                        link.append(m3u8)
                santh1 = link[0]
                rep = requests.get(santhb)
                soup = BeautifulSoup(rep.content, "html5lib")
                links = soup.findAll('iframe')
                linked = str([link['src'] for link in links]).strip("['']")
                print(linked)

                driver = webdriver.Chrome()
                driver.get(linked)
                time.sleep(1)
                test = driver.execute_script(
                    "var performance = window.performance || window.mozPerformance || window.msPerformance || window.webkitPerformance || {}; var network = performance.getEntries() || {}; return network;")
                link = []
                for item in test:
                    if "master.m3u8" in str(item['name']):
                        m3u8 = item['name']
                        link.append(m3u8)
                santh2 = link[0]
                return santh2 ,santh1


    def pada(driver):
        rep = requests.get("http://www.keralatvbox.com/?s=pada")
        soup = BeautifulSoup(rep.content, "html5lib")
        dates = soup.find('time')
        if dates.contents[0] == today:
            print("SUCCESS")
            results = soup.findAll("a", {"rel": "bookmark"}, limit=4)
            santha, santhb = results[0]['href'], results[2]['href']
            rep = requests.get(santha)
            soup = BeautifulSoup(rep.content, "html5lib")
            links = soup.findAll('iframe')
            linked = str([link['src'] for link in links]).strip("['']")
            print(linked)
            driver.get(linked)
            time.sleep(1)
            test = driver.execute_script(
                "var performance = window.performance || window.mozPerformance || window.msPerformance || window.webkitPerformance || {}; var network = performance.getEntries() || {}; return network;")
            link = []
            for item in test:
                if "master.m3u8" in str(item['name']):
                    m3u8 = item['name']
                    link.append(m3u8)
            santh1 = link[0]
            rep = requests.get(santhb)
            soup = BeautifulSoup(rep.content, "html5lib")
            links = soup.findAll('iframe')
            linked = str([link['src'] for link in links]).strip("['']")
            print(linked)

            driver = webdriver.Chrome()
            driver.get(linked)
            time.sleep(1)
            test = driver.execute_script(
                "var performance = window.performance || window.mozPerformance || window.msPerformance || window.webkitPerformance || {}; var network = performance.getEntries() || {}; return network;")
            link = []
            for item in test:
                if "master.m3u8" in str(item['name']):
                    m3u8 = item['name']
                    link.append(m3u8)
            santh2 = link[0]
            return santh2, santh1

    def kann(driver):
            rep = requests.get("http://www.keralatvbox.com/?s=kann")
            soup = BeautifulSoup(rep.content, "html5lib")
            dates = soup.find('time')
            if dates.contents[0] == today:
                print("SUCCESS")
                results = soup.findAll("a", {"rel": "bookmark"}, limit=4)
                santha, santhb = results[0]['href'], results[2]['href']
                rep = requests.get(santha)
                soup = BeautifulSoup(rep.content, "html5lib")
                links = soup.findAll('iframe')
                linked = str([link['src'] for link in links]).strip("['']")
                print(linked)
                driver.get(linked)
                time.sleep(1)
                test = driver.execute_script(
                    "var performance = window.performance || window.mozPerformance || window.msPerformance || window.webkitPerformance || {}; var network = performance.getEntries() || {}; return network;")
                link = []
                for item in test:
                    if "master.m3u8" in str(item['name']):
                        m3u8 = item['name']
                        link.append(m3u8)
                santh1 = link[0]
                rep = requests.get(santhb)
                soup = BeautifulSoup(rep.content, "html5lib")
                links = soup.findAll('iframe')
                linked = str([link['src'] for link in links]).strip("['']")
                print(linked)

                driver = webdriver.Chrome()
                driver.get(linked)
                time.sleep(1)
                test = driver.execute_script(
                    "var performance = window.performance || window.mozPerformance || window.msPerformance || window.webkitPerformance || {}; var network = performance.getEntries() || {}; return network;")
                link = []
                for item in test:
                    if "master.m3u8" in str(item['name']):
                        m3u8 = item['name']
                        link.append(m3u8)
                santh2 = link[0]
                return santh2 ,santh1

    try:
     santh1 , santh2 = santh(driver)
    except : santh1 , santh2 = "NONE ", "NONE"
    try:
     kudu1 , kudu2 = kudu(driver)
    except : kudu1 , kudu2 = "NONE ", "NONE"
    try:
     mou1 , mou2 = mou(driver)
    except : mou1 , mou2 = "NONE ", "NONE"
    try:
     pada1 , pada2 = pada(driver)
    except : pada1 , pada2 = "NONE ", "NONE"
    try:
     kann1 , kann2 = kann(driver)
    except : kann1 , kann2 = "NONE ", "NONE"
    try:
      amm1 , amm2 = amm(driver)
    except : amm1 , amm2 = "NONE ", "NONE"

    save = str(    "#EXTM3U" + "\n" +
                   "#EXTINF:-1,Santhwanam1"+ "\n" +
                   f"{santh1}" +  "\n" +
                   "#EXTINF:-2,Santhwanam2" + "\n" +
                   f"{santh2}" + "\n" +
                   "#EXTINF:-3,Kudumbavilakku1" + "\n" +
                   f"{kudu1}" + "\n" +
                   "#EXTINF:-4,Kudumbavilakku2" + "\n" +
                   f"{kudu2}" + "\n" +
                   "#EXTINF:-5,Mounaragam1" + "\n" +
                   f"{mou1}" + "\n" +
                   "#EXTINF:-6,Mounaragam2" + "\n" +
                   f"{mou2}" + "\n" +
                   "#EXTINF:-7,Padathapainkili1" + "\n" +
                   f"{pada1}" + "\n" +
                   "#EXTINF:-8,Padathapainkili2" + "\n" +
                   f"{pada2}"+ "\n" +
                   "#EXTINF:-9,KannanteRadha1" + "\n" +
                   f"{kann1}" + "\n" +
                   "#EXTINF:-10,KannanteRadha2" + "\n"
                   f"{kann2}" + "\n" 
                   "#EXTINF:-11,Amma Ariyathe1" + "\n" +
                   f"{amm1}" + "\n" +
                   "#EXTINF:-12,Amma Ariyathe2" + "\n"
                   f"{amm2}" + "\n" )

    file_path = "iptv"
    g = Github("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")
    repo = g.get_repo("CRyptoWIZARDS222/IPTV")

    data = save

    def push(path, message, content, branch, update=False):
        author = InputGitAuthor(
            "CRyptoWIZARDS222",
            "cryptowizardsofficial@gmail.com"
        )
        source = repo.get_branch("main")
        contents = repo.get_contents(path, ref=branch)  # Retrieve old file to get its SHA and path
        repo.update_file(contents.path, message, content, contents.sha, branch=branch, author=author)  # Add, commit and push branch

    push(file_path, "Add", data, "main", update=True)
    print("DONE")

schedule.every(10).minutes.do(serial(driver))

while True:
    schedule.run_pending()
    time.sleep(60) # wait one minute
