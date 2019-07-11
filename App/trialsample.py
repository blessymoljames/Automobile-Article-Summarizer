#input and output module
#this module takes input from the html form and redirects output to the form


from App import lem
from urllib import request,error
from bs4 import BeautifulSoup as soup
import string
from App import validate


#function for validating the web URL
def validate_web_url(url):
	try:
		request.urlopen(url)
		return url
	except error.HTTPError:
		headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
		reg_url = url
		req = request.Request(url=reg_url, headers=headers) 
		return req
	except error.URLError:
		return 0



#function for document validation
def valid(n):
	k=validate.input_valid(n)
	return k



#input function
def inputdata(n1):
	for i in range(n1):
		myfile = open("new {}.txt".format(i+1), "r")
		data = myfile.read()
		if len(data)==0:
			print("no length")
		if len(data)!=0:
			lem.tokenizedata(data)
		myfile.close()
	lem.second_input()




#output function
def outputdata():        
	with open("output2.txt","r") as myfile:
		data=myfile.read()
	return data




#main function: takes input from the form
def main(data):
#defining textfiles
	open("output2.txt","w").close()
	open('pos.txt', 'w').close()
	open('neg.txt', 'w').close()
	open('neu.txt', 'w').close()
	open('test.txt', 'w').close()
	open('test1.txt', 'w').close()


#parsing data
	for i in range(len(data)):

		p1=validate_web_url(data[i])
		print(p1)
		if(p1==0):
			a="exception araised"
			print(a)
			return a

		html = request.urlopen(p1)            
		bs = soup(html, "html.parser")
		allText = bs.find_all('p')
		if not allText:
			continue
		else:
			f1=open("new {}.txt".format(i+1),"w")
			for j in allText:
				f1.write(j.text)
			f1.close()

	n=len(data)
	v=valid(n)
	if(v==0):		
		a="Sorry, Invalid input"
		return a
	else:
		inputdata(n)
		a=outputdata()
		return a
