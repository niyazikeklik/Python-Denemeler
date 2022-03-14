from ast import Str
from operator import contains
from typing import List
from asyncore import read
import os
import sys
import time
import json
from webbrowser import get

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


liste = []
os.system('cls')
print("Ortam hazırlanıyor..")
application_path = ""
application_path = os.path.dirname(os.path.abspath(__file__))
driver_path = application_path+"\\chromedriver.exe"
optionss = Options()
# optionss.add_argument('--headless')
optionss.add_argument('--disable-gpu')  # Last I checked this was necessary.
print("Ortam başlatılıyor..")
browser = webdriver.Chrome(executable_path=driver_path, options=optionss)
kullaniciadi = ""
sifre = ""


def JSExecute(komut):
    count = 0
    Execute = True
    while(Execute):
        try:
            return browser.execute_script(komut)
        except:
            count += 1
            time.sleep(0.1)
            if(count > 20):
                return False
            Execute = True


def ReturnJSExecute(komut):
    Execute = True
    while(Execute):
        try:
            return browser.execute_script(komut)
        except:
            Execute = True


def Kaydir():
    oncekikonum = ReturnJSExecute(
        "return document.body.getBoundingClientRect().top;")
    time.sleep(0.02)
    JSExecute("window.scrollTo(0,document.body.scrollHeight);")
    time.sleep(0.2)
    sonrakikonum = ReturnJSExecute(
        "return document.body.getBoundingClientRect().top;")
    if(oncekikonum == sonrakikonum):
        return True
    return False


kisiler = ""


def InstagramLogin():
    print("Adrese yönlendiriliyor..")

    browser.get("https://www.instagram.com")
    os.system('cls')
    kullaniciadi = input("Kullanıcı adı: ")
    time.sleep(3)
    browser.find_element_by_name("username").send_keys(kullaniciadi)
    sifre = input("Sifre: ")
    browser.find_element_by_name("password").send_keys(sifre)
    browser.find_element_by_xpath(
        "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button/div").click()
    print("Giriş yapılıyor..")
    time.sleep(5)
    print("Adrese yönlendiriliyor..")
    browser.get(
        "https://www.instagram.com/accounts/access_tool/current_follow_requests")
    os.system('cls')


def KisileriAl():
    global kisiler
    print("Liste oluşturuluyor..")
    while(True):
        kisisayisi = ReturnJSExecute(
            "return document.getElementsByClassName(\"-utLf\").length;")
        for i in range(0, kisisayisi):
            siradakikisi = ReturnJSExecute(
                "return document.getElementsByClassName(\"-utLf\")["+str(i)+"].innerText;")
            if not siradakikisi in liste:
                liste.append(siradakikisi)
                kisiler = kisiler + siradakikisi + ";"
                print(str(len(liste)) + ". Bulundu: " + siradakikisi)
        if JSExecute("return document.getElementsByClassName(\"sqdOP  L3NKy   y3zKF     \").length > 0"):
            JSExecute("document.getElementsByClassName(\"sqdOP  L3NKy   y3zKF     \")[0].click();")
        else:
            break
        Kaydir()
    f = open("takipetmeyenler.txt", "w")
    f.write(kisiler)
    f.close()
    print("Liste oluşturuldu..")


def İsteklerisil():
    time.sleep(2.5)
    listeelemansayisi = len(liste)
    count = 0
    for kisi in liste:
        count += 1
        sayac = 0
        sayac =  TakiptenCik(kisi)
        print(str(count)+"/"+str(listeelemansayisi) + " | " + str(sayac * 5) + " saniyede silindi: " + kisi)
        if not sayac == 0: 
            time.sleep(40 - (sayac % 8) * 5) 

    print("Bulunan tüm hesaplar ("+str(count) +
          ") silindi! Kontrol amaçlı tekrar çalıştırabilirsiniz.")


def TakiptenCik(kisi, sayac=0):
    browser.get("https://www.instagram.com/"+kisi)
    if "Takip Et" not in str(JSExecute("return document.getElementsByClassName(\"sqdOP  L3NKy\")[0].innerText;")):
        if str(JSExecute("return document.getElementsByClassName(\"sqdOP  L3NKy    _8A5w5    \").length;")) != "0":
            JSExecute(
                "document.getElementsByClassName(\"sqdOP  L3NKy    _8A5w5    \")[0].click()")
            JSExecute(
                "document.getElementsByClassName(\"aOOlW -Cab_   \")[0].click()")
            time.sleep(5)
            return TakiptenCik(kisi, sayac = sayac + 1)
    else:
        return sayac


InstagramLogin()
f = open("takipetmeyenler.txt", "r")
list_json = f.read().split(";")
print(len(list_json))
if (len(list_json) <= 3):
    KisileriAl()
else:
    liste = list_json
İsteklerisil()
browser.quit()
