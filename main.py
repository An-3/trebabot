import os
import telegram
from telegram.ext import Dispatcher, MessageHandler, Filters
from langdetect import detect
import random


def webhook(request):
    bot = telegram.Bot(token=os.environ["TELEGRAM_TOKEN"])
    update = telegram.Update.de_json(request.get_json(force=True), bot)

    dispatcher = Dispatcher(bot, None, workers=0)
    dispatcher.add_handler(MessageHandler(filters=Filters.text, callback=handle_message(bot, update)))

    return "ok"


def handle_message(bot, update):
    chat_id = update.message.chat.id
    lang = detect(update.message.text)
    list_of_swarka = ['Це шо блять таке? Франка на вас немає!', 'Це шо? російська? Ганьба!', 'Чому не державною?', 'Та ти висерок перестанеш писати російською?', 'Йди у сраку зі своєю російською!', 'Я тебе зараз відфайдолю за оцю російську', 'Я тобі зараз зашью ротяку по саму сраку за російську', 'В сраці більше розуму аніж у тих хто пише російською', 'Ті хто спілкуються росвйською -- виродки', 'Ото ти вкурвлене росвйською патякати', 'А щоб тебе підняло та гепнуло російською писати', 'А щоб ти падло дристало та й дристало оту російську використовувати', 'А щоб в тебе пір’я в роті поросло від російської мови', 'Шоб ти ригав від тієї російської', 'Зараз дам по макітрі за російську', 'Гімно ти малодушне російською говорити', 'Вилупок ти козломордий російською спілкуватись', 'Покидьок ти аморальний спілкуватись ворожою мовою', 'Наволоч ти і одоробло. Хто ж москальскою спілкується?']
    if lang == 'ru':
        swarka = random.choice(list_of_swarka)
        bot.sendMessage(chat_id=chat_id, text=swarka)
