#                       Библеотека четное нечетное число
# from isOdd import isOdd
# print(isOdd(1))
# print(isOdd(2))




#                       Библиотека имитация загрузки
# from progress.bar import Bar
# import time
# bar = Bar('Processing', max=20)
# for i in range(20):
#     time.sleep(1)
#     bar.next()
# bar.finish()




#                       Библиотека смайлик палец вверх
# import emoji
# print(emoji.emojize('Python is :thumbs_up:'))




#                       Библиотека вывод графика в отдельное окно
# import matplotlib.pyplot as plt
# import numpy as np
# list = [1,9,1,9,1]
# plt.plot(list)
# plt.show()





#                       Телеграм БОТ 
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import bot_commands as bc
app = ApplicationBuilder().token("5477440053:AAH0leJS4r4NWCioAa2_JoU95TpyLMT-mWQ").build()
app.add_handler(CommandHandler("hi", bc.hi_command))
app.add_handler(CommandHandler("time", bc.time_command))
app.add_handler(CommandHandler("help", bc.help_command))
app.add_handler(CommandHandler("sum", bc.sum_command))
app.add_handler(CommandHandler("difference", bc.difference_command))
app.add_handler(CommandHandler("multiply", bc.multiply_command))
app.add_handler(CommandHandler("division", bc.division_command))
app.run_polling()