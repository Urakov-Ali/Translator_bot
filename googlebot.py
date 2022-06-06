import logging
from googletrans import Translator

import datetime
import pytz
import time
from buttons import *
from classs import Infos 
import asyncio

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import CallbackQuery

 
API_TOKEN = '5288499298:AAF6ndQ9h9GsuCnktm-rhXfmjlmb2wyBBmY'
tr =Translator()

#calling our "Infos" class as an object
x =Infos()
Admin = int("1344241185")
# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)



@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
	#Create our table to save the users in our database 
	#(so by the command of [/alluser] we can know how many people are using our bot now)
	x.create_table()
	global userid
	#taking all the needed informations about the new user
	userid =message.from_user.id
	username =message.from_user.username
	firstname =message.from_user.first_name
	#to check if user's data exist in basa
	#1 -it doesn't let to one person subscribe twice on our bot
	#2 -so the database will sort and add only those subscribers who is new in our bot
	check_it =x.check(userid)
	
	#here is the process of sorting 
	if check_it is None:
		x.insert(userid, username, firstname)
		z =x.admin_notify(userid)
		await bot.send_message(Admin, f"New user has been registered\
			\nUser_id: {z[0]} \nUsername: @{z[1]} \nFirstname: {z[2]}")
	else:
		await message.reply("What will we translate ? \nType your words here:\
			\n\nЧто мы будем переводить? \n Введите свои слова здесь:")

#by alluser command can be seen the quantity of users of our bot
#the command is only available for admin
@dp.message_handler(commands=['alluser'], user_id=Admin)
async def count(message: types.Message):
	userid =message.from_user.id
	num =x.count(userid)
	await bot.send_message(Admin,f"Bot users: {num[0][0]}")

#menu bar
@dp.message_handler(commands=['help'])
async def count(message: types.Message):
	await message.answer('👨‍💻  Use Google translator without leaving a Telegram \
		\n🗿 How ?\
		\n👨‍💻 Just press the /start button to use the bot\
		\n🗿  ok... /start\
		\n\n❗️ For any suggestion or complaints please communicate with adminstration: @Arab_04\
		\n\n👨‍💻 Используйте Google переводчик, не выходя из Telegram\
		\n🗿  Как ?\
		\n👨‍💻  Просто нажмите кнопку /start, чтобы использовать бота\
		\n🗿  Ну, хорошо... /start\
		\n\n❗️  По любым предложениям или жалобам, пожалуйста, свяжитесь с администрацией: @Arab_04')

@dp.message_handler(commands=['suggestion'])
async def count(message: types.Message):
	await message.answer('🙋‍♂️ I have something to tell\
		👨‍💻  So you can write me in direct: @Arab_04\
		\n\n🙋‍♂️ Я хочу кое-что рассказать\
		\n👨‍💻  Напиши мне в директ: @Arab_04')

@dp.message_handler(commands=['suggestion'])
async def count(message: types.Message):
	await message.answer('💰🤵‍♂ I want to buy ads to improve my business\
		\n👨‍💻  ')

@dp.message_handler(text='⬅️  Back')
async def back_go(message: types.Message):
	await message.reply("What will we translate ? \nType your words here:\
		\n\nЧто мы будем переводить? \n Введите свои слова здесь:", reply_markup=types.ReplyKeyboardRemove())

@dp.message_handler(commands=['Translate'], commands_prefix=['#','/'])
async def echo(message: types.Message):
	await message.answer("What will we translate ? \nType your words in any language:")

@dp.message_handler(is_forwarded=True, user_id=Admin)
async def post_sender(message: types.Message):
	announcement =x.announce()
	anno = announcement
	for announce in anno:
		await asyncio.sleep(2)
		await message.send_copy(chat_id =announce[0])
	

#England datetime
@dp.message_handler(text="🇬🇧  Time in London  🕔")
async def time_England(message: types.Message):
	time = pytz.timezone('Europe/London')
	eng_time =datetime.datetime.now(time)
	enge_time =eng_time.strftime("%I:%M:%S %p")
	await message.answer(enge_time)

@dp.message_handler(text="🇬🇧  Data in London  📅")
async def data_england(message: types.Message):
	time = pytz.timezone('Europe/London')
	eng_data =datetime.datetime.now(time)
	enge_data =eng_data.strftime("%A %d %B %Y")
	await message.answer(enge_data)


