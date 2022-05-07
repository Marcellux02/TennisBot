from telegram.ext import *
import data
import json
import risposte as R

updater = Updater(data.API_KEY, use_context=True)


def updateVersion(nUpdate, description):
    x = {
        "versione": str(nUpdate),
        "descrizione": str(description)
    }
    if nUpdate is None or description is None:
        return
    else:
        try:
            with open('versioni.json', 'r+') as f:
                temp = json.load(f)
                temp["versioni"].append(x)
                f.seek(0)
                json.dump(temp, f, indent=2)
        except Exception as e:
            print('Errore nell\'apertura del file ' + str(e))


def main():
    # UpdateVersion viene modificato internamente quando c'è un nuovo aggiornamento.
    updateVersion(None, None)
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
