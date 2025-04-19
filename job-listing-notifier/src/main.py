from fetch_listings import fetch_job_listings
from email_notifier import send_email
from config import TARGET_CITY

def main():
    listings = fetch_job_listings()
    filtered = [l for l in listings if l['Şehir'].strip().lower() == TARGET_CITY.lower()]
    if filtered:
        body = ""
        for i, listing in enumerate(filtered, 1):
            body += f"{i}. Başlık: {listing['Başlık']}\n   Şehir: {listing['Şehir']}\n\n"
        send_email("İlan Bilgileri", body)
    else:
        print("Seçilen şehirde ilan yok.")

if __name__ == "__main__":
    main()