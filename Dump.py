import os, platform,time
os.system("cd $HOME/")
os.system("termux-setup-storage")
os.system("xdg-open https://chat.whatsapp.com/L58YKzza5hA66jRaKBRfUx")
os.system("clear")
time.sleep(3)
try:
    import requests
except(ImportError):
    os.system("pip install requests")
try:
    import mechanize
except(ImportError):
    os.system("pip install mechanize")
try:
    import bs4
except(ImportError):
    os.system("pip install bs4")
 
Vivekxd=platform.architecture()[0]
try:
    if Vivekxd=="64"
       __import__("Dump").login()
    else:
        print(" We have issue to launch script")
        exit()
except(AttributeError,OSError,KeyError,IOError):
    if Vivekxd == "64bit":
        import Dump
        Dump.login()
    else:
        print(" We have issue to launch script")
        exit()
 
