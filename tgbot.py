#!/usr/bin/python
# -*- coding: utf-8 -*-
import re
import telebot
import time
import sys
import os
import logging
import redis
from time import gmtime, strftime
from telebot import types
redis = redis.StrictRedis(host='localhost', port=6379, db=0, decode_responses=True)
reload(sys)
sys.setdefaultencoding("utf-8")
#################################
# by amirspecial @sudo1 with ❤️
#################################
def clear():
    os.system("clear")
start_time = str(strftime("%Y-%m-%d %H:%M:%S", gmtime()))
os.system("figlet special team")
time.sleep(int(3))
clear()
bot = telebot.TeleBot("Token")
user = bot.get_me()
botname = user.username
print " @{} started on {}".format(botname,start_time)
channel = "@ user name channel"
sudo = {"123755887"}
def is_sudo(user):
    for i in sudo:
        if int(user) == int(i):
            return True
        else:
            return False
#logger = telebot.logger
#telebot.logger.setLevel(logging.DEBUG)
##########################################

user_dict = {}


class User:
    def __init__(self, name):
        self.name = name

@bot.message_handler(func=lambda msg: msg.text.encode("utf-8") == "😬 نمایش کل تست ها")
def send_something(message):
    allans = redis.smembers("allans{}".format(message.from_user.id))
    if bot.get_chat_member(channel, message.from_user.id).status == "left" or bot.get_chat_member(channel, message.from_user.id).status == "kicked":
        mk = '''
شما ابتدا باید در کانال ما عضو شوید:
> @special_programming <
پس از عضویت در کانال میتوانید ازین دکمه استفاده نمایید😀❤️👌
        '''
        bot.reply_to(message, mk)
        return False
    if allans:
        for i in allans:
            bot.send_message(message.from_user.id, i)
    if not allans:
        bot.send_message(message.from_user.id, '''دوست من هنوز کسی برات پرسشنامه رو پر نکرده 😕
لطفا لینکتو بین دوستات به اشتراک بذار تا بتونن برات پرسشنامه رو پر کنند 😍''')


#################################
# by amirspecial @sudo1 with ❤️
#################################

@bot.message_handler(func=lambda msg: msg.text.encode("utf-8") == "✅ دریافت لینک")
def send_something(message):
    loll = '''
لینک مخصوص شما برای اینکه بدونی  دوستات چقدر میشناسننت ؟ چه حسی بهت دارن و چی تو دلشون مونده که یهت بگن ؟ چه جنبه از شخصیتتو دوس دارن و ... ؟ رو در پیام پایین برات ساختم 🙏😍
میتونی اون لینکو یا کل پیام رو برای دوستات فوروارد کنی یا توی اینستا و... به اشتراک بذاری تا دوستات بتونن در مورد تو پرسشنامه رو پر کنند  👌
⭕️به محض اینکه هر دوستیت برات پرسشنامه رو پر کرد میتونی برات همه ی جواب هایی که داده رو ارسال میکنم (برای اینکه فرستنده تست ها رو ببینی  لطفا داخل کانال ما عضو شو 👈 @special_programming )
    '''
    lll = '''
    سلام دوست من 😊 خوبی ؟ 🙏

ازت میخوام واسه دوستت  {} یک دقیقه وقت بذاری و یه پرسشنامه با سوالات با حال و جالب رو در موردش پر کنی 👌😬

https://telegram.me/{}?start={}
    '''
    chat_id = message.chat.id
    name = redis.get("name{}".format(chat_id))
    lls = str(lll).format(name,botname,chat_id)
    bot.send_message(message.from_user.id, loll)
    bot.send_message(message.from_user.id, lls)

#################################
# by amirspecial @sudo1 with ❤️
#################################
@bot.message_handler(func=lambda msg: msg.text.encode("utf-8") == "😍 شروع پرسشنامه")
def send_something(message):
    ppp = '''خیلی خوبه دوست من تست با موفقیت شروع شد 👌
✅پاسخ هر سوال را به صورت متن ارسال کنید'''
    bot.send_message(message.from_user.id, ppp)
    ggg = '''
    [📈 1/5]
    {}  را چقدر می شناسیش و تیکه کلامش چیه؟ 😊
    '''
    namm = redis.get("me{}".format(message.from_user.id))
    frid = redis.get("meid{}".format(message.from_user.id))
    ggh = str(ggg).format(namm)
    markup = types.ForceReply(selective=False)
    msg = bot.send_message(message.from_user.id, ggh, reply_markup=markup)
    #msg = bot.reply_to(message, ggh)
    bot.register_next_step_handler(msg, prc_1)
