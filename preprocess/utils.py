from nltk.corpus import stopwords
import unicodedata
import nltk
import re
import string

class preprocessor:

	def __init__(self):
		self.cachedStopWords = stopwords.words('portuguese')
		self.stemmer = nltk.stem.SnowballStemmer('portuguese')
		self.translator = str.maketrans({key:' ' for key in string.punctuation})

	def removePonctuation(self, string):
		return string.translate(self.translator)

	def removeNumbers(self, string):
		return re.sub('[0-9]', '' , string)

	def removeStopWords(self, string):
		return ' '.join([word for word in string.lower().split() if word not in self.cachedStopWords])

	def stemWords(self, string):
		return ' '.join([self.stemmer.stem(word) for word in string.lower().split()])

	def prep(self, string, useStopWords = True, stem = True):
		#removing numbers and ponctuations
		result = self.removeNumbers(self.removePonctuation(string)).lower()

		if useStopWords and stem:
			result = ' '.join([stemmer.stem(word) for word in result.split() if word not in cachedStopWords])
		elif useStopWords:
			result = ' '.join([word for word in result.split() if word not in cachedStopWords])
		elif stem:
			result = ' '.join([stemmer.stem(word) for word in result.split()])

		return result