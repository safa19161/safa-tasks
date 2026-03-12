# To run and test the code you need to update 4 places:
# 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# 2. Go to your email provider and make it allow less secure apps.
# 3. Update the SMTP ADDRESS to match your email provider.
# 4. Update birthdays.csv to contain today's month and day.
# See the solution video in the 100 Days of Python Course for explainations.
import smtplib
import pandas
import datetime as dt
import random
import os
now =  dt.datetime.now()
email = os.environ.get("my_email")
password = os.environ.get("my_password")
# email= "eerieboom@gmail.com"
# password = "zcqyaoqybzizdpto"

read = pandas.read_csv("birthdays.csv")
month = read["month"].tolist()
day = read["day"].tolist()




print(month,day)

if now.month in month and now.day in day:

    choose = random.choice(["letter_1.txt", "letter_2.txt", "letter_3.txt"])
    with open(choose, 'r') as msg:
        content = msg.read()
        name1 = read[(read.day == now.day) & (read.month == now.month)]
        name2 = name1.name.item()
        # one error left to resolve if two name1 found it will give again value error.

        letter = content.replace("[NAME]", name2)

    with smtplib.SMTP("smtp.gmail.com",587) as connection:


        email1 = read[(read.day == now.day) & (read.month == now.month)]
        email2 = email1.email.item()

        connection.starttls()
        connection.login(user=email, password=password)

        connection.sendmail(
            from_addr=email,
            to_addrs=f"{email2}",

            msg=f"subject:Happy Birthday\n\n{letter}")
else:
    print("no birthday")

# from datetime import datetime
# import pandas
# import random
# import smtplib
# import os

# # import os and use it to get the Github repository secrets
# MY_EMAIL = os.environ.get("MY_EMAIL")
# MY_PASSWORD = os.environ.get("MY_PASSWORD")

# today = datetime.now()
# today_tuple = (today.month, today.day)

# data = pandas.read_csv("birthdays.csv")
# birthdays_dict = {(data_row["month"], data_row["day"])                  : data_row for (index, data_row) in data.iterrows()}
# if today_tuple in birthdays_dict:
#     birthday_person = birthdays_dict[today_tuple]
#     file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
#     with open(file_path) as letter_file:
#         contents = letter_file.read()
#         contents = contents.replace("[NAME]", birthday_person["name"])

#     with smtplib.SMTP("YOUR EMAIL PROVIDER SMTP SERVER ADDRESS") as connection:
#         connection.starttls()
#         connection.login(MY_EMAIL, MY_PASSWORD)
#         connection.sendmail(
#             from_addr=MY_EMAIL,
#             to_addrs=birthday_person["email"],
#             msg=f"Subject:Happy Birthday!\n\n{contents}"
#         )
