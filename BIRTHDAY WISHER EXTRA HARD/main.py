
import pandas as pd
import datetime as dt
import smtplib
import random
import os

birthdays = pd.read_csv("birthdays.csv")

now = dt.datetime.now()
year = now.year
month = now.month
day = now.day

letter_templates = "./letter_templates"
letters_sent = "./letters_sent"

txt_files = [file for file in os.listdir(letter_templates) if file.endswith(".txt")]

my_email = "alberto.python.73@gmail.com"
my_password = "kdpiumbxmcdegbgj"

if not os.path.exists(letters_sent):
    os.makedirs(letters_sent)

for _, row in birthdays.iterrows():
    if row["month"] == month and row["day"] == day:
        random_file = random.choice(txt_files)
        with open(f"{letter_templates}/{random_file}") as file:
            read_file = file.read()
        new_letter = read_file.replace("[NAME]", row["name"])

        output_path = f"{letters_sent}/birthday_letter_for_{row['name']}.txt"

        with open(output_path, "w") as new_file:
            custom_letter = new_file.write(new_letter)

        with open(output_path) as file:
            letter_for_mail = file.read()

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            # SECURE OUR CONNECTION
            connection.starttls()

            # LOGIN INTO MY ACCOUNT
            connection.login(user=my_email, password=my_password)

            # SEND EMAIL
            connection.sendmail(from_addr=my_email,
                                to_addrs=f"{row['email']}",
                                msg=f"Subject:Happy birthday, {row['name']}!\n\n {letter_for_mail}")









