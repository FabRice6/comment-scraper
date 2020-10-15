"""
This script will analyze the text by counting occurrences of (groups of) significant words.
TODO Think about multiplying the comments by #(likes - dislikes) or to focus only on comments with most likes.

Advice:
    Jos: Ik zou beginnen met 1-grams (geen 2 grams) en de NOT inderdaad als stop woord zien en niet meenemen. 
    Je zoekt naar thema's waar yogi's over praten? Not is wél belangrijk voor sentiment analyse maar dat doe je dan 
    beter via classifier op sentence embeddings. Voor topic clustering is NOT niét belangrijk want blijft zelfde topic?

Input: 
    TODO A list of strings representing the comments. Probably better to keep the strings apart for other analyses later

Returns:
    TODO Dataframe with count per word per text input. (Probably better to return a dictionary with word(group) + count, since we don't care about the phrases separately).

Example for running as the main program:
    $ python word_counter.py --> Runs with argument defined in the script
    $ python word_counter.py STRING_TO_ANALYZE --> Uncomment the part with 'sys.argv[1]' to run this type of commands
"""
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

def word_counter(list_of_strings, group_size=1, lang='english'):

    # stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

    CountVec = CountVectorizer(ngram_range=(group_size, group_size), stop_words=lang)

    # Transform
    Count_data = CountVec.fit_transform(list_of_strings)
    
    # Create dataframe
    df=pd.DataFrame(Count_data.toarray(),columns=CountVec.get_feature_names())
    df.loc['Totals'] = df.sum()
    df = pd.concat([df.loc[['Totals']], df[:-1]], axis=0)
    print(df)

string_1="This is a good job. I will not miss it for anything"
string_2="This is not good at all"

strings = [string_1, string_2]

if __name__ == "__main__":
    word_counter(strings)
    word_counter(strings, 2)

# # If you want to run this script to analyze a string passed in the terminal.
# if __name__ == "__main__":
#     scrape(sys.argv[1])
#     scrape(sys.argv[1], 2)