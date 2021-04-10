from typing import Union

from aiogram.types import ParseMode # форматирование 
from aiogram.utils import executor #служба
import aiogram.utils.markdown as fmt
from aiogram import Bot,types, Dispatcher
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.dispatcher.filters import Text #  фильтр текста

# for keyboards import make_callbacK_data, main_menu_kb,list_subcategories_kb
from .keyboards import main_menu_callback_data, main_menu_kb, \
    list_subcategories_kb, persona_arial

async def start_cmd(message: Union[types.Message, types.CallbackQuery], **kwargs):
        print("Start")
        messate_text = fmt.text(
        fmt.bold("""
            Приветствую тебя, пользователь 
            Тут я сам пытаюсь немного наворотить эту хуиту
            Надеюсь что из этого что-то выйдет
        """),
        sep='\n' 
        )

        markup = await main_menu_kb()
#не до конца понмаю в чем сут этих проверок, но вроде в возвращение назад
        if isinstance(message, types.Message):
            await message.reply(
                text=messate_text,
                parse_mode=ParseMode.MARKDOWN,
                reply=False,
                reply_markup=markup
        )
        elif isinstance(message, types.CallbackQuery):
            call = message
            await call.message.edit_text(
                text=messate_text,
                parse_mode=ParseMode.MARKDOWN,
                reply_markup=markup
        )

# это уже вызов клавы второго уровня        
async def sub_categories(
    call: types.CallbackQuery,
    main_cat,
    **kwargs
):
    messate_text = '2 level'
    markup = await list_subcategories_kb()
    await call.message.edit_text(
        text=messate_text,
        parse_mode=ParseMode.MARKDOWN,
        reply_markup=markup,
    )
#функция, открывающаяся при выборе личного кабинета
async def sub_persona(
    call:types.CallbackQuery,
    **kwargs
):
    messate_text = '2 level'
    markup = await persona_arial()
    await call.message.edit_text(
        text=messate_text,
        parse_mode=ParseMode.MARKDOWN,
        reply_markup=markup,
    )

#вывод почти пресональной url
async def out_url (
    call:types.CallbackQuery,
    **kwargs
    ):
    messate_text = 'http://t.me/mementologs_bot'
    await call.message.edit_text(
        text=messate_text,
        parse_mode=ParseMode.MARKDOWN,
    )

#основная функция навигации по сложной клавиатуре
async def navigate(
    call: types.callback_query,
    callback_data: dict
):
    #вводим значения из бд
    level           = callback_data.get('level')
    main_cat        = callback_data.get('main_cat')
    sub_cat         = callback_data.get('sub_cat')
    tipe            = callback_data.get("tipe")
    macker          = callback_data.get("macker")
    #задаем уровень. он требуется для перемещения по многоуровнему меню 
    print(tipe)
    if tipe == '0':
        levels = {
            '0': start_cmd,
            '1': sub_categories
        }
    elif tipe == '1':
        if macker == '1':
            levels ={
                '2': out_url
            }
        levels = {
            "0": start_cmd,
            '1': sub_persona
        }
    #передаем в переменную функцию - нужного меню на нужном этапе 
    current_level_function = levels[level]
    
    #запуск выбранной функции
    await current_level_function(
        call,
        main_cat=main_cat,
        sub_cat=sub_cat
    )

# основная функция, принимающая нажатия 
def main_menu(dp:Dispatcher):
    #запускает вывод первичного сообщения 
    dp.register_message_handler(start_cmd, CommandStart())
    #запускает сложное меню 
    dp.register_callback_query_handler(navigate, main_menu_callback_data.filter())