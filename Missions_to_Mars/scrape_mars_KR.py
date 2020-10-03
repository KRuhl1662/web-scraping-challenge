#install dependencies

import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup as bs
import requests
import os


def scrape_mars():
    # intializing the browser object
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)

    mars_data = {
        "news_title":news_title,
        "news_paragraph":news_parag,
        "featured_image":feature_image(),
        "mars facts": table(),
        "hemispheres":mars_hemis()
    }


def news():
    ## PART 1

    # set NASA url
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)

    # Beautiful Soup time!

    html = browser.html
    soup = bs(html, 'html.parser')

    # Finding the most recent title and pargraph
    news_title_div = soup.find('div', class_ = 'list_text').find('div', class_='content_title')
    print(news_title_div)

    new_parag_div = soup.find('div', class_= 'article_teaser_body')
    new_parag_div

    # print news title to check
    news_title = news_title_div.get_text()
    news_title

    # print news summary paragraph
    news_parag = new_parag_div.get_text()
    news_parag


def feature_image():
    ## PART 2

    # set featured image url
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)


    # use splinter to find full image button and click on button
    full_image_button = browser.find_by_id('full_image')
    full_image_button.click()


    # use splinter to find more info button and click the button

    # since not all elements do not load at the same time, this step says "keep checking for this element with this identifier and wait for so long before checking again"
    browser.is_element_present_by_text('more info', wait_time=1)

    # since button does not have an id, now we have to find the "link" by using text 
    more_info_button = browser.links.find_by_partial_text('more info')
    more_info_button.click()


    # BeautifulSoup time to get the image html
    html = browser.html
    soup = bs(html, 'html.parser')

    # Trying to get image url, it was recommended to do a try/except for error handling... need to understand when to use this more.

    # this finds the relative image path
    relative_img_url = soup.find('figure', class_ ="lede").find('img', class_='main_image').get('src')
        
    feature_image_url = f'https://www.jpl.nasa.gov{relative_img_url}'
    feature_image_url


def table():
    # PART 3

    #Table Scrapping

    # set the url
    url = 'https://space-facts.com/mars/'

    # scrape tables from the url and save to dataframes
    tables = pd.read_html(url)

    type(tables)

    # print first table
    tables[0]

    # Save table to a pandas dataframe
    mars_stats_df = tables[0]

    # add column headers
    mars_stats_df.columns=['Description', 'Mars']
    mars_stats_df

    # set Description column as index
    # https://beenje.github.io/blog/posts/parsing-html-tables-in-python-with-pandas/
    mars_stats_df.set_index('Description', inplace = True)
    mars_stats_df

    # convert dataframe to html table string
    mars_stats_df.to_html('mars_facts.html')



def mars_hemis():
    ## Part 4

    # set featured image url
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)


    # CERBERUS (I'm sure there is going to be a way to loop this process, but I want to just get it working first)
    # use Splinter to click on Cerberus link
    cerberus_link = browser.links.find_by_partial_text('Cerberus Hemisphere Enhanced')
    cerberus_link.click()

    # BeautifulSoup time to get image link!
    html = browser.html
    soup = bs(html, 'html.parser')

    #get relative link
    relative_cerberus_url = soup.find('img', class_='wide-image').get('src')

    #append for full link
    cerberus_img_url = f'https://astrogeology.usgs.gov{relative_cerberus_url}'
    cerberus_img_url


    # SCHIAPARELLI
    # click on Schiaparelli link
    schia_link = browser.links.find_by_partial_text('Schiaparelli Hemisphere Enhanced')
    schia_link.click()

    # BeautifulSoup time to get image link!
    html = browser.html
    soup = bs(html, 'html.parser')

    #get relative link
    relative_schia_url = soup.find('img', class_='wide-image').get('src')

    #append for full link
    schiaparelli_img_url = f'https://astrogeology.usgs.gov{relative_schia_url}'
    schiaparelli_img_url


    # SYRTIS MAJOR
    # click on Syrtis Major link
    syrtis_link = browser.links.find_by_partial_text('Syrtis Major Hemisphere Enhanced')
    syrtis_link.click()

    # BeautifulSoup time to get image link!
    html = browser.html
    soup = bs(html, 'html.parser')

    #get relative link
    relative_syrtis_url = soup.find('img', class_='wide-image').get('src')

    #append for full link
    syrtis_img_url = f'https://astrogeology.usgs.gov{relative_syrtis_url}'
    syrtis_img_url


    # VALLES MARINERIS
    # click on Valles Marineris link
    valles_link = browser.links.find_by_partial_text('Valles Marineris Hemisphere Enhanced')
    valles_link.click()

    # BeautifulSoup time to get image link!
    html = browser.html
    soup = bs(html, 'html.parser')

    #get relative link
    relative_valles_url = soup.find('img', class_='wide-image').get('src')

    #append for full link
    valles_img_url = f'https://astrogeology.usgs.gov{relative_valles_url}'
    valles_img_url


    # Hemisphere Images
    mars_hemis = [
        {"title": "Cerberus Hemisphere", "img_url": cerberus_img_url},
        {"title": "Schiaparelli Hemisphere", "img_url": schiaparelli_img_url},
        {"title": "Syrtis Major Hemisphere", "img_url": syrtis_img_url},
        {"title": "Valles Marineris Hemisphere", "img_url": valles_img_url}
    ]


