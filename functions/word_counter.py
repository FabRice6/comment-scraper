"""
This script will analyze the text by counting occurrences of (groups of) significant words.
TODO Think about multiplying the comments by #(likes - dislikes) or to focus only on comments with most likes.

Input: 
    TODO A list of strings representing the comments. Probably better to keep the strings apart for other analyses later

Returns:
    TODO Dataframe with count per word per text input. (Probably better to return a dictionary with word(group) + count, since we don't care about the phrases separately).
"""



import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
 
sentence_1="This is a good job. I will not miss it for anything"
sentence_2="This is not good at all"


 
 
 
CountVec_n1 = CountVectorizer(ngram_range=(1,1), stop_words='english')
CountVec_n2 = CountVectorizer(ngram_range=(2,2), stop_words='english')

# Transform
Count_data = CountVec_n1.fit_transform([sentence_1,sentence_2])
 
# Create dataframe
cv_dataframe=pd.DataFrame(Count_data.toarray(),columns=CountVec.get_feature_names())
print(cv_dataframe)
