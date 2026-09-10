import datetime
import random
import smtplib
from email.message import EmailMessage

now = datetime.datetime.now()
weekday = now.weekday()

if weekday == 3:
    with open("quotes.txt", encoding="utf-8") as quote_file:
        all_quotes = quote_file.readlines()
        selected_quote = random.choice(all_quotes)

    email_msg = EmailMessage()
    email_msg["Subject"] = "Thursday Motivation"
    email_msg["From"] = MY_EMAIL
    email_msg["To"] = MY_EMAIL
    email_msg.set_content(selected_quote)

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, PASSWORD)
        connection.send_message(email_msg)
