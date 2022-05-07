import json
import random
import telegram
import data
from telegram import InputMediaPhoto

# update.message.reply_photo(photo=open("Foto18/.../" + str(prova[rand]), "rb"))
# bot.send_media_group(media=InputMediaPhoto(open(path, 'rb'))
#                      , chat_id=update.message.chat_id)
bot = telegram.Bot(token=data.API_KEY)


def handle_message(update, context):
    text = str(update.message.text).lower()
    print(text)
    if "culo" in text:
        rand = random.randint(0, 9)
        path = str("Foto18/Culo/" + str(data.C[rand]))
        update.message.reply_photo(photo=open(path, "rb"))
    if "tette" in text:
        rand = random.randint(0, 14)
        path = str("Foto18/Tette/" + str(data.T[rand]))
        update.message.reply_photo(photo=open(path, "rb"))


def help_message(update, context):
    update.message.reply_text('TENNIS GANG BOT \n' +
                              'Comandi per iniziare: \n' +
                              '/help_gang per avere questo messaggio \n' +
                              '/menuleoncino per il menu del leoncino \n' +
                              '/immagini per sapere che immagini può mandare il bot \n' +
                              '/audio per sapere che audio può mandare il bot \n' +
                              '/comandi per comandi utili \n' +
                              '/versione_bot per sapere informazioni sugli aggiornamenti \n' +
                              '/documentazione per avere il link github del bot'
                              )


def menu_leoncino(update, context):
    menu = ['Menu/Menu1.jpg', 'Menu/Menu2.jpg']
    bot.send_media_group(media=[InputMediaPhoto(open(menu[0], 'rb')),
                                InputMediaPhoto(open(menu[1], 'rb'))], chat_id=update.message.chat_id)


def immagini(update, context):
    update.message.reply_text('Come spacobot, le parole chiavi sono le seguenti: \n' +
                              'culo, tette \n' +
                              '(Comandi in fase di sviluppo)')


def audio(update, context):
    update.message.reply_text('(Comandi in fase di sviluppo)')


def comandi(update, context):
    update.message.reply_text('(Comandi in fase di sviluppo)')


def versione_bot(update, context):
    with open('versioni.json', 'r') as f:
        cronologia_aggiornamenti = json.load(f)
        final_message = ""
    for agg in cronologia_aggiornamenti["versioni"]:
        v = agg["versione"]
        d = agg["descrizione"]
        temp_message = str("Versione " + v + "\n" + d)
        final_message += temp_message + "\n" + "\n"
    update.message.reply_text(final_message)


def documentazione(update, context):
    update.message.reply_text("Documentazione del bot disponibile a questo link: "
                              "\nhttps://github.com/Marcellux02/TennisBot")
