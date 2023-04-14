import nltk
from nltk.corpus import stopwords
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

nltk.download('averaged_perceptron_tagger')


rating_5 = ["reviews_blazing-tree-brewery-el-paso.txt"]
rating_4_half = ["reviews_chase-the-taste-el-paso.txt", "reviews_orange-cow-burgers-el-paso-2.txt", "reviews_roscos-burger-inn-el-paso.txt", "reviews_the-hoppy-monk-el-paso-el-paso.txt"]
rating_4 =["reviews_crave-kitchen-and-bar-el-paso-2.txt","reviews_west-texas-chophouse-el-paso-5.txt"]
rating_3_half =["reviews_toro-burger-bar-el-paso-3.txt","reviews_track-one-el-paso.txt"] 
rating_3 =["reviews_mooyah-burgers-fries-and-shakes-el-paso-2.txt"]
rating_2_half =["reviews_slap-burger-el-paso.txt"] 


while True:
    rating = input("Enter a rating (Ex. rating_5, rating_4_half), or type 'exit': ")
    if rating == 'exit':
        break
    try:
        file_names = globals()[rating]
    except KeyError:
        print("Invalid rating. Please try again.")
        continue
    
    for file_name in file_names:
        with open(file_name, "r") as reviews:
             text = reviews.read()
             print(text)
             tokens =nltk.word_tokenize(text)
             pos_token =nltk.pos_tag(tokens)
             for token in pos_token:
                if token[1].startswith ('JJ') or token[1].startswith('NN') or token[1].startswith('VB'):
                    print(token)
             for file_name in file_names:
                 with open(file_name, "r") as reviews:
                     text = reviews.read()
                     analyzer = SentimentIntensityAnalyzer()
                     sentiment_score = analyzer.polarity_scores(text)
                     print(file_name)
                     print(sentiment_score)
                     print('\n')