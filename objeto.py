import telepot
from telepot.loop import MessageLoop
import sys
import time

bot = telepot.Bot('552538744:AAE5r1s7wRAHrdxHq6xYWUcRLnfVgar3xQo')
def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)

    if '/' in msg['text']:
        mensagemRecebida = msg['text'][1:]
        mensagemTratada = mensagemRecebida.split(',')
    
    if '>' in msg['text']:
        mensagemRecebidaPorcentagem = msg['text'][1:]
        mensagemTratadaPorcentagem = mensagemRecebidaPorcentagem.split('/')

    if '!' in msg['text']:
        pass
        


MessageLoop(bot, handle).run_as_thread()
print ('Online')

while 1:
    time.sleep(10)
	

