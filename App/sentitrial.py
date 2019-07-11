#Modules containing summaring and sentiment analysis methods


import numpy as np
from math import * 
import networkx as nx
import scipy
from sklearn.metrics.pairwise import cosine_similarity
import nltk
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords 
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import sentiwordnet as swn	
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.corpus import sentiwordnet as swn
from App import lem



#summary generation function
def summary(data,flag):
	stop_words = set(stopwords.words('english')) 
	punctuations = '"!()-[]{};:"\,<>./?@#$%^&*_~"'
	dig="0123456789"
	sentences=sent_tokenize(data)
	lemmatizer = WordNetLemmatizer()
	ps=PorterStemmer()

	final=[]
	files=open("test1.txt","a")

	for s in sent_tokenize(data):
		files.write("\n\nSentence is: "+s+"\n\n")
		tokens=[]
		nltk_tokens = nltk.word_tokenize(s.lower())
		files.write("Tokenized words: "+str(nltk_tokens)+"\n\n")

		for w in nltk_tokens:
			k=w.split('.')
			if(int(len(w.split('.'))>1) and k[1]=='' ):
				tokens.append(k[0])
				tokens.append('.')
			else:
				tokens.append(k[0])

		filtered_sentence = [] 		  
		for w in tokens: 
			if w.lower() not in stop_words: 
				filtered_sentence.append(w)
		files.write("Stopword removed: "+str(filtered_sentence)+"\n\n")

		no_punct = []
		for char in filtered_sentence:
			if char not in punctuations:
				 no_punct.append(char)
		files.write("Punctuation removed: "+str(no_punct)+"\n\n")
		


		l=[]
		pos=[]
		for i in no_punct:
			l.append(i)	
			pos.append(nltk.pos_tag(l))
			l.pop()

		last=[]
		f=open('App/verb.txt','r')
		for i in range(0,len(no_punct)):
			flag=0
			f1=open('App/verb2.txt','r')			#verb2 contains words to be kept as such
			for line in f1:
				if(no_punct[i]==line.strip()):
					last.append(no_punct[i])
					flag=1
			if flag==1:
				continue

			if pos[i]=='NN' or pos[i]=='NNP' :
				last.append(no_punct[i])
				
			elif pos[i]=='NNS'or pos[i]=='NNPS':
				last.append(lemmatizer.lemmatize(no_punct[i]))

			elif pos[i]=='VBD' or pos[i]=='VBN':
				c1=0
				f=open('verb.txt','r')					#verb contains 'ed' words
				for line in f:
					if(no_punct[i]==line.strip()):
						last.append((ps.stem(no_punct[i]))+'e')
						c1=1		
				f.close()
				f=open('App/verb1.txt','r')			#verb1 contains 'ate' words
				for line in f:
					if(no_punct[i]==line.strip()):
						last.append((ps.stem(no_punct[i]))+'ate')
						c1=1		
				f.close()	
				if(c1==0):
					last.append(ps.stem(no_punct[i]))
			elif pos[i]=='VBG':
				c2=0
				f=open('verb.txt','r')
				for line in f:
					if(no_punct[i]==line.strip()):
						last.append((ps.stem(no_punct[i]))+'e')
						c2=1
				f.close()
				f=open('verb1.txt','r')
				for line in f:
					if(no_punct[i]==line.strip()):
						last.append((ps.stem(no_punct[i]))+'ate')
						c2=1		
				f.close()
				if(c2==0):
					last.append(ps.stem(no_punct[i]))
			elif pos[i]=='JJ':
				c3=0
				f=open('verb.txt','r')
				for line in f:
					if(no_punct[i]==line.strip()):
						last.append((ps.stem(no_punct[i]))+'e')
						c3=1
				f.close()
				if(c3==0):
					last.append(ps.stem(no_punct[i]))
			else:
				last.append(lemmatizer.lemmatize(no_punct[i]))		
		final.append(last)
	files.write("Last: "+str(last)+"\n\n\n\n")
	files.close()


	with open('test.txt', 'w') as f:					#lemmatized contents are stored
		for j in final:
			for k in j:
				       	f.write("%s " % k)
			f.write('. ')

	with open('test.txt', 'r') as myfile:
	  data = myfile.read()

#Sentence tokenization
	nltk_sent=nltk.sent_tokenize(data)
	nltk.tokens=[]
	for w in nltk_sent:
		nltk.tokens.append(nltk.word_tokenize(w))

#TF-IDF new calculation
	u=[]
	i=0
#finding unique words
	while i<len(nltk.tokens):
		for w in nltk.tokens[i]:
			if w not in u:
				u.append(w)
		i=i+1

#finding term frequency
	i=0
	c=[]
	while i<len(nltk.tokens):
		c1=[]	
		for w in u:
			if w in nltk.tokens[i]:
				c1.append(nltk.tokens[i].count(w))
			else:
				c1.append("0")
		i=i+1
		c.append(c1)

#Normalised tf
	ntf=[]
	for i in range(0,len(c),1):
		N=len(c[i])
		ntf1=[]
		for j in range(0,len(c[i]),1):
			ntf1.append(float(c[i][j])/N)
		ntf.append(ntf1)

	N=len(nltk.tokens)
	n=[]
	for i in range(0,len(u),1):
		s=0
		for j in range(0,len(c),1):
			 s=s+int(c[j][i])
		n.append(s)

#finding inv document frequency
	idf2=[]
	idf3=[]
	for i in range(0,len(n),1):
		idf2.append(1+log(float(N/int(n[i]))))


#tfidf calculation
	tfidfnew=[]
	for i in range(0,len(c),1):
		tfidf1=[]
		for j in range(0,len(u),1):
			tfidf1.append(float(float(ntf[i][j])*idf2[j]))
		tfidfnew.append(tfidf1)

#similarity matrix
	m=scipy.sparse.csr_matrix(tfidfnew)
	A=cosine_similarity(m,m)
	nx_graph1 = nx.from_scipy_sparse_matrix(scipy.sparse.csr_matrix(A))
	scores1 = nx.pagerank(nx_graph1)
	ranked1=sorted(((scores1[i],s) for i,s in enumerate(sentences)),reverse=True)
	return ranked1

#sentiment-analysis function
def sentiment(data):
	sid = SentimentIntensityAnalyzer()
	dig="0123456789"
	sentences=sent_tokenize(data)

#polarity score calculation
	final=[]
	sfinal2=0
	for s in sent_tokenize(data):
		scores = sid.polarity_scores(s)
		for key in sorted(scores):
			if key=='compound':
				sfinal2=sfinal2+scores[key]

	N=len(sentences)
	if (sfinal2/N)>(0.1):	
		f=open("pos.txt","a+")
		for s in sentences:
			f.write(s)
			f.write(" ")
		f.close()
	elif (sfinal2/N)<(-0.1):
		f=open("neg.txt","a+")
		for s in sentences:
			f.write(s)
			f.write(" ")
		f.close()
	else:
		f=open("neu.txt","a+")
		for s in sentences:
			f.write(s)
			f.write(" ")




#function for second level summary
def secondpos():
	with open('pos.txt', 'r') as myfile:
	  data=myfile.read()
	if len(data)!=0:
		lem.tokenizedata1(data," Positive")

def secondneg():
	with open('neg.txt', 'r') as myfile:
	  data = myfile.read()
	if len(data)!=0:
		lem.tokenizedata1(data," Negative")

def secondneu():
	with open('neu.txt', 'r') as myfile:
	  data = myfile.read()
	if len(data)!=0:
		lem.tokenizedata1(data," Neutral")
