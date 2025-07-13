import tkinter as tk
from tkinter import messagebox
import nltk
from textblob import TextBlob
from newspaper import Article

# Download punkt if not available
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

def summarize():
    url = utext.get("1.0", "end").strip()
    if not url:
        messagebox.showerror("Error", "Please enter a URL.")
        return

    article = Article(url)

    try:
        article.download()
        article.parse()
        article.nlp()
    except Exception as e:
        messagebox.showerror("Download/Parse Error", f"Could not process the article.\n\nError: {e}")
        return

    # Enable text fields
    title.config(state='normal')
    author.config(state='normal')
    publication.config(state='normal')
    summary.config(state='normal')
    sentiment.config(state='normal')

    # Clear previous contents
    title.delete('1.0', 'end')
    author.delete('1.0', 'end')
    publication.delete('1.0', 'end')
    summary.delete('1.0', 'end')
    sentiment.delete('1.0', 'end')

    # Insert new content
    title.insert('1.0', article.title)
    author.insert('1.0', ", ".join(article.authors) if article.authors else "N/A")
    publication.insert('1.0', article.publish_date.strftime("%Y-%m-%d") if article.publish_date else "N/A")
    summary.insert('1.0', article.summary)

    # Sentiment analysis
    analysis = TextBlob(article.text)
    polarity = analysis.polarity
    sentiment_label = (
        "positive" if polarity > 0
        else "negative" if polarity < 0
        else "neutral"
    )
    sentiment.insert('1.0', f"Polarity: {polarity:.2f}, Sentiment: {sentiment_label}")

    # Lock fields
    title.config(state='disabled')
    author.config(state='disabled')
    publication.config(state='disabled')
    summary.config(state='disabled')
    sentiment.config(state='disabled')


# GUI setup
root = tk.Tk()
root.title("News Summarizer")
root.geometry("1200x600")

# Title
tlabel = tk.Label(root, text="Title")
tlabel.pack()
title = tk.Text(root, height=1, width=140, bg='#dddddd', state='disabled')
title.pack()

# Author
alabel = tk.Label(root, text="Author")
alabel.pack()
author = tk.Text(root, height=1, width=140, bg='#dddddd', state='disabled')
author.pack()

# Publish Date
plabel = tk.Label(root, text="Publishing Date")
plabel.pack()
publication = tk.Text(root, height=1, width=140, bg='#dddddd', state='disabled')
publication.pack()

# Summary
slabel = tk.Label(root, text="Summary")
slabel.pack()
summary = tk.Text(root, height=20, width=140, bg='#dddddd', state='disabled')
summary.pack()

# Sentiment
selabel = tk.Label(root, text="Sentiment Analysis")
selabel.pack()
sentiment = tk.Text(root, height=1, width=140, bg='#dddddd', state='disabled')
sentiment.pack()

# URL
ulabel = tk.Label(root, text="URL")
ulabel.pack()
utext = tk.Text(root, height=1, width=140)
utext.pack()

# Summarize Button
btn = tk.Button(root, text="Summarize", command=summarize)
btn.pack()

root.mainloop()
