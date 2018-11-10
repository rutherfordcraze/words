import json, operator
from sys import version_info
from random import randint

py3 = version_info[0] > 2

minLength = 2
output = []

if py3:
	letters = input("Characters to include: ")
else:
	letters = raw_input("Characters to include: ")

if py3:
	minLength = int(input("Minimum word length: "))
else:
	minLength = int(raw_input("Minimum word length: "))

words = []
with open('dictionary.json') as WORDS_FILE:
	words = list(json.load(WORDS_FILE).keys())

runLength = len(words)

def GetWords():
	global output

	for word in range(runLength):
		wordLength = len(words[word])

		if wordLength >= minLength:
			wordOK = True

			for char in range(wordLength):
				if words[word][char:char+1] not in letters:
					wordOK = False
					break

			if wordOK:
				output.append(words[word])

	else:
		print(str(len(output)) + " results found.")
		print(' '.join(map(str,output)))

print("Checking " + str(runLength) + " words...")
GetWords()