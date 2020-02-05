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
            'posicaoPorcentagem': [90, 405],
            'cor':(0,255,0)
        },
        {
            'ativo': mensagemTratada[1],
            'posicao': [310, 350],
            'porcetagem': mensagemTratada[11],
            'posicaoPorcentagem': [310, 405],
            'cor':(0,255,0)
        },

         {
            'ativo': mensagemTratada[2],
            'posicao': [535, 350],
            'porcetagem': mensagemTratada[12],
            'posicaoPorcentagem': [535, 405],
            'cor':(0,255,0)
        },
        {
            'ativo': mensagemTratada[3],
            'posicao': [200, 520],
            'porcetagem': mensagemTratada[13],
            'posicaoPorcentagem': [200, 575],
            'cor':(0,255,0)
        },
        {
            'ativo': mensagemTratada[4],
            'posicao': [430, 520],
            'porcetagem': mensagemTratada[14],
            'posicaoPorcentagem': [420, 575],
            'cor':(0,255,0)
        },
        {
            'ativo': mensagemTratada[5],
            'posicao': [95, 840],
            'porcetagem': mensagemTratada[15],
            'posicaoPorcentagem': [80, 900],
            'cor':(255,0,0)
        },
        {
            'ativo': mensagemTratada[6],
            'posicao': [310, 840],
            'porcetagem': mensagemTratada[16],
            'posicaoPorcentagem': [310, 900],
            'cor':(255,0,0)
        },
        {
            'ativo': mensagemTratada[7],
            'posicao': [535, 840],
            'porcetagem': mensagemTratada[17],
            'posicaoPorcentagem': [530, 900],
            'cor':(255,0,0)
        },
        {
            'ativo': mensagemTratada[8],
            'posicao': [200, 1010],
            'porcetagem': mensagemTratada[18],
            'posicaoPorcentagem': [200, 1070],
            'cor':(255,0,0)
        },
         {
            'ativo': mensagemTratada[9],
            'posicao': [430, 1010],
            'porcetagem': mensagemTratada[19],
            'posicaoPorcentagem': [420, 1070],
            'cor':(255,0,0)
        },
        ]

        
        imagem = Image.open('fundo.jpg')
        imagem.save('pronto.jpg')

        for i in range(10):
            imagem = Image.open('pronto.jpg')
            draw = ImageDraw.Draw(imagem)
            font = ImageFont.truetype("arial.ttf", 30)

            draw.text((lista[i]['posicao'][0],lista[i]['posicao'][1]), '{}'.format(lista[i]['ativo']), (12, 12, 12), font=font)
            draw.text((lista[i]['posicaoPorcentagem'][0], lista[i]['posicaoPorcentagem'][1]), '{}'.format(lista[i]['porcetagem']), lista[i]['cor'], font=font)

            imagem.save('pronto.jpg')
        


MessageLoop(bot, handle).run_as_thread()
print ('Online')

while 1:
    time.sleep(10)
	



