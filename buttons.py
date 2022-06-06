from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

#Our language button list
#That list appears when you type your word to translate

lang =InlineKeyboardMarkup(
	inline_keyboard=[
		[
		InlineKeyboardButton("English  🇬🇧", callback_data='eng'),
		InlineKeyboardButton("Korean  🇰🇷", callback_data='kor'),
		],
		[
		InlineKeyboardButton("Chinese  🇨🇳", callback_data='chin'),
		InlineKeyboardButton("Hindi 🇮🇳", callback_data='hind'),
		],
		[
		InlineKeyboardButton("Spanish 🇪🇸", callback_data='esp'),
		InlineKeyboardButton("French 🇫🇷", callback_data='frn'),
		],
		[
		InlineKeyboardButton("Arabic 🇸🇦", callback_data='arab'),
		InlineKeyboardButton("Russian 🇷🇺", callback_data='rus'),
		],
		[
		InlineKeyboardButton("Turkish 🇹🇷", callback_data='turk'),
		InlineKeyboardButton("Japanise 🇯🇵", callback_data='japan'),
		],
	],
)

#Button to show the time of the countries

time_eng =ReplyKeyboardMarkup(
	[
		[
		KeyboardButton(text='🇬🇧  Time in London  🕔')
		],
		[
		KeyboardButton(text='🇬🇧  Data in London  📅')
		],
		[
		KeyboardButton(text='⬅️  Back')
		],
	],
	resize_keyboard=True
)

time_kor =ReplyKeyboardMarkup(
	[
		[
		KeyboardButton(text='🇰🇷  Time in Seul  🕔')
		],
		[
		KeyboardButton(text='🇰🇷  Data in Seul  📅')
		],
		[
		KeyboardButton(text='⬅️  Back')
		],
	],
	resize_keyboard=True
)

time_chin =ReplyKeyboardMarkup(
	[
		[
		KeyboardButton(text='🇨🇳  Time in Hong_Kong  🕔')
		],
		[
		KeyboardButton(text='🇨🇳  Data in Hong_Kong  📅')
		],
		[
		KeyboardButton(text='⬅️  Back')
		],
	],
	resize_keyboard=True
)

time_hindi =ReplyKeyboardMarkup(
	[
		[
		KeyboardButton(text='🇮🇳  Time in Idnia  🕔')
		],
		[
		KeyboardButton(text='🇮🇳  Data in India  📅')
		],
		[
		KeyboardButton(text='⬅️  Back')
		],
	],
	resize_keyboard=True
)

time_spain =ReplyKeyboardMarkup(
	[
		[
		KeyboardButton(text='🇪🇸  Time in Madrid  🕔')
		],
		[
		KeyboardButton(text='🇪🇸  Data in Madrid  📅')
		],
		[
		KeyboardButton(text='⬅️  Back')
		],
	],
	resize_keyboard=True
)

time_frn =ReplyKeyboardMarkup(
	[
		[
		KeyboardButton(text='🇫🇷  Time in Paris  🕔')
		],
		[
		KeyboardButton(text='🇫🇷  Data in Paris  📅')
		],
		[
		KeyboardButton(text='⬅️  Back')
		],
	],
	resize_keyboard=True
)

time_arab =ReplyKeyboardMarkup(
	[
		[
		KeyboardButton(text='🇦🇪  Time in Dubai  🕔')
		],
		[
		KeyboardButton(text='🇦🇪  Data in Dubai  📅')
		],
		[
		KeyboardButton(text='⬅️  Back')
		],
	],
	resize_keyboard=True
)

time_rus =ReplyKeyboardMarkup(
	[
		[
		KeyboardButton(text='🇷🇺  Time in Moscow  🕔')
		],
		[
		KeyboardButton(text='🇷🇺  Data in Moscow 📅')
		],
		[
		KeyboardButton(text='⬅️  Back')
		],
	],
	resize_keyboard=True
)

time_turk =ReplyKeyboardMarkup(
	[
		[
		KeyboardButton(text='🇹🇷  Time in Istanbul  🕔')
		],
		[
		KeyboardButton(text='🇹🇷  Data in Istanbul  📅')
		],
		[
		KeyboardButton(text='⬅️  Back')
		],
	],
	resize_keyboard=True
)

time_japan =ReplyKeyboardMarkup(
	[
		[
		KeyboardButton(text='🇯🇵  Time in Tokio  🕔')
		],
		[
		KeyboardButton(text='🇯🇵  Data in Tokio  📅')
		],
		[
		KeyboardButton(text='⬅️  Back')
		],
	],
	resize_keyboard=True
)