def prc_1(message):
    chat_id = message.chat.id
    tike = message.text
    namr = redis.get("me{}".format(message.from_user.id))
    frid = redis.get("meid{}".format(message.from_user.id))
    redis.set("tike{}.format(message.from_user.id)",tike)
    #bot.send_message(message.from_user.id, "{} tike kalameshe".format(tike))
    fd = '''
[📈 2/5]
چه چیزی {} را ناراحت می کنه و خط قرمزش چیه؟ 🤔
        '''
    msg = bot.reply_to(message, str(fd).format(namr))
    bot.register_next_step_handler(msg, prc_2)
def prc_2(message):
    chat_id = message.chat.id
    khat = message.text
    frid = redis.get("meid{}".format(message.from_user.id))
    redis.set("khat{}.format(message.from_user.id)",khat)
    namr = redis.get("me{}".format(message.from_user.id))
    #bot.send_message(message.from_user.id, "{} khat ghermeze".format(khat))
    fd = '''
    [📈 3/5]
چه حسی نسبت به {} داری و ته دلت چی مونده که هنوز بهش نگفتی؟ 🤔
     '''
    msg = bot.reply_to(message, str(fd).format(namr))
    bot.register_next_step_handler(msg, prc_3)
def prc_3(message):
    chat_id = message.chat.id
    tahdel = message.text
    frid = redis.get("meid{}".format(message.from_user.id))
    redis.set("tahdel{}.format(message.from_user.id)",tahdel)
    namr = redis.get("me{}".format(message.from_user.id))
    #bot.send_message(message.from_user.id, "{} tah deleshe".format(tahdel))
    fd = '''
[📈 4/5]
کدوم جنبه از شخصیت و رفتار {} را دوست داری؟ 🤔
     '''
    msg = bot.reply_to(message, str(fd).format(namr))
    bot.register_next_step_handler(msg, prc_4)
def prc_4(message):
    chat_id = message.chat.id
    janbe = message.text
    frid = redis.get("meid{}".format(message.from_user.id))
    redis.set("janbe{}.format(message.from_user.id)",janbe)
    namr = redis.get("me{}".format(message.from_user.id))
    #bot.send_message(message.from_user.id, "{} tah deleshe".format(janbe))
    fd = '''
[📈 5/5]
 دوست داری با {} به مسافرت بری؟ اگه جوابت مثبته کجا دوست داری بری باهاش؟😬
     '''
    msg = bot.reply_to(message, str(fd).format(namr))
    bot.register_next_step_handler(msg, prc_5)
def prc_5(message):
    chat_id = message.chat.id
    safar = message.text
    namr = redis.get("me{}".format(message.from_user.id))
    frid = redis.get("meid{}".format(message.from_user.id))
    redis.set("safar{}.format(message.from_user.id)",safar)
    #bot.send_message(message.from_user.id, "{} safar beri".format(safar))
    fd = '''
دوست من پرسشنامه با موفقیت تکمیل شد 😍

ما الان پاسخ هایی که دادی رو برای دوستت {} ارسال میکنیم 😍😬

میخوای تو هم لینک شخصی خودتو بسازی و بین دوستات پخش کنی ؟😍
اگه میخوای لینک شخصی خودت رو بسازی تا بدونی دوستات چقدر میشناسنت ؟ چه حسی بهت دارن و چی تو دلشون مونده که بهت بگن ؟ چه جنبه از شخصیتتو دوس دارن و ... ؟ روی دکمه ی ساخت لینک شخصی کلیک کن 😍😬
    '''
    #msg = bot.reply_to(message, str(fd).format(namr))
    markup = types.ReplyKeyboardMarkup(row_width=3,resize_keyboard=True)
    kb = types.KeyboardButton('😍 برو بریم')
    markup.row(kb)
    msg = bot.send_message(message.from_user.id, str(fd).format(namr), reply_markup=markup)
    ssafar = redis.get("safar{}.format(message.from_user.id)")
    jjanbe = redis.get("janbe{}.format(message.from_user.id)")
    ttahdel = redis.get("tahdel{}.format(message.from_user.id)")
    kkhat = redis.get("khat{}.format(message.from_user.id)")
    ttike = redis.get("tike{}.format(message.from_user.id)")
    sfr = '''
🗣 ارسال شده از طرف {}
دوست من {} همین الان دوستت {}  برات پرسشنامه رو پر کرد پاسخ هایی که داده رو در زیر برات مینویسم 😍

🔘 {}  را چقدر می شناسیش و تیکه کلامش چیه؟ 😊
✅ پاسخ : {}

🔘 چه چیزی {} را ناراحت می کنه و خط قرمزش چیه؟ 🤔
✅ پاسخ : {}

🔘 چه حسی نسبت به {} داری و ته دلت چی مونده که هنوز بهش نگفتی؟🤔
✅ پاسخ : {}

🔘 کدوم جنبه از شخصیت و رفتار {} را دوست داری؟ 🤔
✅ پاسخ : {}

🔘 دوست داری با {} به مسافرت بری؟ اگه جوابت مثبته کجا دوست داری بری باهاش؟😬
✅ پاسخ : {}
    '''
    namr = redis.get("me{}".format(message.from_user.id))
    frid = redis.get("meid{}".format(message.from_user.id))
    dg = str(sfr).format(message.from_user.first_name,namr,message.from_user.first_name,namr,ttike,namr,kkhat,namr,ttahdel,namr,jjanbe,namr,ssafar)
    redis.sadd("allans{}".format(frid),dg)
    redis.set("sabtshode{}{}".format(message.from_user.id,frid),"ok")
    if bot.get_chat_member(channel, frid).status == "left" or bot.get_chat_member(channel, frid).status == "kicked":
        mk = '''
شما یک پیام جدید از طرف دوستتان دریافت کردید😍❤️.
برای دیدن پیام ابتدا در کانال
@special_programming
عضو بشید😅
سپس میتونید با دکمه:
😬 نمایش کل تست ها
تمامی پیام های دوستانتان رو ببینید.
🙈❤️
        '''
        bot.send_message(frid, mk)
    if not bot.get_chat_member(channel, frid).status == "left" or bot.get_chat_member(channel, frid).status == "kicked":
        pass
        bot.send_message(frid, dg)

