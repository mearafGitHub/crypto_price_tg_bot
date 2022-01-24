import telegram
from telegram.ext import Updater
from telegram.ext import CommandHandler
from tracker import get_cardano_price

telegram_bot_token = "2041232392:AAEij_qtGE0b2l0I-kbsaL-tU8AgHmpUd8w"
updater = Updater(token=telegram_bot_token, use_context=True)
dispatcher = updater.dispatcher


def start(update, context):
    chat_id = update.effective_chat.id
    message = ""
    cardano_data = get_cardano_price()

    cardano_price = cardano_data['cardano']['usd']
    cardano_volume = cardano_data['cardano']['usd_24h_vol']
    cardano_market_cap = cardano_data['cardano']['usd_market_cap']
    message += f"Coin: 'Cardano Today'\nPrice: ${cardano_price:,.2f}\nHour Change: {cardano_volume:.3f}%\nDay Change: {cardano_market_cap:.3f}%\n\n"

    # for i in crypto_data:
    #     coin = crypto_data[i]["coin"]
    #     price = crypto_data[i]["price"]
    #     change_day = crypto_data[i]["change_day"]
    #     change_hour = crypto_data[i]["change_hour"]
    #     message += f"Coin: {coin}\nPrice: ${price:,.2f}\nHour Change: {change_hour:.3f}%\nDay Change: {change_day:.3f}%\n\n"

    context.bot.send_message(chat_id=chat_id, text=message)


dispatcher.add_handler(CommandHandler("start", start))
updater.start_polling()
