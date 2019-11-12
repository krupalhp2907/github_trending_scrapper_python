import requests
from bs4 import BeautifulSoup


page = requests.get('https://github.com/trending')


soup = BeautifulSoup(page.text, 'html.parser')


repo = soup.find(class_="repo-list")

lh=soup.find_all(class_="h3 lh-condensed")
descrip=soup.find_all(class_="col-9 text-gray my-1 pr-4")
#for div in lh:
#    print(div.find("a")['href'])
#for de in desc:
#    print(de.text)

print(len(lh))


file_name = "github_trending_today.csv"
f = csv.writer(open(file_name, 'w', newline=''))



for i in range(len(lh)):
    desc=lh[i].find("a")['href'].split("/")
    repo_name=desc[1]
    author=desc[2]
    repo_desc=descrip[i].text.strip()
    for value in repo_desc:
        if not 33<=ord(value)<=126:
            repo_desc="Nothing to display"
            break
    print('Name:', repo_name)
    print('Author: ', author)
    print('Repo-Desc:', repo_desc)
