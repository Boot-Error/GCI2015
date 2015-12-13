#!/usr/bin/env python

import utils

def parseDataFromIndiWords(data):

	declesions = []
	for word, url in data:
	
		domain = "https://en.wiktionary.org%s"
		page   = utils.fetchSoup(domain % url)
	
		try:	
			table = page("table", {"class" : "prettytable"})[0]
			# print(str(table)[30:50])
			nouns  = [unicode(i.string) for i in page("ol")[0]("a")]
			print(nouns)
			gender = unicode(page("span", {"class" : "gender"})[0].string)
			print(gender)
		except:
			print("[+] Table for word : %s not found!" % word)
			table, nouns = [], []

		# processing begins here
		try:
			tableProcd  = [[unicode(k.string) for k in j("td")] for j in table("tr")]
			print("[+] Word %s has %d nouns" % (word, len(nouns)))
			declesions.append((word, nouns, tableProcd, gender))
		except Exception as e:
			print(e)
			print("[!] Seems like there exists No required Data, SKIP!")
		utils.sleeper(3)
		# break
	return declesions

def spellingFormater(data, case):
	
	# extract into tuples
	resultT = []
	for word, nouns, table, g in data:
		t2 = utils.reStructer(table)
		for a, b in t2:
			for w in set(b[1]):
				dataTuple = (word, w, a, b[0], g)
				resultT.append(dataTuple)

	prop = {
		"Singular"   : "sg",
		"Plural"     : "pl",
		"Indefinite" : "ind",
		"Definite"   : "def",
		"Nominative" : "nom",
		"Accusative" : "acc",
		"Dative"     : "dat",
		"Genitive"   : "gen"
	}
	# convert into string format recognised as spelling format
	out = []
	for t in resultT:
		
		stringF = "%s; %s;" % (t[0], t[1])
		for c in set([x[1] for x in case if x[0] == t[1]]):
			propty  = (prop[t[-3]], prop[t[-2]], prop[c])	
			out.append(stringF + " %s.%s.%s" % propty + "; n." + t[-1])
	
	return out

def caseExtractor(data):
	
	r = []
	for i in data[2][2:]:
		for j in i[1:]:
			r.append((j, i[0]))

	return r
