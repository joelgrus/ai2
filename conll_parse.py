#!/usr/bin/python
# conll_parse.py

""" 
A python script which processes phoenix_0002.coref
from the CoNLL 2012 shared task. Github url is below.
"""

# Author: Kyle Buckingham <buckinkb@gmail.com>
# License: BSD 3 clause

import urllib2
import re
import pprint

response = urllib2.urlopen(
    'https://gist.githubusercontent.com/schmmd/c4fbc9f80dd23f7d25e463cbe653e68b/raw/bc65dd232766eac54b68ba6b18c5e553871a196b/phoenix_0002.coref')
doc = response.read()

# Make full_readout true for a full breakdown of the document.
full_readout = False

def get_text_blocks(doc):
    """Function to find text blocks within document. Prints out results"""
    r = re.finditer("<TEXT(.|\n)*?</TEXT>", doc)
    counts = []
    for s in r:
        counts += process_text(s.group())

    # Average count of distinct entities per sentence
    total_coref_counts = [sentence['coref_count'] for sentence in counts]
    avg = sum(total_coref_counts) / float(len(total_coref_counts))
    print 'Average count of distinct entities per sentence:  ' + str(avg)
    print ' '

	# Largest Sentences
    largest_sentence_count = max([sentence['word_count'] for sentence in counts])
    largest_sentences = [" ".join(sentence['words']) for sentence in counts if len(sentence['words']) == largest_sentence_count]
    print "Largest sentences (length " + str(largest_sentence_count) + '):'
    print ''
    for i,s in enumerate(largest_sentences):
    	print str(i + 1) + '. ' + s 
    	print ''


    # print max(total_word_counts)
    if full_readout: pprint.pprint(counts)


def process_text(text):
    """ Processing function for a text block. Right now its one
    massive for loop. With more time, it should be broken into
    more functions or classes (example classes would be 
    sentences or words)."""

    # Remove <TEXT></TEXT> tags
    text = re.sub("<TEXT(.*?)>", "", text)
    text = re.sub("</TEXT>", "", text)

    sentences = []
    corefs = []
    words = []
    newStr = ''
    i = 0
    while i < len(text):

        # "Dr." logic.
        if text[i + 2:i + 5] == 'Dr.':
            words.append('Dr.')
            i += 5
        # End of sentence logic (and caviats).
        elif text[i] in ['!', '.', '?'] or text[i:i + 2] == '--' or i + 1 == len(text):
            # If at the end of text block
            end = i + 1 == len(text)
            # Float numbers
            if not end and text[i + 1].isdigit() and text[i - 1].isdigit():
                newStr += text[i]
                i += 1
            # am/pm logic
            elif not end and i + 2 < len(text) and text[i + 2] == '.':
                newStr += text[i:i + 2]
                i += 3
            # End of sentence
            else:
                # If end of text string
                if end:
                    words.append(newStr)
                    newStr = ''
                # Remove LRB/RRB
                words = [word for word in words if word not in ['LRB', 'RRB']]
                sentences.append({
                    "corefs": corefs,
                    "words": words,
                    "word_count": len(words),
                    "coref_count": len(corefs)
                })
                # reset lists
                corefs = []
                words = []
                i += 1

        # Spaces logic
        elif text[i] == ' ':
            # handle "long - range"
            if text[i:i + 3] == ' - ':
                newStr += '-'
                i += 2
            # Create new word
            elif len(newStr) > 0:
                words.append(newStr)
                newStr = ''
            i += 1

        # Comma logic
        elif text[i] == ',':
            # comma numbers
            if text[i + 1].isdigit() and text[i - 1].isdigit():
                newStr += text[i]
                i += 1
            # check if word
            elif len(newStr) > 0:
                words.append(newStr)
                newStr = ''
                i += 1
            # skip otherise
            else:
                i += 1

        # Apostrophe logic
        elif text[i] == "'" and text[i + 1].isalpha():
            # n't
            if text[i - 1].isalpha():
                words[-1] += text[i - 1]
                newStr = ''
            # 't
            words[-1] += "'" + text[i + 1]
            #  're
            if text[i + 2].isalpha():
                words[-1] += text[i + 2]
                i += 1
            i += 2

        # Coreference logic
        elif text[i] == '<':
            # COREF. Find tag, add it to list
            end = text[i:].find('>') + i
            if text[i + 1] == 'C':
                id = re.findall(r'\d+', text[i:end])[0]
                if id not in corefs:
                    corefs.append(id)
            i = end + 1

        # Everything else
        else:
            # normal characters
            if text[i].isalnum():
                newStr += text[i]
            i += 1

    return sentences

get_text_blocks(doc)
