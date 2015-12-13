#!/usr/bin/env python

import utils
import parser

data = []
url = "https://en.wiktionary.org/wiki/Category:Faroese_nouns"
while True:

	# fetching and creating soup
	soup = utils.fetchSoup(url)
	# div housing the words
	page = soup("div", {"id" : "mw-pages"})
	
	# word groups
	groups = page[0]("div", {"class" : "mw-category-group"})

	# traverse of very group and extract data into groupD
	for g in groups:

		words = [(unicode(i("a")[0].string), i("a")[0]["href"]) for i in g("li")]
		categ = unicode(g("h3")[0].string)
		
		data.extend(words)
		print("[*] Letter %s has %d words" % (categ, len(words)))

	# extract url for next page
	links = page[0]("a")
	nextL = [x for x in links if x.string=="next page"]
	if len(nextL) == 0:
		print("Done Scraping!")
		break
	url   = "https://en.wiktionary.org" + nextL[0]["href"]
	
	print("-"*20)
	utils.sleeper(3)
	# break

utils.PWriter("FaroeseWordsLinks.p", data)
print("+-"*20)
# faroeseData = parser.parseDataFromIndiWords(data)
# utils.PWriter("FaroeseNounsData.p", faroeseData)

result = []
f = open("FaroeseNounsData.speling", "w")

for d in data:
	fData = parser.parseDataFromIndiWords([d])
	
	# Empty Table condition
	if len(fData) == 0: continue
	# converting into spelling format
	cases = parser.caseExtractor(fData[0])
	splFt = parser.spellingFormater(fData, cases)
	# result.extend(splFt)
# with open("FaroeesNounsData.spelf", "w") as f:
	for s in splFt:
		f.write(unicode(s+"\n").encode("utf-8"))
	f.flush()
f.close()
