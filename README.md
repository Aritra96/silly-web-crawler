# Wikipedia Web Crawlin'

_All links lead to Rome? More like all links lead to Philosophy_

# Project Overview

There's this weird phenomenon on the web which you may be already familiar with, especially if you browse Wikipedia a little too much. 

If you begin browsing any random Wikipedia page and click the first link on each page which leads to the next, after a couple of clicks, you will find yourself on the "Philosophy" page. As of 2016, 97% of pages invariably lead to "Philosophy". 

Don't believe me yet? Check [this](https://en.wikipedia.org/wiki/Wikipedia:Getting_to_Philosophy) out.

This is a simple project which goes through a number of pages from the first page till the last page (as specified by the user) and counts how many pages were crawled to get to the last page.

### Running the program

You can run this program by using the command python udacitycrawler.py. 

By default it'll take you from a random wikipedia page to the Philosophy page. 

You can change this simply by changing the pages in the .py file. The two variables you may want to change are start_url and target_url.

# Requirements

* Language: Python 3.5 or above
* Libraries: beautifulsoup, requests, time, urllib

# Built with

* [Python 3.6.6](https://www.python.org/) - The language used to develop this.
* [time](https://docs.python.org/2/library/time.html) - One of the libraries used for this.
* [beautifulsoup](https://beautiful-soup-4.readthedocs.io/en/latest/) - One of the libraries used for this.
* [requests](https://pypi.org/project/requests/) - One of the libraries used for this.
* [urllib](https://docs.python.org/3/library/urllib.html) - One of the libraries used for this.

# Author

 * [Aritra Chattaraj](https://github.com/aritra96) - Sole author for this program. Mentioned all the help received in 'Acknowledgements' section.
 
# Acknowledgments

* [Udacity](https://www.udacity.com/)
* [Wikipedia](https://www.wikipedia.org/)
