import urllib.request
import platform
import requests
import os
from bs4 import BeautifulSoup
from lxml import html

SAVE_PATH_WIN = "D:\\Wallpapers\\Yandex\\"
SAVE_PATH_NIX = "/home/gadget/Изображения/"
SCREEN_SIZE = ["1920x1200", "1920x1080", "1280x1024"]

def saveTodayImage(ImageName, save_path):
    for screen in SCREEN_SIZE:
        url = 'https://yandex.by/images/today?size=' + screen

        if not os.path.exists(save_path + str(screen)):
            os.makedirs(save_path + str(screen))
        fullpath = os.path.join(save_path + str(screen), ImageName + ".jpg")
        urllib.request.urlretrieve(url, fullpath)
        print('Image succesful saved')

def GetTodayImageName():
    NAME_URL = "https://yandex.by/images/"
    r = requests.get(NAME_URL)
    # Save html to file
    # with open('test.html', 'w', encoding='utf-8') as output:
    #     output.write(r.text)
    soup = BeautifulSoup(r.text)
    TodayImageName = soup.find('span', {'class': 'b-501px__name'}).text

    return TodayImageName


#Get os type
if platform.system() == 'Windows':
    path_to_save = SAVE_PATH_WIN
else:
    path_to_save = SAVE_PATH_NIX

ImageName = GetTodayImageName()

if ImageName != "":
    saveTodayImage(ImageName, path_to_save)

