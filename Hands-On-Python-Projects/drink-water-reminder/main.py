import time
from plyer import notification

def water_reminder():
    while True:
        try:
            print("Please sip some water!")
            notification.notify(
                title="Please drink some water",
                message="You need to drink some water",
                app_name="Water Reminder",
                app_icon=None,  # Change this to the path of your icon if you want
                timeout=10  # Notification will stay for 10 seconds
            )
        except Exception as e:
            print(f"An error occurred: {e}")
        time.sleep(60 * 60)  # Wait for 1 hour

if __name__ == "__main__":
    water_reminder()