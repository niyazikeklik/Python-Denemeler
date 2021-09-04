import os
import sys
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

liste = []
os.system('cls')
print("Ortam hazırlanıyor..")
application_path=""
application_path = os.path.dirname(os.path.abspath(__file__))
driver_path = application_path+"\\chromedriver.exe"
optionss = Options()
#optionss.add_argument('--headless')
optionss.add_argument('--disable-gpu')  # Last I checked this was necessary.
print("Ortam başlatılıyor..")
browser = webdriver.Chrome(executable_path=driver_path,options=optionss)
kullaniciadi = ""
sifre = ""
def JSExecute(komut):
    count = 0
    Execute = True
    while(Execute):
        try:
            browser.execute_script(komut)
            return True
        except:
            count += 1
            time.sleep(0.1)
            if(count > 20):
                return False
            Execute=True

def ReturnJSExecute(komut):
    Execute = True
    while(Execute):
        try:
            return browser.execute_script(komut)
        except:
            Execute=True

def Kaydir():
    oncekikonum = ReturnJSExecute("return document.body.getBoundingClientRect().top;")
    time.sleep(0.15)
    JSExecute("window.scrollTo(0,document.body.scrollHeight);")
    time.sleep(0.4)
    sonrakikonum = ReturnJSExecute("return document.body.getBoundingClientRect().top;")
    if(oncekikonum == sonrakikonum):
        return True
    return False

def InstagramLogin():
    print("Adrese yönlendiriliyor..")
    browser.get("https://www.instagram.com")
    kullaniciadi = input("Kullanıcı adı giriniz: ")
    browser.find_element_by_name("username").send_keys(kullaniciadi)
    sifre = input("Sifre giriniz: ")
    browser.find_element_by_name("password").send_keys(sifre)
    browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button/div").click()
    print("Giriş yapılıyor..")
    time.sleep(2.5)
    print("Adrese yönlendiriliyor..")
    browser.get("https://www.instagram.com/accounts/access_tool/current_follow_requests")
    time.sleep(2.5)

def KisileriAl():
    print("Liste oluşturuluyor..")
    while(True):
        kisisayisi = ReturnJSExecute("return document.getElementsByClassName(\"-utLf\").length;")
        for i in range(0, kisisayisi):
            siradakikisi = ReturnJSExecute("return document.getElementsByClassName(\"-utLf\")["+str(i)+"].innerText;")
            if not siradakikisi in liste:
                liste.append(siradakikisi)
                print(str(len(liste))+ ". Bulundu: "+ siradakikisi)
        if not JSExecute("document.getElementsByClassName(\"sqdOP  L3NKy   y3zKF     \")[0].click();"):
            break
        Kaydir()
    print("Liste oluşturuldu..")
    

def İsteklerisil():
    listeelemansayisi= len(liste)
    count =0
    for kisi in liste:
        count +=1
        print(str(count)+"/"+str(listeelemansayisi) + " Siliniyor: "+ kisi)
        browser.get("https://www.instagram.com/"+kisi)
        time.sleep(0.3)
        JSExecute("document.getElementsByClassName(\"sqdOP  L3NKy    _8A5w5    \")[0].click()")
        JSExecute("document.getElementsByClassName(\"aOOlW -Cab_   \")[0].click()")
        time.sleep(0.2)
    os.system('cls')
    print("Bulunan tüm hesaplar ("+str(count)+") silindi! Kontrol amaçlı tekrar çalıştırabilirsiniz.")

InstagramLogin()
KisileriAl()
İsteklerisil()
browser.quit()
    

