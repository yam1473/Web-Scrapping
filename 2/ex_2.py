
import requests
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/Pawe%C5%82_Domaga%C5%82a'
resp = requests.get(url)
soup = BeautifulSoup(resp.content, 'html.parser')

#Extact Pawel's date of birth
Pawel_dob = soup.find('span', {'class': 'bday'}).text
print("Pawel's DOB is ", Pawel_dob)

#Extract Pawe l's three occupations
Pawel_occu = [li.text for li in soup.find('div', {'class': 'hlist'}).find_all('li')]
print("Pawel's Occupation is ", Pawel_occu)

#Extract the list of references
Pawel_ref = [a.text for a in soup.find_all('span', {'class': 'reference-text'})]
print("Pawel's reference list ", Pawel_ref)
