from telegram.ext import *
import risposte as R
import costanti
API_KEY = costanti.API_KEY
updater = Updater(API_KEY, use_context=True)


def main():
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("help_gang", R.help_message))
    dp.add_handler(CommandHandler("menuleoncino", R.menu_leoncino))
    dp.add_handler(CommandHandler("immagini", R.immagini))
    dp.add_handler(CommandHandler("audio", R.audio))
    dp.add_handler(CommandHandler("comandi", R.comandi))
    dp.add_handler(CommandHandler("documentazione", R.documentazione))
    dp.add_handler(CommandHandler("versione_bot", R.versione_bot))
    dp.add_handler(MessageHandler(Filters.text, R.handle_message))

    updater.start_polling()
    updater.idle()


main()
