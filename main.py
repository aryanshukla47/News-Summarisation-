import tkinter as tk
import nltk
from textblob import TextBlob
from newspaper import Article


nltk.download('punkt') # for sentiment analysis 

# summarisation & sentiment analysis 

url = 'https://indianexpress.com/article/cities/delhi/delhi-weather-forecast-imd-heatwave-alert-2024-9293662/'

article = Article(url)

article.download()
article.parse()
article.nlp()

print(f'Title:{article.title}')
print(f'Author:{article.authors}')
print(f'Publication Date:{article.publish_date}')
print(f'Summary:{article.summary}')

analysis = TextBlob(article.text)
print(analysis.polarity)
print(f'Sentiment:{"positive" if analysis.polarity>0 else "negative" if analysis.polarity<0 else "neutral"}')
