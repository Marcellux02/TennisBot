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
    if "venerd" in text:
        bot.send_audio(chat_id=update.message.chat_id, audio=open("Audio/venerdi.mp3", 'rb'))
    if "bimbo" in text:
        bot.send_audio(chat_id=update.message.chat_id, audio=open("Audio/bimbomerda.mp3", 'rb'))
    if "cringe" in text:
        bot.send_audio(chat_id=update.message.chat_id, audio=open("Audio/cringe.mp3", 'rb'))
    if "audioacaso" in text:
        with open('dati.json', 'r') as f:
            temp = json.load(f)
        rand = random.randint(0, len(temp["audio"]))
        for i in temp["audio"]:
            # Estremamente poco efficiente ma devo studiare di più python e so farlo solo così haha
            if i["index"] == rand:
                path = "Audio/{}.mp3".format(i["nome"])
                print(path)
                bot.send_audio(chat_id=update.message.chat_id, audio=open(path, 'rb'))


def help_message(update, context):
    update.message.reply_text('TENNIS GANG BOT \n' +
                              'Comandi per iniziare: \n' +
                              '/help_gang per avere questo messaggio \n' +
                              '/menu per i menu supportati \n' +
                              '/immagini per sapere che immagini può mandare il bot \n' +
                              '/audio per sapere che audio può mandare il bot \n' +
                              '/comandi per comandi utili \n' +
                              '/versione_bot per sapere informazioni sugli aggiornamenti \n' +
                              '/documentazione per avere il link github del bot'
                              )


def menu(update, context):
    update.message.reply_text('Ecco i seguenti ristoranti supportati: \nLeoncino: /menuleoncino\n'
                              'Tennis: /menutennis')


def menu_Leoncino(update, context):
    menuL = ['Menu/leoncino/Menu1.jpg', 'Menu/leoncino/Menu2.jpg']
    bot.send_media_group(media=[InputMediaPhoto(open(menuL[0], 'rb')),
                                InputMediaPhoto(open(menuL[1], 'rb'))], chat_id=update.message.chat_id)


def menu_Tennis(update, context):
    menuT = ['Menu/tennis/Menu1.jpg', 'Menu/tennis/Menu2.jpg']
    bot.send_media_group(media=[InputMediaPhoto(open(menuT[0], 'rb')),
                                InputMediaPhoto(open(menuT[1], 'rb'))], chat_id=update.message.chat_id)


def immagini(update, context):
    update.message.reply_text('Come spacobot, le parole chiavi sono le seguenti: \n' +
                              'culo, tette \n' +
                              '(Comandi in fase di sviluppo)')


def audio(update, context):
    update.message.reply_text('COMANDI AUDIO:'
                              '\n✔audioacaso inoltra un audio casuale tra i possibili'
                              '\n✔audiobestemmie inoltra un audio con bestemmie (Manutenzione)'
                              '\n✔audiociccio inoltra cicciogamer (Manutenzione)'
                              '\n✔audiomasseo inoltra ilmasseo (Manutenzione)')


def comandi(update, context):
    update.message.reply_text('(Comandi in fase di sviluppo)')


def versione_bot(update, context):
    with open('dati.json', 'r') as f:
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