#England message
@dp.callback_query_handler(text="eng")
async def to_english(call:CallbackQuery):
	tarjima =tr.translate(t, dest='en')
	await call.message.answer(f"Your result \n{tarjima.text}", reply_markup=time_eng)
	await call.message.delete()



#Korean datetime
@dp.message_handler(text="🇰🇷  Time in Seul  🕔")
async def time_korean(message: types.Message):
	time = pytz.timezone('Asia/Seoul')
	kor_time =datetime.datetime.now(time)
	kore_time =kor_time.strftime("%I:%M:%S %p")
	await message.answer(kore_time)

@dp.message_handler(text="🇰🇷  Data in Seul  📅")
async def data_korean(message: types.Message):
	time = pytz.timezone('Asia/Seoul')
	kor_data =datetime.datetime.now(time)
	kore_data =kor_data.strftime("%A %d %B %Y")
	await message.answer(kore_data)


#Korean message
@dp.callback_query_handler(text="kor")
async def to_korean(call:CallbackQuery):
	tarjima =tr.translate(t, dest='ko')
	await call.message.answer(f"Your result \n{tarjima.text}", reply_markup=time_kor)
	await call.message.delete()


#China datetime
@dp.message_handler(text="🇨🇳  Time in Hong_Kong  🕔")
async def time_china(message: types.Message):
	time = pytz.timezone('Asia/Hong_Kong')
	chin_time =datetime.datetime.now(time)
	chine_time =chin_time.strftime("%I:%M:%S %p")
	await message.answer(chine_time)

@dp.message_handler(text="🇨🇳  Data in Hong_Kong  📅")
async def data_china(message: types.Message):
	time = pytz.timezone('Asia/Hong_Kong')
	chin_data =datetime.datetime.now(time)
	chine_data =chin_data.strftime("%A %d %B %Y")
	await message.answer(chine_data)


#China message
@dp.callback_query_handler(text="chin")
async def to_chinese(call:CallbackQuery):
	tarjima =tr.translate(t, dest='zh-cn')
	await call.message.answer(f"Your result \n{tarjima.text}", reply_markup=time_chin)
	await call.message.delete()


#Hind datetime
@dp.message_handler(text='🇮🇳  Time in Idnia  🕔')
async def time_hind(message: types.Message):
	time = pytz.timezone('Asia/Kolkata')
	hind_time =datetime.datetime.now(time)
	india_time =hind_time.strftime("%I:%M:%S %p")
	await message.answer(india_time)

@dp.message_handler(text="🇮🇳  Time in Idnia  🕔")
async def data_hind(message: types.Message):
	time = pytz.timezone('Asia/Kolkata')
	hind_data =datetime.datetime.now(time)
	india_data =hind_data.strftime("%A %d %B %Y")
	await message.answer(india_data)

#Hind message
@dp.callback_query_handler(text="hind")
async def to_hind(call:CallbackQuery):
	tarjima =tr.translate(t, dest='hi')
	await call.message.answer(f"Your result: \n{tarjima.text}", reply_markup=time_hindi)
	await call.message.delete()

#spanish datetime
@dp.message_handler(text='🇪🇸  Time in Madrid  🕔')
async def time_spaine(message: types.Message):
	time = pytz.timezone('Europe/Madrid')
	spanish_time =datetime.datetime.now(time)
	spain_time =spanish_time.strftime("%I:%M:%S %p")
	await message.answer(spain_time)

@dp.message_handler(text="'🇪🇸  Data in Madrid  📅")
async def data_spaine(message: types.Message):
	time = pytz.timezone('Europe/Madrid')
	spanish_data =datetime.datetime.now(time)
	spain_data =spanish_data.strftime("%A %d %B %Y")
	await message.answer(spain_data)

#spain message
@dp.callback_query_handler(text="esp")
async def to_spaine(call:CallbackQuery):
	tarjima =tr.translate(t, dest='fr')
	await call.message.answer(f"Your result: \n{tarjima.text}", reply_markup=time_spain)
	await call.message.delete()


#French datetime
@dp.message_handler(text='🇫🇷  Time in Paris  🕔')
async def time_france(message: types.Message):
	time = pytz.timezone('Europe/Paris')
	French_time =datetime.datetime.now(time)
	france_time =French_time.strftime("%I:%M:%S %p")
	await message.answer(france_time)

