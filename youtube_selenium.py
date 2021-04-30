#Dependencies/Prerequisites
#pip install webdriver-manager
#pip install selenium
#latest firefox browser

from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
firefox_profile = webdriver.FirefoxProfile()
firefox_profile.set_preference("browser.privatebrowsing.autostart", True)

while(True):
    input_string=input("Enter song name here: ")
    if len(input_string)<=2 or input_string.isdigit()==True:
        print('Please type the song name properly')
    else: 
        break
   


while(True):
    download_type=input('''
     Type '1' for mp3 format
     Type '2' for mp4 format
     ''')
    if str(download_type)=='1' or str(download_type)=='2':
         break
    else:
       print("Input must be 1 or 2")
    
        


browser = webdriver.Firefox(executable_path=GeckoDriverManager().install(),firefox_profile=firefox_profile)
browser.get("https://www.youtube.com/")
browser.maximize_window()
browser.implicitly_wait(3)

element = browser.find_element_by_css_selector(".style-scope:nth-child(1) > #items > .style-scope:nth-child(3) > #endpoint .title") # opens subscriptions
element.click()
time.sleep(2) # wait for page to load before finding it
searchelement = browser.find_element_by_css_selector('input#search') # search bar

#here if statement
if download_type=='2':
    searchelement.send_keys(str(input_string) + " full video song")
else:
    searchelement.send_keys(str(input_string) + " full song lyrics")
    
searchelement.submit()
browser.find_element_by_css_selector("yt-icon.ytd-searchbox").click()


browser.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]/div').click()
curr_str=browser.current_url
time.sleep(2)
browser.get('https://ytmp3.cc/en13/')
time.sleep(3)

#here if statment for mp4
if download_type=='2':
    browser.find_element_by_css_selector('#mp4').click()
else:
    pass

input_element=browser.find_element_by_css_selector('#input')
input_element.send_keys(curr_str)
input_element.submit()

wait = WebDriverWait(browser, 90)
element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#buttons > a:nth-child(1)')))
time.sleep(2)
element.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/div[3]/a[1]').click()
