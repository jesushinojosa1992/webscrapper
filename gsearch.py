#! /usr/bin/python

import webbrowser

import numpy as np

# Automated google searches opens new tabs with
# key words from kewyword_searched.txt

keyword_file = "keyword_searched.txt"


def lines(keyword_file):

	with open(keyword_file) as f:
		keyword_lines = f.read().splitlines()
	return keyword_lines

keyword_lines = lines(keyword_file)

print(keyword_lines[1])
print(type(keyword_lines[1]))
print("how many searches? ",len(keyword_lines))

def search():
	for i in range(len(keyword_lines)):
		tabUrl = "http://google.com/?q="
		umich=" University of Michigan Ann Arbor"
		term=keyword_lines[i]
		webbrowser.open(tabUrl+term+umich,new=[i])#opens a new tab for each search in default browser
search()

#Future todo: 
# save searched links to a file ;)