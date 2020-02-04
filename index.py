from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import sys
import time
import telepot
from telepot.loop import MessageLoop
import requests

bot = telepot.Bot('552538744:AAE5r1s7wRAHrdxHq6xYWUcRLnfVgar3xQo')
def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)

    if msg['text'] == 'start':
	    bot.sendMessage(chat_id,'''Digite a lista de ativos que desejas adicionar, contendo as seguintes informações: ID do ativo, porcetagem (alta ou baixa) e a sua cotação atual, exemplo:
PETRA3 / +1,41% / R$ 12,99
JBS3 / -0,41% / R$ 2,99''')
    if '/' in msg['text']:
	    mensagem = msg['text']
	    #print(mensagem)
		#=== Recortar a string e armzenar valores =====
	    ativoUm = mensagem[1:6]
	    ativoDois = mensagem[7:12]
	    ativoTres = mensagem[13:18]
	    ativoQuatro = mensagem[19:24]
	    ativoCinco = mensagem[25:30]
	    ativoSeis = mensagem[31:36]
	    ativoSete = mensagem[37:42]
	    ativoOito = mensagem[43:48]
	    ativoNove = mensagem[49:54]
	    ativoDez = mensagem[55:60]
	    
	    img = Image.open("fundo.jpg")
	    draw = ImageDraw.Draw(img)
		# font = ImageFont.truetype(<font-file>, <font-size>)
	    font = ImageFont.truetype("arial.ttf", 30)
		
	    draw.text((95, 350), '{}'.format(ativoUm), (0, 0, 0), font=font)
	    draw.text((310, 350), '{}'.format(ativoDois), (0, 0, 0), font=font)
	    draw.text((535, 350), '{}'.format(ativoTres), (0, 0, 0), font=font)
	    draw.text((200, 520), '{}'.format(ativoQuatro), (0, 0, 0), font=font)
	    draw.text((430, 520), '{}'.format(ativoCinco), (0, 0, 0), font=font)
		
	    draw.text((95, 840), '{}'.format(ativoSeis), (0, 0, 0), font=font)
	    draw.text((310, 840), '{}'.format(ativoSete), (0, 0, 0), font=font)
	    draw.text((535, 840), '{}'.format(ativoOito), (0, 0, 0), font=font)
	    draw.text((200, 1010), '{}'.format(ativoNove), (0, 0, 0), font=font)
	    draw.text((430, 1010), '{}'.format(ativoDez), (0, 0, 0), font=font)
		
	    img.save('pronto.jpg')
	
    if '>' in msg['text']:
	    mensagem = msg['text']
	    porcentagemUm = mensagem[1:7]
	    porcentagemDois = mensagem[8:14]
	    porcentagemTres = mensagem[15:21]
	    porcentagemQuatro = mensagem[22:28]
	    porcentagemCinco = mensagem[29:35]
	    porcentagemSeis = mensagem[36:42]
	    porcentagemSete = mensagem[43:49]
	    porcentagemOito = mensagem[50:56]
	    porcentagemNove = mensagem[57:63]
	    porcentagemDez = mensagem[64:70]
	    img = Image.open("balanço.jpg")
	    draw = ImageDraw.Draw(img)
		# font = ImageFont.truetype(<font-file>, <font-size>)
	    font = ImageFont.truetype("arial.ttf", 30)
		
	    draw.text((80, 405), '{}'.format(porcentagemUm), (0, 255, 0), font=font)
	    draw.text((310, 405), '{}'.format(porcentagemDois), (0, 255, 0), font=font)
	    draw.text((535, 405), '{}'.format(porcentagemTres), (0, 255, 0), font=font)
	    draw.text((200, 575), '{}'.format(porcentagemQuatro), (0, 255, 0), font=font)
	    draw.text((420, 575), '{}'.format(porcentagemCinco), (0, 255, 0), font=font)
		
	    draw.text((80, 900), '{}'.format(porcentagemSeis), (255,0,0), font=font)
	    draw.text((310, 900), '{}'.format(porcentagemSete), (255,0,0), font=font)
	    draw.text((530, 900), '{}'.format(porcentagemOito), (255,0,0), font=font)
	    draw.text((200, 1070), '{}'.format(porcentagemNove), (255,0,0), font=font)
	    draw.text((420, 1070), '{}'.format(porcentagemDez), (255,0,0), font=font)
	    
	    img.save('pronto.jpg')
		
		
	    url = "https://api.telegram.org/bot552538744:AAE5r1s7wRAHrdxHq6xYWUcRLnfVgar3xQo/sendPhoto";
	    files = {'photo': open('pronto.jpg', 'rb')}
	    data = {'chat_id' : chat_id}
	    r= requests.post(url, files=files, data=data)
	    print(r.status_code, r.reason, r.content)
	
	
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		

MessageLoop(bot, handle).run_as_thread()
print ('Online')

# Keep the program running.
while 1:
    time.sleep(10)
	
	
	
