from bs4 import BeautifulSoup
import requests

######   Scrape titles of trending on homepage of github.com/trending   ######
# page = requests.get('https://github.com/trending')
# soup = BeautifulSoup(page.text, 'html.parser')
# article = soup.find('article')
# # print(article.prettify())
# title = article.find('h1', 'h3 lh-condensed')
# titleww = title.a.text
# print(''.join(titleww.split()))

######   Scrape titles of articles on homepage of space.com   ######
# page = requests.get('https://www.space.com/')
# soup = BeautifulSoup(page.text, 'html.parser')
# for div in soup.find_all('figcaption'):
#     figcaption = div.find('span', class_='article-name')
#     print(figcaption.text)


######   Scrape names of "car" search, from trademe.co.nz   ######
# page = requests.get('https://www.trademe.co.nz/Browse/SearchResults.aspx?searchString=cars&type=Search&searchType=all&user_region=100&user_district=0&generalSearch_keypresses=4&generalSearch_suggested=0&generalSearch_suggestedCategory=')
# soup = BeautifulSoup(page.text, 'html.parser')
# for div in soup.find_all('div', class_='tmm-sf-search-card-list-view__details'):
#     car = div.find('div', class_='tmm-sf-search-card-list-view__title tmm-sf-search-card-list-view__title--bold').text
#     #print(''.join(car.split()))
#     print(car.strip())


######   Top 10 blogs   ######

###### Scrape latest articles from the Engadget homepage
page = requests.get('https://www.engadget.com/')
soup = BeautifulSoup(page.text, 'html.parser')

#first blog is structured differently to rest so is scraped seperately
blogone = soup.find('div', class_='o-thumb_overlay_desc@tp+ bg-white@tp+ c-gray-0@tp+ absolute@tp+ b-0 r-0 pt-20@tl pt-30@tp+ pl-40@tp+').span.text
print(blogone.strip())

#other blogs are strucutured the same so are scraped together
for otherblogs in soup.find_all('div', class_='border-top@m+ mt-40@m+ pt-40@m+'):
    title = otherblogs.find('span', class_='th-underline').text
    print(title.strip())