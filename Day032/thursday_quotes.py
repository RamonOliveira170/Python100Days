import datetime
import random
import smtplib

MY_EMAIL = "ramonoliveirasantos170@gmail.com"
PASSWORD = "rjzbxfdsljzaaqgg"

now = datetime.datetime.now()
weekday = now.weekday()

if weekday == 3:
    with open("quotes.txt", encoding="utf-8") as quote_file:
        all_quotes = quote_file.readlines()
        selected_quote = random.choice(all_quotes)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject: Thursday Motivation\n\n"
                f"{selected_quote}")
