from  telebot import TeleBot,types
from functions import adduser
from  btns import buttons
import  functions
bot=TeleBot(token)
@bot.message_handler(commands=["start"])
def start(msg:types.Message):
    adduser(msg.from_user.id)
    bot.send_message(msg.from_user.id,'kalkulatorga xush kelibsiz',reply_markup=buttons)



@bot.callback_query_handler(func=lambda a:a.data)
def cdrest(msg:types.CallbackQuery):
    def sonlar(n):

        functions.changeson(msg.from_user.id, n)
        data = functions.getSon(msg.from_user.id)
        matn = ""
        for i in data:
            matn += i
            try:
                bot.edit_message_text(f"hozirgi holat:\n\n{matn}", msg.from_user.id,
                              msg.message.id, reply_markup=buttons)
            except:
                pass

    def amallar(amal):
        functions.changeamal(msg.from_user.id, amal)
        functions.changebelgi(msg.from_user.id)
        data=functions.getSon(msg.from_user.id)
        matn=""
        for i in data:
            matn+=i
        try:
            bot.edit_message_text(f"hozirgi holat:\n\n{matn}", msg.from_user.id,
                                  msg.message.id, reply_markup=buttons)
        except:
            pass

    match msg.data:
        case "1":
            sonlar(1)
        case "2":
            sonlar(2)
        case "3":
            sonlar(3)
        case "4":
            sonlar(4)
        case "5":
            sonlar(5)
        case "6":
            sonlar(6)
        case "7":
            sonlar(7)
        case "8":
            sonlar(8)
        case "9":
            sonlar(9)
        case "0":
            sonlar(0)
        case "+":
            amallar("+")
        case "*":
            amallar("*")
        case "-":
            amallar("-")
        case "/":
            amallar("/")
        case "RESULT":
            try:
                bot.edit_message_text(f"natija:\n\n {functions.GetRes(msg.from_user.id)}",msg.from_user.id,msg.message.id,
                                  reply_markup=buttons)
            except:
                pass
            #     bot.answer_callback_query(msg.id,"...")
        case 'CLEAR':
             bot.edit_message_text(f"{functions.clear(msg.from_user.id)}", msg.from_user.id, msg.message.id,
                          reply_markup=buttons)




bot.polling()
