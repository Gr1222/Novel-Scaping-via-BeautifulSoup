Here's a piece of python code to scrape the body text of novels on the Chinese website晋江文学城. 
Be reminded: it only works for FREE novels (sadly)
The idea is that although many websites provide online reading of novels, but sometimes we want to download them. I can find many .txt versions of the popular novels (those that need vip) but the less popular ones (also free) have much less related resources.
This is why I wrote this very simple program, so that I can download the novel into .txt, which is the most accessible text file, then it can be converted into various forms such as .mobi to read on my kindle.
If anyone wants to use it for the same purpose or build upon it, you are mostly welcome!Just change the [homeurl] to the link of the homepage of the novel!

Encoding problem:
  A big problem is that the website uses the charset "gb18030", although the program works for the specific novel I tested it with, it sometimes return garbled text when I tested it a vip novel.
  It seems to work for the free novels I tried, however, be aware of this problem!
