import requests
from bs4 import BeautifulSoup

def Connect(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    return soup

out = open('output.txt', 'w', encoding='utf-8')

pageid = 1
pagetoparse = int(input("Enter the count of pages to parse: "))

url = input('Enter a website to parse: ')

soup = Connect(url)

while pageid < pagetoparse:
    
    if pageid > 1:
        soup = Connect(url + 'page' + str(pageid))
        print(url + 'page' + str(pageid))

    for article in soup.find_all('div', {'class': 'tm-article-snippet'}):
        try:
            author = article.find('a', {'class': 'tm-user-info__username'}).text
            link = article.find('a', {'class': 'tm-article-snippet__title-link'})
            title = link.find('span').text
            out.write(author + title + ' - ' + ('https://habr.com' + link.get('href')) + '\n')
        except Exception as e:
            print(e)
    pageid += 1

out.close()