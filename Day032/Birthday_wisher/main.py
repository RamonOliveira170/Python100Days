import smtplib
import pandas
import datetime
import random
from email.message import EmailMessage

today = datetime.datetime.now()
today_tuple = (today.month, today.day)
data = pandas.read_csv("birthdays.csv")
birthdays = {(data_row["month"], data_row["day"]): data_row  for (index, data_row) in data.iterrows()}

if today_tuple in birthdays:
    birthday_person = birthdays[today_tuple]
    file_path = f"./letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", f"{birthday_person["name"]}")

    email_msg = EmailMessage()
    email_msg["Subject"] = f"Happy birthday"
    email_msg["From"] = MY_EMAIL
    email_msg["To"] = birthday_person["email"]
    email_msg.set_content(contents)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, PASSWORD)
        connection.send_message(email_msg)
