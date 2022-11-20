import time
from plyer import notification
if __name__ == '__main__':
    while True:
        notification.notify(
            title = "🥛Please Drink Water Now!!",
            message ="Drinking Water Helps to Maintain the Balance of Body Fluids.",
            timeout= 10,
            app_icon = "D:\Practise Program PY\Project\icon.ico",
            ticker = "Drink Water Please",
            )
        
