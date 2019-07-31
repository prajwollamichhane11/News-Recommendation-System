import nltk, string
from sklearn.feature_extraction.text import TfidfVectorizer


nltk.download('punkt')


stemmer = nltk.stem.porter.PorterStemmer()
remove_punctuation_map = dict((ord(char), None) for char in string.punctuation)


def stem_tokens(tokens):
    return [stemmer.stem(item) for item in tokens]


def normalize(text):
    return stem_tokens(nltk.word_tokenize(text.lower().translate(remove_punctuation_map)))



vectorizer = TfidfVectorizer(tokenizer=normalize, stop_words='english')



def cosine_sim(text1, text2):
    tfidf = vectorizer.fit_transform([text1, text2])
    return ((tfidf * tfidf.T).A)[0,1]


count = 0
Title = open("./NewsTitle", "r")
for lines in (Title):
    count = count + 1
    print(count,end = " ")
    title_file = open("./NewsTitle", "r")
    for eachline in (title_file):
        print (eachline)
        #print(lines)
        print(cosine_sim(lines, eachline))