@dp.message_handler(text="🇫🇷  Data in Paris  📅")
async def data_france(message: types.Message):
	time = pytz.timezone('Europe/Paris')
	French_data =datetime.datetime.now(time)
	france_data =French_data.strftime("%A %d %B %Y")
	await message.answer(france_data)

#France message
@dp.callback_query_handler(text="frn")
async def to_France(call:CallbackQuery):
	tarjima =tr.translate(t, dest='fr')
	await call.message.answer(f"Your result: \n{tarjima.text}", reply_markup=time_frn)
	await call.message.delete()


#Arabic datetime
@dp.message_handler(text='🇦🇪  Time in Dubai  🕔')
async def time_arabe(message: types.Message):
	time = pytz.timezone('Asia/Dubai')
	Arabic_time =datetime.datetime.now(time)
	arab_time =Arabic_time.strftime("%I:%M:%S %p")
	await message.answer(arab_time)

@dp.message_handler(text="🇦🇪  Data in Dubai  📅")
async def data_arabe(message: types.Message):
	time = pytz.timezone('Asia/Dubai')
	Arabic_data =datetime.datetime.now(time)
	arab_data =Arabic_data.strftime("%A %d %B %Y")
	await message.answer(arab_data)

#arab message
@dp.callback_query_handler(text="arab")
async def to_arabe(call:CallbackQuery):
	tarjima =tr.translate(t, dest='ar')
	await call.message.answer(f"Your result: \n{tarjima.text}", reply_markup=time_arab)
	await call.message.delete()


#russian datetime
@dp.message_handler(text='🇷🇺  Time in Moscow  🕔')
async def time_ruse(message: types.Message):
	time = pytz.timezone('Europe/Moscow')
	russian_time =datetime.datetime.now(time)
	rus_time =russian_time.strftime("%I:%M:%S %p")
	await message.answer(rus_time)

@dp.message_handler(text="🇷🇺  Data in Moscow 📅")
async def data_ruse(message: types.Message):
	time = pytz.timezone('Europe/Moscow')
	russian_data =datetime.datetime.now(time)
	rus_data =russian_data.strftime("%A %d %B %Y")
	await message.answer(rus_data)

#rus message
@dp.callback_query_handler(text="rus")
async def to_ruse(call:CallbackQuery):
	tarjima =tr.translate(t, dest='ru')
	await call.message.answer(f"Your result: \n{tarjima.text}", reply_markup=time_rus)
	await call.message.delete()



#turkish datetime
@dp.message_handler(text='🇹🇷  Time in Istanbul  🕔')
async def time_turke(message: types.Message):
	time = pytz.timezone('Europe/Istanbul')
	turkish_time =datetime.datetime.now(time)
	turk_time =turkish_time.strftime("%I:%M:%S %p")
	await message.answer(turk_time)

@dp.message_handler(text="🇹🇷  Data in Istanbul  📅")
async def data_turke(message: types.Message):
	time = pytz.timezone('Europe/Istanbul')
	turkish_data =datetime.datetime.now(time)
	turk_data =turkish_data.strftime("%A %d %B %Y")
	await message.answer(turk_data)

#turk message
@dp.callback_query_handler(text="turk")
async def to_turke(call:CallbackQuery):
	tarjima =tr.translate(t, dest='tr')
	await call.message.answer(f"Your result: \n{tarjima.text}", reply_markup=time_turk)
	await call.message.delete()


#japanise datetime
@dp.message_handler(text='🇯🇵  Time in Tokio  🕔')
async def time_japane(message: types.Message):
	time = pytz.timezone('Asia/Tokyo')
	japanise_time =datetime.datetime.now(time)
	japan_time =japanise_time.strftime("%I:%M:%S %p")
	await message.answer(japan_time)

@dp.message_handler(text="🇯🇵  Data in Tokio  📅")
async def data_japane(message: types.Message):
	time = pytz.timezone('Asia/Tokyo')
	japanise_data =datetime.datetime.now(time)
	japan_data =japanise_data.strftime("%A %d %B %Y")
	await message.answer(japan_data)

#japan message
@dp.callback_query_handler(text="japan")
async def to_japane(call:CallbackQuery):
	tarjima =tr.translate(t, dest='ja')
	await call.message.answer(f"Your result: \n{tarjima.text}", reply_markup=time_japan)
	await call.message.delete()


@dp.message_handler()
async def echo(message: types.Message):
	global t
	t =message.text
	await message.answer("Choose the language: \n\nВыберите язык:", reply_markup=lang)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)