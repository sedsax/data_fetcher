from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
import pandas as pd
import time

def fetch_job_listings():
    service = Service("D:/indirilenler/geckodriver.exe")  
    driver = webdriver.Firefox(service=service)

    url = 'https://www.ilan.gov.tr/ilan/kategori/73/akademik-personel-alimlari'
    driver.get(url)
    time.sleep(5)  
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5) 

    ilanlar = driver.find_elements(By.CSS_SELECTOR, 'div.search-results-row')

    veri = []
    for ilan in ilanlar[:10]:  # Limit to the first 10 listings
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
    return veri