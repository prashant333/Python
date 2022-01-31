# this is a web scrapping python code
import requests
from bs4 import BeautifulSoup as bs

github_user = input("Enter the github user name: ")
url = "https://github.com/" + github_user
r = requests.get(url).text
soup = bs(r, 'html.parser')
profile_pic = soup.find('img', class_='avatar avatar-user width-full border color-bg-default')['src']
print(profile_pic)

"""
soup = bs(r.content, 'html.parser')
profile_img = soup.find('img', {'alt': 'Avatar'})['src']
print(profile_img)
"""
