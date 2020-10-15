"""
Main script to scrape and analyze the comments of any Youtube video.

Example: TODO adapt if necessary with eg. a second argument = location for saving the output.
    $ python main.py "https://www.youtube.com/watch?v=ZK2XBduF84I&ab_channel=YogaWithAdriene"
    $ python main.py "https://www.youtube.com/watch?v=Jcpn_W9cbZU&ab_channel=SportclubHetEiland" ---> (Just 4 comments and 1 comment-like)
"""
import functions.comments as comments
import sys

if __name__ == "__main__":
    comments_and_likes = comments.scrape(sys.argv[1])
    print(comments_and_likes)