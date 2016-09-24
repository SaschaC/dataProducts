# tabelel mit woertern (mindestens zweisilbig), Wortart(A,N,V), frequency, silbenzahl, akzentposition und wortart (nur Nomen, Adektiv, Verb) erstellen
import string, re

def input(f):
	file = [line.split('\\') for line in open(f, 'r').read().split('\n')]
	return file
	
def output(matches):

	out = open('./stats.txt', 'w')
	header=['index','word','frequency','wortart','accent_p','syll_n']
	out.write(string.join(header,'\t')+'\n')
	for line in matches:
		out.write(string.join(line, '\t')+'\n')

	
def create_stats(gpl, gml):	

	stats = []
	for i, line in enumerate(gpl):
		
		syll_n = get_syll_n(line[3])
		wortart = get_wortart(gml[i][13])
		
		if syll_n >=2 and wortart != 0:
			frequency = line[2]
			accent_p = get_accent(line[3])	
			stats.append([line[0],line[1],line[2],wortart,str(accent_p),str(syll_n)])
		
	return stats
	
def get_accent(element):

	syllables = element.split('-') # be-`ruf
	for i, syll in enumerate(syllables):
		if syll[0]=='\'':
			return i+1	
	return('error')
	
def get_syll_n(element):
	syllables=element.split('-')
	return(len(syllables))
	
def get_wortart(element):

	if re.search('\[A\]$',element):
		return 'A'
	elif re.search('\[N\]$',element):
		return 'N'
	elif re.search('\[V\]$',element):
		return 'V'	
	return 0

	
##############################################################
##############################################################

f1 = '../GML_GPL/GPL.txt'
f2 = '../GML_GPL/GML.txt'
gpl = input(f1)
gml = input(f2)

stats = create_stats(gpl, gml)
output(stats)




