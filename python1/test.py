import urllib.request

def fillUserNamePassword() -> bool:
    userName = '102817874909'
    password = '29am31fr'
    webUrl = urllib.request.urlopen('https://selfcare.actcorp.in/web/blr/home')
    #content = str(webUrl.read())
    print(str(webUrl.read()))


fillUserNamePassword()

