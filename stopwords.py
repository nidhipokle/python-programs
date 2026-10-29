import nltk
nltk.download('stopwords')

from nltk.corpus import stopwords

stops = set(stopwords.words('english'))

words = ['There', 'is', 'a', 'tree',
         'near', 'the', 'river']

for word in words:
    if word.lower() not in stops:
        print(word)
