import telepot
from telepot.loop import MessageLoop

bot = telepot.Bot('552538744:AAE5r1s7wRAHrdxHq6xYWUcRLnfVgar3xQo')
def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)


MessageLoop(bot, handle).run_as_thread()
print ('Online')

# Keep the program running.
while 1:
    time.sleep(10)
	