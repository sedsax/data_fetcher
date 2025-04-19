# Job Listing Notifier

This project is designed to scrape job listings from a specified website, check for listings from İstanbul, and send email notifications if such listings are found. It is intended to run weekly without manual intervention.

## Project Structure

```
job-listing-notifier
├── src
│   ├── main.py              # Entry point of the application
│   ├── fetch_listings.py    # Functions to scrape job listings
│   ├── email_notifier.py     # Functions to send email notifications
│   └── config.py            # Configuration settings
├── requirements.txt          # Project dependencies
└── README.md                 # Project documentation
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd job-listing-notifier
   ```

2. **Install dependencies:**
   Make sure you have Python installed. Then, run:
   ```
   pip install -r requirements.txt
   ```

3. **Configure email settings:**
   Edit the `src/config.py` file to include your email credentials and the target email address.

4. **Run the application:**
   You can run the application manually by executing:
   ```
   python src/main.py
   ```

## Usage

The script will fetch the first 10 job listings from the specified website, check if any of them are from İSTANBUL, and send an email notification if such listings are found.

## Scheduling

To run the script weekly without manual intervention, you can use a task scheduler:

- **On Unix-based systems:** Use `cron` to schedule the script.
- **On Windows:** Use Task Scheduler to execute `src/main.py` at the desired interval.
