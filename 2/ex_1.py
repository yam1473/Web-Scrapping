import requests
from bs4 import BeautifulSoup

url = 'http://www.pythonscraping.com/pages/page3.html'

resp = requests.get(url)
bs = BeautifulSoup(resp.content, 'html.parser')

#Extract bolded parts of the text
bold_title= [h.text for h in bs.findAll("h1")]
bold_desc= [th.text[1:-1] for th in bs.findAll("th")]
bold_table = [b.text for b in bs.findAll("span", { "class" : "excitingNote" })]
bold_text = bold_title + bold_desc + bold_table
print("\n")
print("Bold Texts: ", bold_text)

#Extract the last Item Title from the table
title = [tr.text for tr in bs.findAll("tr",{ "class" : "gift" })]
last_title = str(title[-1]).split('\n')[1]
print("\n")
print("Last Item: ",last_title)

#Extract the footer of the webpage
footer = [f.text for f in bs.findAll("div", { "id" : "footer" })]
print("\n")
print("Footer: ", footer[0])


