import requests
import re

url = 'https://gist.githubusercontent.com/schmmd/c4fbc9f80dd23f7d25e463cbe653e68b/raw/bc65dd232766eac54b68ba6b18c5e553871a196b/phoenix_0002.coref'
r = requests.get(url)
doc = r.text

# find the first text block
def get_text_blocks(doc):
	r = re.finditer("<TEXT(.|\n)*?</TEXT>", doc)
	for (i,s) in enumerate(r):
		if i < 1:
			process_text(s.group())

def process_text(text):
	# remove text tags
	text = re.sub("<TEXT(.*?)>", "", text)
	text = re.sub("</TEXT>", "", text)

	text = '''At 3:42 on <COREF ID="320" TYPE="IDENT">July 28 , 1976</COREF> , 
	<COREF ID="323" TYPE="IDENT">a strong earthquake ca n't  should n't</COREF> hit ' ' ,,, <COREF ID="324" TYPE="IDENT">Tangshan </COREF> .'''
	
	sentences = []
	corefs = []
	words = []
	newStr = ''
	i = 0
	while i < len(text):
		# if text[i] in ['!','.','?']:
		# 	# sentence end
		# 	i += 1
		# 	# print 'end sentence'

		if text[i] == ' ':
			if len(newStr) > 0:
				words.append(newStr)
				newStr = ''
			i += 1
			print 'space'
		elif text[i] == ',':
			if len(newStr) > 0:
				words.append(newStr)
				newStr = ''
			i += 1
			print 'comma'
		elif text[i] == "'" and text[i+1].isalpha():
			# n't etc
			if text[i-1].isalpha():
				words[-1] += text[i-1]
				newStr = ''
			# 't
			words[-1] += "'" + text[i + 1]
			#  're
			if text[i+2].isalpha():
				words[-1] += text[i + 2]
				i += 1
			i += 2
			print 'apostrophe'
		elif text[i] == '<':
			# COREF. Find tag, add it to list
			end = text[i:].find('>') + i
			if text[i+1] == 'C':
				id = re.findall(r'\d+', text[i:end])[0]
				if id not in corefs:
					corefs.append(id)
			i = end + 1
			print 'coref'
		else:
			if text[i].isalnum():
				newStr += text[i]
			i += 1
			print 'character'

	print sentences
	print corefs
	print words
	print newStr

get_text_blocks(doc)