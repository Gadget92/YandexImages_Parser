import urllib.request
import platform
import requests
import os
import configparser
# from lxml import html

from bs4 import BeautifulSoup

SAVE_PATH_WIN = "D:\\Wallpapers\\Yandex\\"
SAVE_PATH_NIX = "/home/gadget/Изображения/"
SCREEN_SIZE = ["1920x1200", "1920x1080", "1280x1024"]

def saveTodayImage(ImageName, save_path):
    for screen in SCREEN_SIZE:
        url = 'https://yandex.by/images/today?size=' + screen
        if not os.path.exists(save_path + str(screen)):
            os.makedirs(save_path + str(screen))
        fullpath = os.path.join(save_path + str(screen), ImageName + ".jpg")
        if not os.path.exists(fullpath):
            urllib.request.urlretrieve(url, fullpath)
            print('Image succesful saved, size: ' + str(screen))
        else:
            print('Today this image was saved')

def GetTodayImageName():
    NAME_URL = "https://yandex.by/images/"
    r = requests.get(NAME_URL)
    soup = BeautifulSoup(r.text, "html.parser")
    TodayImageName = soup.find('span', {'class': 'b-501px__name'}).text
    return TodayImageName

def GetSavePath():
    #Get os type
    if platform.system() == 'Windows':
        return SAVE_PATH_WIN
    else:
        return SAVE_PATH_NIX

def SaveImage():
    ImageName = GetTodayImageName()
    if ImageName != "":
        saveTodayImage(ImageName, GetSavePath())

if __name__ == "__main__":
    SaveImage()
