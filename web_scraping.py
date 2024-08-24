import bs4
from selenium import webdriver
import pandas as pd
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import hashlib
import time

chrome_options = Options()

driver = webdriver.Chrome(options=chrome_options)

job_list = ['Python Developer', 'Java Developer', 'Web Developer', 'Database Administrator', 'Security Analyst', 'Project Manager', 'Frontend Developer'
            'Network Administrator', 'Software Developer']


resume_links = pd.DataFrame()
category = []

for job in job_list:
    JOB = job.lower()
    for i in range(1,2):   # INCREASE THE RANGE TO GET MORE RESUME DATA
        PAGE = str(i)
        URL = "https://www.livecareer.com/resume-search/search?jt=" + JOB + "&bg=85&eg=100&comp=&mod=&pg=" + PAGE
        # print(URL)
        driver.get(URL)
        aTagsInLi_list = driver.find_elements(By.CSS_SELECTOR, "a.sc-1dzblrg-0")
        for a in aTagsInLi_list:
            category.append(JOB)
            href = a.get_attribute('href')

resume_links["Category"] = category

resume_links.Category.value_counts()

resume_links["Resume"] = ""

for i in range(resume_links.shape[0]):
    url = resume_links.link[i]
    driver.get(url)
    # print(url)
    time.sleep(0.5)
    x = driver.page_source
    x = x.replace(">", "> ")
    soup = bs4.BeautifulSoup(x, 'html.parser')
    # Search for a specific tag
    div = soup.find("div", class_="document")

    resume_links.Raw_html[i] = div
    try:
        if div is not None:
            resume_links.Resume[i] = div.text
        else:
            print("Div with id 'document' not found in the HTML source.")
    except Exception as err:
        print("some error occurred: ", err)

resume_links.head()
resume_links.to_csv("Resume.csv", index=False)
