#module for first-level and second-level summary generation

from App import sentitrial


#first-level summary generation
def tokenizedata(data):

	ranked1=sentitrial.summary(data,0)
	i1=len(ranked1)
	summarize_text1=[]

	with open("output.txt","w+") as f0:
		for i in range(int((0.6)*i1)):
			summarize_text1.append("".join(ranked1[i][1]))
		f0.write(" ".join(summarize_text1))

	with open("output.txt","r") as f0:
		data=f0.read()
	sentitrial.sentiment(data)


	
#functions for second level summary
def second_input():
	sentitrial.secondpos()
	sentitrial.secondneg()
	sentitrial.secondneu()	



#second-level summary generation
def tokenizedata1(data,i):
	ranked1=sentitrial.summary(data,1)
	i1=len(ranked1)
	summarize_text1=[]

	with open("output2.txt","a+") as f0:
		f0.write("\n"+i+" Summary:\n")
		for i in range(int((0.4)*i1)):
			summarize_text1.append("".join(ranked1[i][1]))
		f0.write(" ".join(summarize_text1))
