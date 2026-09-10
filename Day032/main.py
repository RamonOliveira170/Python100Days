import smtplib
import datetime
import pandas

'''with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="salebat170@gmail.com",
        msg="Subject:Happy birthday\n\n"
            "Hello")'''

now = datetime.datetime.now()
print(now.weekday())
print(now)
