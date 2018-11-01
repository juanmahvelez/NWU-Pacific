import gensim
from nltk.stem import WordNetLemmatizer, SnowballStemmer
import string
import nltk
nltk.download('wordnet')


stoplist = gensim.parsing.preprocessing.STOPWORDS

def lemmatize_stemming(text, stemmer = SnowballStemmer('english')):
    text = text.decode('utf-8')
    return stemmer.stem(WordNetLemmatizer().lemmatize(text, pos='v'))

def remove_punctuation(s, exclude = string.punctuation):
    table = string.maketrans("","")
    return s.translate(table, exclude)


def tokenize(document, stem=True, stemmer=SnowballStemmer('english'),
             stoplist=gensim.parsing.preprocessing.STOPWORDS):
    if type(document) == str:
        tokens = []
        document = remove_punctuation(document)
        for word in document.lower().split():
            if word not in stoplist and len(word) > 3:
                tokens.append(lemmatize_stemming(word, stemmer)
        return tokens