#################################
# by amirspecial @sudo1 with ❤️
#################################

@bot.message_handler(func=lambda msg: msg.text.encode("utf-8") == "😍 ساخت لینک شخصی")
def send_something(message):
    markup = types.ReplyKeyboardMarkup(row_width=3,resize_keyboard=True)
    kb = types.KeyboardButton('😍 برو بریم')
    markup.row(kb)
    name = message.from_user.first_name
    sss = '''
سلام دوست من  {} خوبی ؟ 😍

میخوای بدونی دوستات چقدر میشناسنت ؟ چه حسی بهت دارن و چی تو دلشون مونده که بهت بگن ؟ چه جنبه از شخصیتتو دوس دارن و ... ؟   😬

پس منتظر چی هستی ؟ روی دکمه ی برو بریم  کلیک کن 😍🙏
     '''
    st = str(sss).format(name)
    bot.send_message(message.from_user.id, st, reply_markup=markup)
@bot.message_handler(func=lambda msg: msg.text.encode("utf-8") == "😍 عضویت در کانال")
def send_something(message):
    bot.reply_to(message, "join @special_programming (:")

@bot.message_handler(func=lambda msg: msg.text.encode("utf-8") == "😍 برو بریم")
def send_something(message):
    markup = types.ForceReply(selective=False)
    msg = bot.send_message(message.from_user.id, "دوست من لطفا اسمتو برام بنویس و ارسال کن 😍🙏", reply_markup=markup)
    bot.register_next_step_handler(msg, process_name_step)
def process_name_step(message):
    try:
        chat_id = message.chat.id
        name = message.text
        user = User(name)
        user_dict[chat_id] = user
        redis.set("name{}".format(chat_id),name)
        oms = '''
        دوست من {} اسمت با موفقیت ثبت شد 👌

لینک مخصوص شما برای اینکه بدونی دوستات چقدر میشناسنت ؟ چه حسی بهت دارن و چی تو دلشون مونده که بهت بگن ؟ چه جنبه از شخصیتتو دوس دارن و ... ؟  رو در پیام پایین برات ساختم 🙏😍

میتونی اون لینکو یا کل پیام رو برای دوستات فوروارد کنی یا توی اینستا و... به اشتراک بذاری تا دوستات بتونن در مورد تو پرسشنامه رو پر کنند  👌

⭕️به محض اینکه هر دوستت برات پرسشنامه رو پر کرد برات همه ی جواب هایی که داده رو ارسال میکنم (فرستنده پاسخ ها نمایش داده نخواهد شد و برای اینکه ببینی کی برات تست رو انجام داده میتونی عضو كانال ما بشي و از همه امكانات ربات استفاده كني)
        '''
        omstr = str(oms).format(name)
        msg = bot.reply_to(message, omstr)
        lll = '''
        سلام دوست من 😊 خوبی ؟ 🙏

ازت میخوام واسه دوستت  {} یک دقیقه وقت بذاری و یه پرسشنامه با سوالات با حال و جالب رو در موردش پر کنی 👌😬

برای شروع ، روی انجام تست  (  کلیک کن و یا روی لینک زیر کلیک کن 🙏

https://telegram.me/{}?start={}
        '''
        lls = str(lll).format(name,botname,chat_id)
        markup = types.ReplyKeyboardMarkup(row_width=3,resize_keyboard=True)
        kb = types.KeyboardButton("😍 عضویت در کانال")
        kbb = types.KeyboardButton("😬 نمایش کل تست ها")
        kbbb = types.KeyboardButton("✅ دریافت لینک")
        kbbbb = types.KeyboardButton("😍 ساخت لینک شخصی")
        markup.row(kb)
        markup.row(kbb)
        markup.row(kbbb)
        markup.row(kbbbb)
        bot.send_message(message.from_user.id, lls, reply_markup=markup)

    except Exception as e:
        bot.reply_to(message, 'oooops')

