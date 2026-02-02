# ch5_7_3.py
import bs4

htmlFile = "<div book-info='deepmind'>深智數位</div>"
objSoup = bs4.BeautifulSoup(htmlFile, 'lxml')
tag = objSoup.find(attrs={'book-info':'deepmind'})
print(tag)
print(tag.text)















