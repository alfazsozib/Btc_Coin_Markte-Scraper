from typing import Counter
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Fun for webdriver
def web_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("no-sandbox")
    options.add_argument('--dns-prefetch-disable')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    prefs = {"profile.managed_default_content_settings.images": 2}
    options.add_experimental_option("prefs", prefs)
    options.add_argument("--disable-extensions")
    return webdriver.Chrome(executable_path='./chromedriver.exe')

# Data Scraper
def data_scrape():
    driver = web_driver()
    url = 'https://www.coingecko.com/en/coins/bitcoin#markets'
    driver.get(url)  
    all_data = []
    count = 100
    
    while True:
        time.sleep(3)
        try:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            driver.find_element_by_link_text('Show More').click()
            count += 100
            time.sleep(5)
        except:
            break   

    try:  
        exchange = driver.find_elements_by_xpath('//*[@id="spot"]/div/div[1]/div[2]/table/tbody[2]/tr/td[2]/div/a')
    except:
        pass
    try:    
        pair = driver.find_elements_by_xpath('//*[@id="spot"]/div/div[1]/div[2]/table/tbody[2]/tr/td[3]/a')
    except:
        pass
    try:    
        price = driver.find_elements_by_xpath('//*[@id="spot"]/div/div[1]/div[2]/table/tbody[2]/tr/td[4]')
    except:
        pass
    try:     
        spread = driver.find_elements_by_xpath('//*[@id="spot"]/div/div[1]/div[2]/table/tbody[2]/tr/td[5]')
    except:
        pass
    try:
        depth = driver.find_elements_by_xpath('//*[@id="spot"]/div/div[1]/div[2]/table/tbody[2]/tr/td[6]')    
    except:
        pass
    try:    
        minus_depth = driver.find_elements_by_xpath('//*[@id="spot"]/div/div[1]/div[2]/table/tbody[2]/tr/td[7]') 
    except:
        pass
    try:    
        vol_24 = driver.find_elements_by_xpath('//*[@id="spot"]/div/div[1]/div[2]/table/tbody[2]/tr/td[8]')    
    except:
        pass
    try:    
        volume = driver.find_elements_by_xpath('//*[@id="spot"]/div/div[1]/div[2]/table/tbody[2]/tr/td[9]')
    except:
        pass
    try:
        last_trade = driver.find_elements_by_xpath('//*[@id="spot"]/div/div[1]/div[2]/table/tbody[2]/tr/td[10]')
    except:
        # last_trade = ''
        pass
        
    for i in range(1,len(last_trade)):

        data = {
            'Exchange':exchange[i].text,
            'Pair': pair[i].text,
            'Price':price[i].text,
            'Spread':spread[i].text,
            '+2% Depth':depth[i].text,
            '-2% Depth': minus_depth[i].text,
            '24h Volume':vol_24[i].text,
            'Volume %':volume[i].text,
            'Last Trade':last_trade[i].text,
            }
        
        all_data.append(data)
        print('Scraping Running')
        print(len(exchange))

        df = pd.DataFrame(all_data)
        df.to_csv('btc_coin_market.csv') 

        
        
        # while True:
        #     time.sleep(3)
        #     if driver.find_element_by_link_text('Show More'):
        #         driver.find_element_by_link_text('Show More').click()
        #         count += 100
        #     else:
        #         break    

              
    df = pd.DataFrame(all_data)
    print('<---------------Scraping Completed------------->')
    df.to_csv('btc_coin_market.csv')          
                
    

if __name__=='__main__':
    data_scrape()
    









    links = driver.find_elements_by_xpath('//*[@id="video-title"]')
    title = driver.find_elements_by_xpath('//*[@id="video-title"]')

    for i in links:
        print(i.get_attribute('href'))
