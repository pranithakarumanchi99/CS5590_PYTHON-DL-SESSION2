from bs4 import BeautifulSoup
import urllib.request
import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')
nltk.download('wordnet')
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.util import trigrams
from nltk import ne_chunk


# Read the web url into a variable
url = "https://en.wikipedia.org/wiki/Google"

# use urllib to open the url
page = urllib.request.urlopen(url)    #opening the defined url
plain_text = page
# Use beautiful soup to get the content of webpage
soup = BeautifulSoup(plain_text, "html.parser") #using beautiful soap to get the text

input = soup.get_text("\n") #Extracting text using soup.get_text

#writig the data to a text file
with open("out.txt",'w') as f:
    f.write(str(input.encode("utf-8")))

# Tokenization

wtokens = nltk.word_tokenize(input)
#print("Tokenized words: ", wtokens)

#POS

pos = nltk.pos_tag(wtokens)

print("Parts Of Speech", pos)

#Trigrams
print("Trigrams: ")
print(list(trigrams(wtokens)))  #listing all the trigrams from the words

#Named Entity Recognition
ner = ne_chunk(pos)
print("Named Entity Recognition", ner)

#Stemming
with open("out.txt",'r') as f:
    lines=f.read().splitlines() #splitting the data into lines
    for l in lines:
        words=l.split()   # for each line of the data, splititng into words
        pstem=PorterStemmer()
        word_lemmatizer=WordNetLemmatizer()
        for i in words:
            print("Stemmed words")
            # applying stemmer to get the stem of the word
            print(pstem.stem(i))
            # applying stemmer to get the stem of the word
            print("Lemmatized words")
            # applying lemmatization to each word to check the difference
            print(word_lemmatizer.lemmatize(i))

