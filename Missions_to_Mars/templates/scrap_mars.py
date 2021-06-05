from splinter import Browser
from bs4 import BeautifulSoup as bs
import time
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

def init_browser():
    executable_path = {"executable_path": "ChromeDriverManager().install()"}
    return Browser("chrome", **executable_path, headless=False)

def scrape_info():
    browser = init_browser()

    # mars news
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)

    time.sleep(1)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")


    # Get the new title and paragraph
    news_title = soup.find('div', id='content_title')[0].text

    news_p = soup.find('div', id='article_teaser_body')[0].text

    #Find the src for the sloth image
    relative_image_path = soup.find_all('img', class = 'headerimage')[1]["src"]
    featured_img = url + relative_image_path

    
    # mars facts table
    mars_factsUrl = "https://space-facts.com/mars/"

    tables = pd.read_html(mars_factsUrl)
    tables

    df = tables[0]
    df.head()



    #mars hemispheres
    hemisphere_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(hemisphere_url)

    time.sleep(1)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")

    hemisphere = soup.find_all('div', class = 'description')





    browser.quit()
    
    return scrape_info