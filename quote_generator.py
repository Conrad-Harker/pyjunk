import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
import markovify

nltk.download('stopwords')
nltk.download('punkt')

def new_quote_generator():
    df = pd.read_csv(r'C:\Users\harke\OneDrive\Desktop\Python\quotes\input\quotes.csv')

    # Subset the data if you want to select certain authors
    # selected_authors = ['Oscar Wilde', 'Marcus Aurelius','Mark Twain']
    # selected_quotes = df[df['author'].isin(selected_authors)]['quote']
    # print(selected_quotes)

    # Randomly sampled quote
    random_df = df[['quote','author']]
    random_quote = random_df.sample()
    random_quote = random_quote.values.tolist()
    random_quote = random_quote[0]
    quote = random_quote[0]
    author = random_quote[1]

    # Subset the data on all authors and quotes
    selected_quotes = df['quote']

    # Combine the quotes
    combined_quotes = ' '.join(selected_quotes)

    # Modeling
    # create a markov chain model from the cleaned tokens
    text_model = markovify.Text(combined_quotes, state_size=3)
    # generate a new quote from the model
    new_quote = text_model.make_sentence(tries=100)

    return new_quote

# Random Quote
def random_quote_generator():
    df = pd.read_csv(r'C:\Users\harke\OneDrive\Desktop\Python\quotes\input\quotes.csv')
    
    # Randomly sampled quote
    random_df = df[['quote','author']]
    random_quote = random_df.sample()
    random_quote = random_quote.values.tolist()
    random_quote = random_quote[0]
    quote = random_quote[0]
    author = random_quote[1]

    return quote, author