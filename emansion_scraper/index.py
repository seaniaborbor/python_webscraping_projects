from bs4 import BeautifulSoup 
import requests
html_text = requests.get("https://www.emansion.gov.lr/2content_a.php?sub=82&related=30&third=82&pg=sp").text
job_list = BeautifulSoup(html_text, 'lxml')
jobs = job_list.find("ol", {"id": "doclist"})
job = jobs.find_all('li')
for opening in job:
	print(opening.find('a').text)
	print(opening.find('div',{"id": "newsdate"} ).text)
	print("........................................")
