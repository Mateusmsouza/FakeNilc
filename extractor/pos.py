# -*- coding: utf-8 -*-

from extractor import preprocessing
import numpy as np

#supress some warnings about type conversion
import warnings
with warnings.catch_warnings():
	warnings.filterwarnings("ignore",category=FutureWarning)
	from nlpnet import POSTagger


def countTags(text, tagger, normalize=False):

	wordcount = 0

	#pos tags used by nlpnet
	pos_tags = {'ADJ': 0, 'ADV': 0, 'ADV-KS': 0, 'ART': 0, 'CUR': 0, 'IN': 0, 'KC': 0, 'KS': 0, 'N': 0, 'NPROP': 0, 'NUM': 0, 'PCP': 0, 'PDEN': 0, 'PREP': 0, 'PROADJ': 0, 'PRO-KS': 0, 'PROPESS': 0, 'PROSUB': 0, 'V': 0, 'PU': 0}

	#counting frequencies
	#for each resulting tuple from the tagging method
	for res in tagger.tag(text):
		for word_result in res:
			wordcount += 1
			#sometimes one word gets more than one tag. Splitting it into two or more tags
			split_result = word_result[1].replace('+',' ').split()

			#increase the frequency of each tag
			for tag in split_result:
				pos_tags[tag] += 1

	result = list(pos_tags.values())

	for i in range(len(result)):
		if(wordcount == 0):
			exit(0)
		result[i] /= wordcount

	return result


#function that loads the corpus and counts LIWC classes frequencies
def loadPos(filenames, tags, max_features = None, normalize = False, total_normalization = True):

	result = {'labels': [], 'data': []}

	#loading nlpnet	
	tagger = POSTagger(r'var/nlpnet', language='pt')

	result['labels'] = list({'ADJ': 0, 'ADV': 0, 'ADV-KS': 0, 'ART': 0, 'CUR': 0, 'IN': 0, 'KC': 0, 'KS': 0, 'N': 0, 'NPROP': 0, 'NUM': 0, 'PCP': 0, 'PDEN': 0, 'PREP': 0, 'PROADJ': 0, 'PRO-KS': 0, 'PROPESS': 0, 'PROSUB': 0, 'V': 0, 'PU': 0}.keys())

	# print(result['labels'])
	#loading files
	for filename, tag in zip(filenames,tags):
		with open(filename, encoding='utf8') as f:
			#preprocesses the text read in f using prep()
			#then counts the frequencies using the tagger
			#returns a list with frequencies
			try:
				freqs = countTags(preprocessing.prep(f.read(), useStopWords = False, stem = False),tagger, normalize=False)
			except:
				print('Error processing POS with :',filename,flush=True)
				continue

			#then appends this list into the data segment of the result dict
			result['data'].append(freqs)

	return result