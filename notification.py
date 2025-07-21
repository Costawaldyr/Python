# import time 
# from plyer import notification
# sur windows

# if __name__  == '__main__':
#     while True:
#         notification.notify(
#             title = "ALERT!!!",
#             message =  "Take a break! It has been an  hour",
#             timeout = 10
#         )
#         time.sleep(3600)



#  sur mac
import time
from pync import Notifier

if __name__ == '__main__':
    while True:
        Notifier.notify("Take a break! It has been an hour", title="ALERT!!!")
        time.sleep(3600)