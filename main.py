"""
Main script to scrape and analyze the comments of any Youtube video.

Example: TODO adapt if necessary with eg. a second argument = location for saving the output.
    $ python main.py "https://www.youtube.com/watch?v=ZK2XBduF84I&ab_channel=YogaWithAdriene"
    $ python main.py "https://www.youtube.com/watch?v=Jcpn_W9cbZU&ab_channel=SportclubHetEiland" ---> (Just 4 comments and 1 comment-like)
"""
import functions.comments as comments
import functions.word_counter as wcount
import pandas as pd
import json
import os
import sys

# Collect some of the best yoga videos on YouTube
# Accourding to Women's Health Mag: https://www.womenshealthmag.com/fitness/g29264172/best-yoga-videos/
urls = [
    'https://www.youtube.com/watch?v=oX6I6vs1EFs',
    'https://www.youtube.com/watch?v=FRAEaBtP2r4',
    'https://www.youtube.com/watch?v=v7AYKMP6rOE',
    'https://www.youtube.com/watch?v=oBu-pQG6sTY',
    'https://www.youtube.com/watch?v=Ci3na6ThUJc',
    'https://www.youtube.com/watch?v=w0cLgFg4Zsw',
    'https://www.youtube.com/watch?v=gbiHWx97x60',
    'https://www.youtube.com/watch?v=7ciS93shMNQ',
    'https://www.youtube.com/watch?v=4pKly2JojMw',
    'https://www.youtube.com/watch?v=GGJzZx4H2K4',
    'https://www.youtube.com/watch?v=hJbRpHZr_d0',
    'https://www.youtube.com/watch?v=4vTJHUDB5ak',
    'https://www.youtube.com/watch?v=tvucPJUJJFk',
    'https://www.youtube.com/watch?v=bN5_uqja5dk',
    'https://www.youtube.com/watch?v=dRsC1YdXqOc'
]

# Initialize empty dict for the results
comments_and_likes = {
    'title': 'WomensHealthMag_top15',
    'comments': {
        'text': [],
        'likes': []
    }
}

if __name__ == "__main__":
    # Scrape the comments from all the videos in the list
    # NOTE We want to analyze all comments together, not per video so we add all the comments to one list
    for url in urls: 
        one_video = comments.scrape(url=url)
        comments_and_likes['comments']['text'].append(one_video['comments']['text'])
        comments_and_likes['comments']['likes'].append(one_video['comments']['likes'])
    
    # Save the comments in a JSON file
    with open(f"./data/comments_{comments_and_likes['title']}.json", 'w') as fp:
        json.dump(comments_and_likes, fp, indent=4)

    # Make 1-, 2- and 3-grams
    for i in range(3):
        comment_texts = comments_and_likes['comments']['text']
        comment_likes = comments_and_likes['comments']['likes']
        table = wcount.word_counter(comment_texts, group_size=i+1)

        # Add the number of likes and create a 'Totals' row
        df = wcount.add_likes_and_totals(count_table=table, likes=comment_likes)
        print(df)
        # Save the results to a csv
        path = './reports'
        name = f"YouTube_video_{comments_and_likes['title']}_{i+1}gram"
        df.to_csv(os.path.join(path, name + '.csv'))
        # df.to_excel(os.path.join(path, name + '.xlsx'))