import os, sys, urllib2, argparse, datetime, atexit
from bs4 import BeautifulSoup

addresses = []
deepestAddresses = []

maxLevel = 1
storeFolder = "Wikistore " + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))

undesirables = [ {"element" : "table", "attr" : {'class' : 'infobox'} }, {"element" : "table", "attr" : {'class' : 'vertical-navbox'}}, {"element" : "span", "attr" : {'class' : 'mw-editsection'}}, {"element" : "div", "attr" : {'class' : 'thumb'}}, {"element" : "sup", "attr" : {'class' : 'reference'}}, {"element" : "div", "attr" : {'class' : 'reflist'}}, {"element" : "table", "attr" : {'class' : 'nowraplinks'}}, {"element" : "table", "attr" : {'class' : 'ambox-Refimprove'}}, {"element" : "img", "attr" : None}, {"element" : "script", "attr" : None}, {"element" : "table", "attr" : {'class' : 'mbox-small'}} , {"element" : "span", "attr" : {"id" : "coordinates"}}, {"element" : "table", "attr" : {"class" : "ambox-Orphan"}}, {"element" : "div", "attr" : {"class" : "mainarticle"}}, {"element" : None, "attr" : {"id" : "References"}} ]

def init():
	parser = argparse.ArgumentParser(description='Handle the starting page and number of levels we\'re going to scrape')
	parser.add_argument('-URL', dest='link', action='store', help='The Wikipedia page from which we will start scraping')
	parser.add_argument('-levels', dest="levels", action='store', help='How many levels deep should the scraping go')
	args = parser.parse_args()

	if(args.levels != None):
		global maxLevel8
		maxLevel = int(args.levels)

	if(args.link == None):
		print("You need to pass a link with the -URL flag")
		sys.exit(0)
	else:
		if not os.path.exists(storeFolder):
			os.makedirs(storeFolder)

		grabPage(args.link, 0, args.link.split("/wiki/")[1].strip().replace("_", " "))

	atexit.register(cleanUp)

def isValidLink(link):
	
	if "/wiki/" in link and ":" not in link and "http://" not in link and "wikibooks" not in link and "#" not in link and "wikiquote" not in link and "wiktionary" not in link and "wikiversity" not in link and "wikivoyage" not in link and "wikisource" not in link and "wikinews" not in link and "wikiversity" not in link and "wikidata" not in link:
		return True
	else:
		return False

def grabPage(URL, level, name):

	opener = urllib2.build_opener()
	opener.addheaders = [('User-agent', 'Mozilla/5.0')]
	req = opener.open(URL)

	page = req.read()

	req.close()

	soup = BeautifulSoup(page, "html5lib", from_encoding="UTF-8")

	content = soup.find(id="mw-content-text")

	if hasattr(content, 'find_all'):

		global undesirables

		for notWanted in undesirables:

			removal = content.find_all(notWanted['element'], notWanted['attr'])
			if len(removal) > 0:
				for el in removal:
					el.extract()

		also = content.find(id="See_also")
		
		if(also != None):
			also.extract()
			tail = also.find_all_next()
			if(len(tail) > 0):
				for element in tail:
					element.extract()

		for link in content.find_all('a'):
			
			href = link["href"]

			if isValidLink(href):

				if level < maxLevel:

					stored = False;
					for addr in addresses:
						if addr == link.get("href"):
							stored = True

					if(stored == False):
						title = link.get('href').replace("/wiki/", "")
						addresses.append(str(title + ".html"))
						grabPage("http://en.wikipedia.org" + link.get('href'), level + 1, title)
						print title

			link["href"] = link["href"].replace("/wiki/", "") + ".html"
		
		fileName = str(name)

		if level == maxLevel:
			deepestAddresses.append(fileName.replace('/', '_') + ".html")

		doctype = "<!DOCTYPE html>"

		head = "<head><meta charset=\"UTF-8\" /><title>" + fileName + "</title></head>"

		f = open(storeFolder + "/" + fileName.replace('/', '_') + ".html", 'w')
		f.write(doctype + "<html lang=\"en\">" + head + "<body><h1>" + fileName + "</h1>" + str(content) + "</body></html>")
		f.close()

def cleanUp():

	print("\nRemoving links to pages that have not been saved\n")

	for deepPage in deepestAddresses:

		rF = open(storeFolder + "/" + deepPage, 'r')

		deepSoup = BeautifulSoup(rF.read(),  "html5lib", from_encoding="UTF-8")

		for deepLinks in deepSoup.find_all('a'):
			link = deepLinks.get("href")
			
			pageStored = False

			for addr in addresses:
				if addr == link:
					pageStored = True

			if pageStored == False:

				if link is not None:

					if '#' not in link:
						del deepLinks['href']
					elif '#' in link and len(link.split('#')) > 1 or ':' in link:
						del deepLinks['href']

		wF = open(storeFolder + "/" + deepPage, 'w')
		wF.write(str(deepSoup))
		wF.close()

	print("Complete")
		
if __name__ == "__main__":
	init()