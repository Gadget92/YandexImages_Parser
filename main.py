import urllib.request
import os

SAVE_PATH = "D:\\Wallpapers\\Yandex\\"
SCREEN_SIZE = ["1920x1200", "1920x1080", "1280x1024"]

def saveTodayImage(ImageName):
    for screen in SCREEN_SIZE:
        url = 'https://yandex.by/images/today?size=' + screen
        if not os.path.exists(SAVE_PATH + str(screen)):
            os.makedirs(SAVE_PATH + str(screen))
        fullpath = os.path.join(SAVE_PATH + str(screen), str(screen) + ".jpg")
        urllib.request.urlretrieve(url, fullpath)

def GetTodayImageName():
    NAME_URL = "https://yandex.by/images/"
    # Need add parse image name
    TodayImageName = ""

    return TodayImageName


ImageName = GetTodayImageName()
if ImageName != "":
    saveTodayImage(ImageName)