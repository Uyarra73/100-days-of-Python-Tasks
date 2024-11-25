import smtplib
import datetime as dt
import random

now = dt.datetime.now()
year = now.year
month = now.month
day_of_the_week = now.weekday()

my_email = "alberto.python.73@gmail.com"
my_password = "kdpiumbxmcdegbgj"

print(day_of_the_week)


with open("quotes.txt") as file:
    quotes = file.read().splitlines()
    random_quote = random.choice(quotes)
    print(random_quote)

#EMAIL PROVIDER
if day_of_the_week == 0:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:

        # SECURE OUR CONNECTION
        connection.starttls()

        # LOGIN INTO MY ACCOUNT
        connection.login(user=my_email, password=my_password)

        # SEND EMAIL
        connection.sendmail(from_addr=my_email,
                            to_addrs="albi.python73@yahoo.com",
                            msg=f"Subject:Monday motivation quote!\n\n {random_quote}")













