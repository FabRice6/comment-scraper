"""
Script to scrape the comments of any Youtube video.

Example:
    $ python functions/comments.py "https://www.youtube.com/watch?v=ZK2XBduF84I&ab_channel=YogaWithAdriene"
    $ python functions/comments.py "https://www.youtube.com/watch?v=Jcpn_W9cbZU&ab_channel=SportclubHetEiland" ---> (Just 4 comments and 1 comment-like)
"""

from selenium import webdriver
from selenium.common import exceptions
import sys
import time

def scrape(url):
    """
    Extracts the comments from the Youtube video given by the URL.

    Args:
        url (str): The URL to the Youtube video

    Raises:
        selenium.common.exceptions.NoSuchElementException:
        When certain elements to look for cannot be found
    
    Returns:
        Dictionary with video title, all comments and the likes count for each comment.
    """

    # Note: replace argument with absolute path to the driver executable.
    driver = webdriver.Chrome('/Users/fabriceverhaert/github/tech/chromedriver')

    # Navigates to the URL, maximizes the current window, and
    # then suspends execution for (at least) 5 seconds (this
    # gives time for the page to load).
    driver.get(url)
    driver.maximize_window()
    time.sleep(5)

    try:
        # Extract the elements storing the video title and
        # comment section.
        title = driver.find_element_by_xpath('//*[@id="container"]/h1/yt-formatted-string').text
        comment_section = driver.find_element_by_xpath('//*[@id="comments"]')
    except exceptions.NoSuchElementException:
        # Note: Youtube may have changed their HTML layouts for
        # videos, so raise an error for sanity sake in case the
        # elements provided cannot be found anymore.
        error = "Error: Double check selector OR "
        error += "element may not yet be on the screen at the time of the find operation"
        print(error)

    # Scroll into view the comment section, then allow some time
    # for everything to be loaded as necessary.
    driver.execute_script("arguments[0].scrollIntoView();", comment_section)
    time.sleep(7)

    # Scroll all the way down to the bottom in order to get all the
    # elements loaded (since Youtube dynamically loads them).
    last_height = driver.execute_script("return document.documentElement.scrollHeight")

    while True:
        # Scroll down 'til "next load".
        driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")

        # Wait to load everything thus far.
        time.sleep(2)

        # Calculate new scroll height and compare with last scroll height.
        new_height = driver.execute_script("return document.documentElement.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    # One last scroll just in case.
    driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")

    try:
        # Extract the elements storing the usernames and comments.
        comment_elems = driver.find_elements_by_xpath('//*[@id="content-text"]')
        like_counts = driver.find_elements_by_xpath('//*[@id="vote-count-middle"]')
    except exceptions.NoSuchElementException:
        error = "Error: Double check selector OR "
        error += "element may not yet be on the screen at the time of the find operation"
        print(error)

    print("> VIDEO TITLE: " + title + "\n")
    print("> SCRAPING COMMENTS...")

    # print("-----------------------\nCOMMENT ELEMS\n-----------------------")
    # print(f"Length: {len(comment_elems)}")
    # print(comment_elems)

    results = {
        'title': title,
        'comments': {
            'text': [],
            'likes': []
        }
    }

    for comment, likes in zip(comment_elems, like_counts):
        # Reformat missing likes and type '1.5K' like count to integer
        if not likes.text: 
            likes = 0
        elif likes.text[-1] == 'K':
            likes = int(float(likes.text[:-1]) * 1000)
        elif likes.text[-1] == 'M':
            likes = int(float(likes.text[:-1]) * 1000 * 1000)
        else:
            likes = int(likes.text)
        results['comments']['text'].append(comment.text)
        results['comments']['likes'].append(likes)
        
        # Print out the results
        # print(username.text + ":")
        # print(comment.text + "\n")
        # print("--------------NO. OF LIKES: " + str(likes) + '\n') 

    driver.close()

    return results

if __name__ == "__main__":
    scrape(sys.argv[1])
