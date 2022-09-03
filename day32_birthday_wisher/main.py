#To run and test the code you need to update 4 places:
# 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# 2. Go to your email provider and make it allow less secure apps.
# 3. Update the SMTP ADDRESS to match your email provider.
# 4. Update birthdays.csv to contain today's month and day.
# See the solution video in the 100 Days of Python Course for explainations.


from datetime import datetime
import pandas
import random
import smtplib

MY_EMAIL = "YOUR EMAIL"
MY_PASSWORD = "YOUR PASSWORD"

today = datetime.now()
today_tuple = (today.month, today.day)

df = pandas.read_csv("birthdays.csv")
birth_dict = {
    (row["month"], row["day"]): row 
    for (idx, row) in df.iterrows()
    }

if today_tuple in birth_dict:
    person = birth_dict[today_tuple]
    fpath = f"letter_templates/letter_{random.randint(1,3)}.txt"
    
    with open(fpath) as f:
        contents = f.read()
        contents = contents.replace("[NAME]", person["name"])

    with smtplib.SMTP("YOUR EMAIL PROVIDER SMTP SERVER ADDRESS") as conn:
        conn.starttls()
        conn.login(MY_EMAIL, MY_PASSWORD)
        conn.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=person["email"],
            msg=f"Subject:Happy Birthday!\n\n{contents}"
        )
