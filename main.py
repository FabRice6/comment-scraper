"""
Main script to scrape and analyze the comments of any Youtube video.

Example: TODO adapt if necessary with eg. a second argument = location for saving the output.
    $ python main.py "https://www.youtube.com/watch?v=ZK2XBduF84I&ab_channel=YogaWithAdriene"
    $ python main.py "https://www.youtube.com/watch?v=Jcpn_W9cbZU&ab_channel=SportclubHetEiland" ---> (Just 4 comments and 1 comment-like)
"""
import functions.comments as comments
import functions.word_counter as word_counter
import numpy as np
import os
import sys

if __name__ == "__main__":
    comments_and_likes = comments.scrape(sys.argv[1])
    print(comments_and_likes)
    count_table = word_counter.word_counter(comments_and_likes['comments']['text'])

    # Add the number of likes as the first column of the dataframe.
    likes = comments_and_likes['comments']['likes']
    count_table['likes'] = likes
    columns = count_table.columns
    new_columns = columns[:-1].insert(0, columns[-1])
    count_table = count_table.reindex(columns=new_columns)
    # Add a 'Totals' columns as the first row.
    
    print(count_table)

    # Save the results to a csv
    path = './reports'
    name = f"YouTube_video_{comments_and_likes['title']}"
    # count_table.to_csv(os.path.join(path, name + '.csv'))
    count_table.to_excel(os.path.join(path, name + '.xlsx'))



 
