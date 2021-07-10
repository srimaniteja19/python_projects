import requests
from bs4 import BeautifulSoup
from simple_chalk import chalk
res = requests.get('https://news.ycombinator.com/')

soup = BeautifulSoup(res.text, 'html.parser')
# print(soup.body)
# print(soup.find_all('a'))
s = soup.select('.score')
story = soup.select('.athing')
tags = []
for i in s:
    points = i.text
    point = points.index('p')
    p = points[0:point]
    if(int(p) >= 100):
        tags.append(i['id'])

story_id = []
r_tags = []
for i in tags:
    x  =i.index('_')
    r_tags.append(i[x+1:])

z_tags = list(map(lambda x: int(x), r_tags))  

for i in story:
    # print(i.select('.storylink'))
    if int(i['id']) in z_tags:
        story_id.append(int(i['id']))
result = []
for i in story:
    if int(i['id']) in story_id:
        t = i.find('a','storylink')
        print(f"{chalk.yellow.bold(t.text)} {chalk.magenta.dim(t['href'])}")     
        print()     