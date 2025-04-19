from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
import pandas as pd
import time


service = Service("D:/indirilenler/geckodriver.exe")  
driver = webdriver.Firefox(service=service)


url = 'https://www.ilan.gov.tr/ilan/kategori/73/akademik-personel-alimlari'
driver.get(url)
time.sleep(5)  
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(5) 



ilanlar = driver.find_elements(By.CSS_SELECTOR, 'div.search-results-row')

veri = []
for ilan in ilanlar:
    try:
        baslik = ilan.find_elements(By.CLASS_NAME, 'col')[1].text.strip()
        sehir = ilan.find_elements(By.CLASS_NAME, 'col')[3].text.strip()
        veri.append({
            'Başlık': baslik.strip(),
            'Şehir': sehir.strip(),
        })
    except:
        continue


driver.quit()


df = pd.DataFrame(veri)


print(df.head(10))
print(f"Bulunan ilan sayısı: {len(ilanlar)}")

"""
python academic_info.py
                                              Başlık     Şehir
0  Yeditepe Üniversitesi Rektörlüğü Öğretim Elema...  İSTANBUL
1  Yeditepe Üniversitesi Rektörlüğü Öğretim Üyesi...  İSTANBUL
2  İbn Haldun Üniversitesi Rektörlüğü Öğretim Üye...  İSTANBUL
3  İstanbul Sağlık ve Teknoloji Üniversitesi Rekt...  İSTANBUL
4  Düzeltme İlanı ( İstanbul Beykent Üniversitesi...  İSTANBUL
5  Yaşar Üniversitesi Rektörlüğü Araştırma Görevl...     İZMİR
6  Atılım Üniversitesi Rektörlüğü Öğretim Üyesi A...    ANKARA
7  İstanbul Rumeli Üniversitesi Araştırma Elemanı...  İSTANBUL
8  İstanbul Rumeli Üniversitesi Öğretim Üyesi Alacak  İSTANBUL
9    Nişantaşı Üniversitesi Akademik Personel Alacak  İSTANBUL
Bulunan ilan sayısı: 12

------------------------------------------------------------
from fetch_listings import fetch_job_listings
from email_notifier import send_email
from config import TARGET_CITY

def main():
    listings = fetch_job_listings()
    for listing in listings:
        if listing['Şehir'] == TARGET_CITY:
            send_email("İlan Bilgisi", f"Başlık: {listing['Başlık']}\nŞehir: {listing['Şehir']}")
            break

if __name__ == "__main__":
    main()

-->> ilanlardan ilk eşleşen bir ilanı bulup mail atacak.
"""
