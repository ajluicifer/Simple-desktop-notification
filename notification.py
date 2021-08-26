# Importing Libraries
import time
from plyer import notification

if __name__=="__main__":
    while True:
        notification.notify(
            title = 'Please Take a break',
            message = "Acc to some scientist we should take a break after every 25 mins during work",
            app_icon = "shout_announcement_megaphone_woman_girl_icon_191399.ico",
            app_name = "Reminder",
            timeout = 5
        )
        time.sleep(5)
