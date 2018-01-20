import re
import csv
import requests
import io
from bs4 import BeautifulSoup

# load webpage
url = 'https://www.creepypasta.com/loss-alive/'
response = requests.get(url)
html = response.content
soup = BeautifulSoup(html, "lxml")

# get links to different stories
links = []
for link in soup.find_all('a', href=re.compile('https')):
    if ("random" in link.text):
	    links.append(link['href'])
	    # print(link['href'])
# print(links)

# get text
text = []
textCount = 0;
for element in soup.find_all('p'):
	text.append(element.text)
	textCount += len(element.text)
	# print(element.text)
# print(text)
# print (textCount)

# keep crawling through different random links untill text[] is over 1500 lines
while (textCount < 150000):
	print('Going to: ', links[1])
	url = links[1]
	response = requests.get(url)
	html = response.content
	soup = BeautifulSoup(html, "lxml")
	
	# get links to different stories
	links = []
	for link in soup.find_all('a', href=re.compile('https')):
		if ("random" in link.text):
			links.append(link['href'])
	
	for element in soup.find_all('p'):
		text.append(element.text)
		textCount += len(element.text)

# write the output to the file
with io.open("creepy.txt", "w", encoding="utf-8") as file:
    for item in text:
	    file.write("%s\n" % item)
	
file.close()

# FAILED ATTEMPTS - useful for future use
# text = soup.get_text()
# for element in soup.find_all('div', attrs={"class" : "general"})
# print(text)
