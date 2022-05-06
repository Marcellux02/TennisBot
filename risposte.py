import random
import telegram
import costanti
from telegram import InputMediaPhoto

# update.message.reply_photo(photo=open("Foto18/.../" + str(prova[rand]), "rb"))
# bot.send_media_group(media=InputMediaPhoto(open(path, 'rb'))
#                      , chat_id=update.message.chat_id)

aggiornamenti = ["Versione 1.0.0 \nVersione iniziale del bot, pieno di bug ma arriveranno aggiornamenti",
                 "Versione 1.0.1 \nAggiunti vari comandi e risolto alcuni bug"]
API_KEY = costanti.API_KEY
bot = telegram.Bot(token=API_KEY)
tette = ["1.jpg", "2.jpg", "3.jpg", "4.jpg", "5.jpg", "6.jpg", "7.jpg", "8.jpg", "9.jpg", "10.jpg",
         "11.jpg", "12.jpg", "13.jpg", "14.jpg", "15.jpg"]
culo = ["1.jpg", "2.jpg", "3.jpg", "4.jpg", "5.jpg", "6.jpg", "7.jpg", "8.jpg", "9.jpg", "10.jpg"]


def handle_message(update, context):
    text = str(update.message.text).lower()
    print(text)
    if "culo" in text:
        rand = random.randint(0, 9)
        path = str("Foto18/Culo/" + str(culo[rand]))
        update.message.reply_photo(photo=open(path, "rb"))
    if "tette" in text:
        rand = random.randint(0, 14)
        path = str("Foto18/Tette/" + str(tette[rand]))
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
    for aggiornamento in aggiornamenti:
        update.message.reply_text(aggiornamento)


def documentazione(update, context):
    update.message.reply_text("Documentazione del bot disponibile a questo link: "
                              "\nhttps://github.com/Marcellux02/TennisBot")
