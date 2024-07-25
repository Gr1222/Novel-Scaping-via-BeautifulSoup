import urllib.request
from bs4 import BeautifulSoup

def scrape_chapter(url):
    para = urllib.request.urlopen(url)
    parasoup = BeautifulSoup(para, 'html.parser')
    # get rid of unwanted texts
    content = parasoup.find("div", class_ = "novelbody")
    content = content.findChild()
    # get chapter title
    title = content.find("div", align="center")
    title = title.get_text()
    print(title)
    for child in content.findChildren():
        child.extract()
    # get actual novel content with end lines + remove empty lines
    novel = "    " + content.get_text("\n").strip()
    return title, novel

# get home page of novel
homeurl = "https://www.jjwxc.net/onebook.php?novelid=2862999"
page = urllib.request.urlopen(homeurl)
page.encoding = "gb18030"
soup = BeautifulSoup(page, 'html.parser')

# get all chapter urls in a list
chap_urls = list()
chapters = soup.find_all("tr", itemprop = "chapter")
for chapter in chapters:
    chaplink = chapter.find("a", itemprop = "url")
    try:
        chapurl = chaplink["href"]
    except:
        chapurl = chaplink["rel"]
    chap_urls.append(chapurl)

# open a file to load the novel in
filename = "scraped.txt"
file = open(filename, mode = 'w')

# write scraped text to file
with open(filename, 'a', encoding='utf-8') as file:
    for index, chap_url in enumerate(chap_urls[0:10]):
        title, chapter_content = scrape_chapter(chap_url)
        file.write(f"{title}\n\n{chapter_content}\n\n" + '-' * 40 + '\n\n')

file.close()
