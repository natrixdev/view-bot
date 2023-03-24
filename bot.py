import webbrowser
import time

# Your tiktok video URL
url = "https://www.tiktok.com/@natrixofficiel/video/7204193932475944198"

# Number of views you want
num = 100

views=0
for i in range(num):
    webbrowser.open(url, new=2) 
    views=views+1
    print("[+] New view - View amounnt :"+str(views))
    time.sleep(0.1) 
print(str(num) + " views sended")
    