#################################
# by amirspecial @sudo1 with ❤️
#################################
@bot.message_handler(regexp="^(/start) (.*)")
def handle_message(message):
    text = message.text.split()[1]
    redis.sadd("porsmanbot",message.from_user.id)
    if redis.get("sabtshode{}{}".format(message.from_user.id,text)) == "ok":
        frn = redis.get("name{}".format(text))
        mnm = '''
دوست من شما قبلا تست رو برای {} دادی و دوباره نمیتونی تست بدی 😕

اگه میخوای لینک شخصیتو بسازی تا بدونی دوستات چقدر میشناسنت ؟ چه حسی بهت دارن و چی تو دلشون مونده که بهت بگن ؟ چه جنبه از شخصیتتو دوس دارن و ... ؟ روی ساخت لینک شخصی کلیک کن😬😍
        '''
        mbb = str(mnm).format(frn)
        markup = types.ReplyKeyboardMarkup(row_width=3,resize_keyboard=True)
        kb = types.KeyboardButton('😍 برو بریم')
        markup.row(kb)
        bot.send_message(message.from_user.id, mbb, reply_markup=markup)
        return False

    if re.search("([-+]?[0-9]+)", text):
        if int(text) == int(message.from_user.id):
            name = redis.get("name{}".format(message.from_user.id))
            bot.reply_to(message, str(''' دوست من {}  !
خودت که نمیتونی راجع به خودت پرسشنامه رو پر کنی 😕
لطفا لینکتو بین دوستات پخش کن تا اونا پرسشنامه رو برات پر کنند 😍''').format(name))
        if not int(text) == int(message.from_user.id):
            namedost = redis.get("name{}".format(text))
            redis.set("me{}".format(message.from_user.id),namedost)
            redis.set("meid{}".format(message.from_user.id),text)
            fg = '''
سلام دوست من 😍

خیلی ازت ممنونم که واسه دوستت  {} میخوای تست رو انجام بدی 🙏

در پایان اگه خواستی لینک شخصی خودت رو هم میسازم برات تا بدونی  دوستات چقدر میشناسنت ؟ چه حسی بهت دارن و چی تو دلشون مونده که بهت بگن ؟ چه جنبه از شخصیتتو دوس دارن و ... ؟ 😍

حالا برای انجام تست برای دوستت {} روی شروع پرسشنامه کلیک کن 😬
            '''
            fff = str(fg).format(namedost,namedost)
            markup = types.ReplyKeyboardMarkup(row_width=3,resize_keyboard=True)
            kb = types.KeyboardButton("😍 شروع پرسشنامه")
            markup.row(kb)
            bot.send_message(message.from_user.id, fff, reply_markup=markup)
#################################
# by amirspecial @sudo1 with ❤️
#################################
@bot.message_handler(commands=['stats'])
def send_welcome(message):
    if is_sudo(message.from_user.id):
        bot.reply_to(message, redis.scard("porsmanbot"))
    else:
        bot.reply_to(message, "siktir |:")
@bot.message_handler(commands=['bc'])
def send_welcome(message):
    if is_sudo(message.from_user.id):
        text = message.text.split()[1]
        bchash = redis.smembers("porsmanbot")
        bot.send_message(123755887, "starting to broadcast to all bot users")
        try:
            for i in bchash:
                bot.send_message(i, text)
        except:
            print "fuck |:"
    else:
        bot.reply_to(message, "siktir |:")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    #print message
    redis.sadd("porsmanbot",message.from_user.id)
    markup = types.ReplyKeyboardMarkup(row_width=3,resize_keyboard=True)
    kb = types.KeyboardButton('😍 برو بریم')
    markup.row(kb)
    name = message.from_user.first_name
    sss = '''
سلام دوست من  {} خوبی ؟ 😍

میخوای بدونی دوستات چقدر میشناسنت ؟ چه حسی بهت دارن و چی تو دلشون مونده که بهت بگن ؟ چه جنبه از شخصیتتو دوس دارن و ... ؟   😬

پس منتظر چی هستی ؟ روی دکمه ی برو بریم  کلیک کن 😍🙏
     '''
    st = str(sss).format(name)
    bot.send_message(message.from_user.id, st, reply_markup=markup)
bot.polling(True)
#################################
# by amirspecial @sudo1 with ❤️
#################################
