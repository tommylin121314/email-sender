import smtplib
import sys
import datetime as dt


print("Program currently running...")

try:
    email = sys.argv[1]
    password = sys.argv[2]
    recp = sys.argv[3]
except IndexError:
    print("Incorrect argument format.")
    print("Expected: python email-sender.py [username] [password] [recipient]")
    quit()


curr_min = 0
num_sent = 0
print(f"\rNumber of emails sent: {num_sent}", end='', flush=True)

while(True):

    min = dt.datetime.now().minute

    if min != curr_min:
        curr_min = min
        with smtplib.SMTP("smtp.gmail.com") as conn:
            conn.starttls()
            conn.login(user=email, password=password)
            conn.sendmail(
                from_addr=email,
                to_addrs=recp, 
                msg=f"Subject:Time\n\nThe current time is {dt.datetime.now()}."
            )

        num_sent += 1
        print(f"\rNumber of emails sent: {num_sent}", end='', flush=True)