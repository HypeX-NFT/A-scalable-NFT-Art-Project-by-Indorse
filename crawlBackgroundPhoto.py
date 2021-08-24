import requests
from bs4 import BeautifulSoup
import os

url = 'https://www.google.com/search?q=cyberpunk+2077&sxsrf=ALeKk00Jm6IYhs-xixcvPb6b-o1qkqAHcA:1629243708755&source=lnms&tbm=isch&sa=X&ved=2ahUKEwi8tozknbnyAhUVHc0KHd_SAKUQ_AUoBHoECAEQBg&biw=1280&bih=946'

r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

images = soup.find_all('img')
# for image in images:
#     print(image['src'])