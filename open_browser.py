import webbrowser
import urllib.request

url = 'http://localhost:8000'
try:
    urlstatus = urllib.request.urlopen(url).getcode()
except:
    y = input("Do you want to open browser (Y/N)... ").upper()
    if y[0] == 'Y':
        webbrowser.open(url)
