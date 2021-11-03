from selenium import webdriver
from selenium.webdriver.common import action_chains
from selenium.webdriver.common import actions
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.actions import key_actions

import time

browser = webdriver.Chrome(executable_path=r"C:\Program Files (x86)\Chromedriver\chromedriver2.exe")

vacancies = [
    r"https://za.indeed.com/jobs?q=CIMA&l=",
    r"https://za.indeed.com/jobs?q=python+advanced+excel&l=",
    r"https://za.indeed.com/jobs?q=&l=Mosselbaai%2C+Western+Cape",
    r"https://za.indeed.com/jobs?q=&l=George%2C+Western+Cape",
    r"https://www.pnet.co.za/5/job-search-detailed.html?where=george&radius=50&searchOrigin=Resultlist_top-search",
    r"https://www.pnet.co.za/5/job-search-detailed.html?where=knysna&radius=50&searchOrigin=Resultlist_top-search",
    r"https://www.pnet.co.za/5/job-search-detailed.html?where=mosselbay&radius=50&searchOrigin=Resultlist_top-search",
    r"https://www.pnet.co.za/5/job-search-detailed.html?what=advanced%20excel%20python&searchOrigin=Resultlist_top-search",
    r"https://za.indeed.com/jobs?q=work%20from%20home%20online&l=Western%20Cape",
    r"https://www.amazon.jobs/en/landing_pages/aws-south-africa",
    r"https://westerncapegov.erecruit.co/candidateapp/login/",
    r"https://www.beaufortwestmun.co.za/current-opportunities"
]

def Vacancies():
    for i in range(len(vacancies)):
        browser.execute_script("window.open('');")
        kids = browser.window_handles
        browser.switch_to_window(kids[-1])
        browser.get(vacancies[i])

Vacancies()


