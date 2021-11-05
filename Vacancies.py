from selenium import webdriver
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
    r"https://westerncapegov.erecruit.co/candidateapp/login/"
]

def get_vacancies():
    for i in range(len(vacancies)):
                x = 0
                if vacancies[i][12:16] == "pnet" and x == 0:
                    try:
                        browser.get(vacancies[i])
                        time.sleep(2)
                        cookies = browser.find_element_by_xpath('//*[@id="ccmgt_explicit_preferences"]')
                        cookies.click()
                        cookies2 = browser.find_element_by_xpath('//*[@id="ccmgt_preferences_reject"]')
                        cookies2.click()
                        browser.switch_to.new_window('window')
                        x += 1
                    except:
                        browser.get(vacancies[i])
                        browser.minimize_window()
                        browser.switch_to.new_window('window')
                else:
                    browser.get(vacancies[i])
                    browser.minimize_window()
                    browser.switch_to.new_window('window')
get_vacancies()
