from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
from ordered_set import OrderedSet
import pandas as pd
import random


# Open Chrome browser incognito with Selenium and get the page


options = Options()
options.headless = True
options.add_argument("--incognito")
driver = webdriver.Chrome('/usr/bin/chromedriver', chrome_options=options)
driver.get("PAGE_URL")


# Here we need 3 types of data in every post: date, text and post url


post_texts = OrderedSet([])
post_dates = OrderedSet([])
post_urls = OrderedSet([])


def get_text_and_date(url):
    driver.get(url)
    text = []
    ps = driver.find_elements_by_xpath('//p')
    for p in ps:
        text.append(p.text)

    print("TEXT: ", text)

    date = driver.find_element_by_xpath('//abbr').text
    return [text, date]



try:

# Range of 150 is how many times our browser scrolls the page down

    for i in range(150):
            #texts = driver.find_elements_by_xpath('//div[@class="story_body_container"]/div[@class="_5rgt _5nk5 _5msi"]')
            #dates = driver.find_elements_by_xpath("//div[@class='story_body_container']/header/div/div/div/div/div[@data-sigil='m-feed-voice-subtitle']/a/abbr")
        urls = driver.find_elements_by_xpath("//div[@class='story_body_container']/header/div/div/div/div/div[@class='_52jc _5qc4 _78cz _24u0 _36xo']/a[@href]")
        
        for url in urls:
            post_urls.add(url.get_attribute('href'))


        print("SCROLL...", i)
        print("URLS LEN: ", len(post_urls))



        html_page = driver.find_element_by_tag_name('html')
        html_page.send_keys(Keys.END)
        time.sleep(random.random())

except: print(error)
finally:


    posts = []
    try:
        for url in post_urls:
                data = get_text_and_date(url)
                post = ((data[1], data[0], url))
                posts.append(post)
                time.sleep(random.random())
    except: print("ERROR IN PARSE!")
    finally:
        df = pd.DataFrame(posts, columns=['date', 'text', 'url'])
        df.to_csv('NAME.csv')
        print(df)
        driver.close()









