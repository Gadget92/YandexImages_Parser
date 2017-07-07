import urllib.request
import os
save_path = "D:\\Wallpapers\\Yandex\\"
screen_size = ["1920x1200", "1920x1080", "1280x1024"]

def saveTodayImage(ImageName):
    for screen in screen_size:
        url = 'https://yandex.by/images/today?size=' + screen
        if not os.path.exists(save_path+str(screen)):
            os.makedirs(save_path+str(screen))
        fullPath = os.path.join(save_path+str(screen), str(screen)+".jpg")
        urllib.request.urlretrieve(url, fullPath)

def GetTodayImageName():
    TodayImageName = ""

    return TodayImageName