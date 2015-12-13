#!/usr/bin/env python

from bs4 import BeautifulSoup
import requests
import pickle
import time

def fetchSoup(url):
	
	print("[*] Fetching URL : %s" % url)
	r = requests.get(url)
	soup = BeautifulSoup(r.content, "lxml")
	return soup

def PLoader(filename):

	with open(filename, "rb") as f:
		data = pickle.load(f)
	return data

def PWriter(filename, data):
	
	with open(filename, "wb") as f:
		pickle.dump(data, f)

def sleeper(t, m=10):
	time.sleep(t)

def reStructer(tb):
	
	head = [u'Singular', u'Singular', u'Plural', u'Plural']
	
	transPose = list(zip(*tb[2:]))
	category  = list(zip(tb[1][1:], transPose[1:]))
	
	return list(zip(head, category))
	
