import requests
from bs4 import BeautifulSoup as bs
import time
from urllib.parse import urljoin
import urllib

#Initializing all variables
start_url = 'https://en.wikipedia.org/wiki/Special:Random'
target_url = 'https://en.wikipedia.org/wiki/Philosophy'
article_chain = [start_url]
count = 0

def continue_crawl(search_hist, target_url, max_steps = 25):
    """
     A function to create a 'crawler' that continues crawling until arriving
     at a particular (target) page

     Args:
        param1 (list): A search history list; contains all explored urls
        param2 (str): The target url as per user input
        param3 (int): The number of page crawls before halting; default val = 25

    Returns:
        True: Return true if the function can continue crawling
        False: Return false if one of the three conditions are met
    """
    if search_hist[-1] == target_url:
        print('\nWe\'ve found the target article.')
        return False
    elif len(search_hist) > max_steps:
        print('\nToo long; Aborting search!')
        return False
    elif search_hist[-1] in search_hist[:-1]:
        print('We\'re revisting an older article; Aborting search!')
        return False
    else:
        return True


def find_first_link(url):
    """
     A function created to find the first link in an article.

     Args:
        param1 (str): A url

    Returns:
        str (first_link): If a link is found, it is returned as a string
    """
    #Return the first link as a string, or return None if there is no link
    #Download html of last article in article_chain
    response = requests.get(url)
    #Feed the HTML into Beautiful Soup
    html = response.text
    soup = bs(html, 'html.parser')
    #Traversing to the correct path through id's to select the right place to
    #mine; this div contains the article's body, nested in two div tags
    content_div = soup.find(id="mw-content-text").find(class_="mw-parser-output")
    #Find the first link in the article, or set to None if no link in article
    article_link = None
    #Find all the direct children of content_div that are paragraphs
    #Recursive=False only allows bs to find direct children; what we want here.
    for element in content_div.find_all("p", recursive=False):
        #Find the first anchor tag that's a direct child of a paragraph.
        #It's important to only look at direct children, because other types
        #of link, e.g. footnotes and pronunciation, could come before the
        #first link to an article. Those other link types aren't direct
        #children though, they're in divs of various classes.
        if element.find('a', recursive=False):
            article_link = element.find('a', recursive=False).get('href')
            break

    if not article_link:
        return

    # Build a full url from the relative article_link url
    first_link = urllib.parse.urljoin('https://en.wikipedia.org/', article_link)

    return first_link


while continue_crawl(article_chain, target_url):
    count += 1
    print(article_chain[-1])
    #Passing string article_chain[-1] to receive string from find_first_link()
    first_link = find_first_link(article_chain[-1])
    if not first_link:
        print("\nIt appears we have arrived at an article with no links.")
        print("\nAbandon search!")
    #Add the first link to article_chain
    article_chain.append(first_link)
    #Delay for five seconds
    time.sleep(3)

print(f"\nWe crawled {count} times to get here.")
