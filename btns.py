from telebot import  types
buttons=types.InlineKeyboardMarkup(row_width=3)
buttons.add(types.InlineKeyboardButton(text='1',callback_data='1'),
            types.InlineKeyboardButton(text='2',callback_data='2'),
            types.InlineKeyboardButton(text='3',callback_data='3'),
            types.InlineKeyboardButton(text='4',callback_data='4'),
            types.InlineKeyboardButton(text='5', callback_data='5'),
            types.InlineKeyboardButton(text='6',callback_data='6'),
            types.InlineKeyboardButton(text='7',callback_data='7'),
            types.InlineKeyboardButton(text='8',callback_data='8'),
            types.InlineKeyboardButton(text='9',callback_data='9'),
            types.InlineKeyboardButton(text='0',callback_data='0'),
            types.InlineKeyboardButton(text='+',callback_data='+'),
            types.InlineKeyboardButton(text='*',callback_data='*'),
            types.InlineKeyboardButton(text='/',callback_data='/'),
            types.InlineKeyboardButton(text='-',callback_data='-'),
            types.InlineKeyboardButton(text='C',callback_data='CLEAR'),
            types.InlineKeyboardButton(text='=',callback_data='RESULT'),
            )




