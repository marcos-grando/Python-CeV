from urllib import request

try:
    site = request.urlopen('https://www.pudim.com.br')
except: 
    print("Not'on")
else:
    print("Ye'on")