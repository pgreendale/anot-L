from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
options = Options()
options.headless = True

import winsound
import time
winsound.Beep(2000,500)
counter = 0; 
while(1):
    print('Test Nr:', counter)
    driver = webdriver.Firefox(options=options)
    driver.get("https://tnv.leipzig.de/tnv/?START_OFFICEGROUP=Gruppe_KFZ_Zulassung")
    assert "Terminverwaltung" in driver.title
    elem = driver.find_element_by_name("AGREEMENT_ACCEPT")
    elem.send_keys(Keys.SPACE)
    elem = driver.find_element_by_name("ACTION_INFOPAGE_NEXT")
    elem.send_keys(Keys.RETURN)
    time.sleep(1)
    driver.find_element_by_xpath("//button[contains(text(),' Kfz-Zulassungsbehörde')]").click()
    driver.find_element_by_xpath("//button[contains(text(),'Termin vereinbaren')]").click()
    # dropdown menu for 1 Ummeldung
    driver.find_element_by_name("1229610692").send_keys("1")
    driver.find_element_by_xpath("//button[contains(text(),'Weiter')]").click()
    # next page
    driver.find_element_by_xpath("//button[contains(text(),'Weiter')]").click()
    # listing elements
    days = driver.find_elements_by_xpath("//div[@class='ekolCalendarFreeTimeContainer']")
    print('Days found: ',len(days))
    match = False
    for day in days:
            test = day.get_attribute('innerHTML')
            print(test)
            if (test != '0 frei'):
                winsound.Beep(1000,500)
                not match 
                break
    if match :
        print('Free date found, aborting')
        break #while loop
    
    else:
        print('No free dates found')
        winsound.Beep(500,500)
        counter = counter + 1
        driver.quit()
        #wait 5 min 
        time.sleep(500) 
#driver.close()
