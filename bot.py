from selenium import webdriver
import time
options = webdriver.ChromeOptions()
options.binary_location = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe"
driver = webdriver.Chrome('C:/Users/user/Documents/bot/chromedriver', chrome_options=options)

url='http://example.org/'
server_id='100'
player_id='25cd0237-bf47-429c-a05e-7ea2e1931f10'
iteration=''
times=0
def runBot(url, server_id, player_id, iteration, times):
    driver.get(url+'?server_id='+server_id+'&player_uuid='+player_id+iteration)
    time.sleep(35)
    if times==5:
        runBot(url, server_id, player_id, iteration + '-', 0)
    else:
        runBot(url, server_id, player_id, iteration, times+1)

runBot(url, server_id, player_id, iteration,times)