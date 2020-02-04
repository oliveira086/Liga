from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import telepot
from telepot.loop import MessageLoop
import sys
import time

bot = telepot.Bot('552538744:AAE5r1s7wRAHrdxHq6xYWUcRLnfVgar3xQo')
def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)

    if '/' in msg['text']:
        mensagemRecebida = msg['text'][1:]
        mensagemTratada = mensagemRecebida.split('/')

        lista = [
        {
            'ativo': mensagemTratada[0],
            'posicao': [90, 350],
            'porcetagem': mensagemTratada[10],
            'posicaoPorcentagem': '80, 405',
        },
        {
            'ativo': mensagemTratada[1],
            'posicao': [310, 350],
            'porcetagem': mensagemTratada[11],
            'posicaoPorcentagem': '310, 405',
        },
        ]

        

        for i in range(1):
            imagem = Image.open('fundo.jpg')
            draw = ImageDraw.Draw(imagem)
            font = ImageFont.truetype("arial.ttf", 30)

            draw.text((lista[i]['posicao'][0],lista[i]['posicao'][1]), '{}'.format(lista[i]['ativo']), (12, 12, 12), font=font)
            draw.text((lista[i]['posicaoPorcentagem'][0],lista[i]['posicaoPorcentagem'][1]), '{}'.format(lista[i]['porcetagem']), (12, 12, 12), font=font)

        imagem.save('pronto.jpg')


MessageLoop(bot, handle).run_as_thread()
print ('Online')

while 1:
    time.sleep(10)
	



