#module validates documents


import nltk
from math import log
import string



#function: returns dict of nouns with less idf
def validate(data):
	nltk_sent=nltk.sent_tokenize(data)
	nltk.tokens=[]
	for w in nltk_sent:
		nltk.tokens.append(nltk.word_tokenize(w.lower()))

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

	idfsum=0
	for i in range(len(u)):
		idfsum=idfsum+idf2[i]
	idfavg = float(idfsum/len(idf2))


	dict1={}
	pos1 = nltk.pos_tag(u)
	for i in range(len(u)):
		if ((pos1[i])[1].startswith('N')) and (idf2[i]<idfavg) :		
			dict1[u[i]] = idf2[i]

	return [*dict1]		
	
    
#function: compare nouns with automobile words and validate document
def compare(arr):
    flag=0      
# initialize result with first array as a set 
    result = set(arr[0]) 
    for currSet in arr[1:]: 
        result.intersection_update(currSet) 

    with open("autowords.txt","r") as f2:
	    u1=f2.read().splitlines()         
   
    newList = []
    for i in u1:
        newList.append(i.lower())
    for w in list(result):
	    if w.lower() in newList:
		    flag=1

    if(len(list(result))==0):
    	return 0
    elif(flag==1):	
    	return 1
    else:
        return 0



#global array
comparison_list=[]


#function: returns result to main module
def input_valid(n):
	for i in range(n):
		myfile = open("new {}.txt".format(i+1), "r")
		data = myfile.read()
		comparison_list.append(validate(data))
	k=(compare(comparison_list))
	k=int(k)
	return k
