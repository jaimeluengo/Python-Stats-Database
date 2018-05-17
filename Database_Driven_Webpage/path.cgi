''' lol'''

import cgi
import cx_Oracle

def main():
    form = cgi.FieldStorage()
    theStr = form.getfirst('path','')
    contents = processInput(theStr)
    print contents

def processInput(theFile):
	con = cx_Oracle.connect('Jaime/lowkey')
	cur = con.cursor()
	cur.execute('drop table beeGenes')
	cur.execute('''create table beeGenes(
					gi varchar2(10),
					sequence clob,
					freq_A number,
					freq_C number,
					freq_G number,
					freq_T number,
					freq_CG number
					)''')
	cur.bindarraysize = 50
	cur.setinputsizes(10,9000,float, float, float,float,float)

	#read raw data from a file
	print(theFile)
	infile = file(theFile,'r')
	myStr=""
	finalStr=''
	
        #read line by line
        for aLine in infile:
            myStr=myStr + aLine
        
	#from a continuous string
	strL = myStr.replace('\n','')

	#change the string into a list, one protein per list item
	aList=strL.split('>')

	#keep the List items that contains the substring, [Apis mellifera]
	for anItem in aList:
		if 'mRNA' in anItem:
			finalStr = finalStr+anItem
	end=0

	totalLength=len(finalStr)
	repetitions = finalStr.count('mRNA')

	#extract the target  substrings, the gi number and the protein sequence
	for i in range(repetitions):
		
		start = finalStr.find('gi|',end)+3
		end = finalStr.find('|',start)
		gi = finalStr[start:end]
		#print 'gi=', gi
		start= finalStr.find('mRNA', end) +10
		end=finalStr.find('gi|', start)
		if end == -1:
			end = totalLength
		seq = finalStr[start : end]
		#print 'seq=', seq
		seqLength=len(seq)
		freq_A=seq.count('A')/float(seqLength)
		freq_C=seq.count('C')/float(seqLength)
		freq_G=seq.count('G')/float(seqLength)
		freq_T=seq.count('T')/float(seqLength)
		freq_CG= freq_C + freq_G
		
		cur.execute('''insert into beeGenes (gi, sequence, freq_A,
					freq_C,freq_G,freq_T,freq_CG) values(:v1,:v2,
					:v3,:v4,:v5,:v6,:v7)''',(gi, seq, freq_A,
					freq_C,freq_G,freq_T,freq_CG))

#(gi, seq, freq_A,freq_C,freq_G,freq_T,freq_T,freq_CG)		
	con.commit()
		
	cur.close()
	con.close()
		
	return makePage('done_submission_template.html',("Thank you for uploading"))

def fileToStr(fileName):
	'''Return a string containing the contents of the named file'''
	fin = open(fileName);
	contents = fin.read();
	fin.close()
	return contents

def makePage(templateFileName, substitutions):
	pageTemplate = fileToStr(templateFileName)
	return pageTemplate % substitutions
	
try:
	print "Content-type: text/html\n\n"
	main()
except:
	cgi.print_exception()
	
	
