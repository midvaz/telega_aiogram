from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData
#импорт функций по выгрузке бд
from .db_worker import get_all_cat, get_all_sub_cat
#штука необходимая для передавание по функциям походу 

main_menu_callback_data = CallbackData('main_menu', 'level','tipe','macker', 'main_cat', 'sub_cat')

def make_callbacK_data(
    level, 
    tipe,
    macker = 0, #если этот параметр равен особому числу, то запуск спец. сценариев
    main_cat = 0,
    sub_cat = 0
):
    return main_menu_callback_data.new(
        level = level,
        tipe = tipe,
        macker = macker,
        main_cat = main_cat,
        sub_cat = sub_cat
    )

async def main_menu_kb():
     
    CURR_LEVEL = 0 
    TIPE_KB = 0
    MARK = 0
    #контейнер клавиатуры

    categories = get_all_cat()

    markup = InlineKeyboardMarkup(row_width=2)
    for item in categories:
        markup.add(
                InlineKeyboardButton(
                text=item['Name'],
                callback_data=make_callbacK_data(
                    level=CURR_LEVEL+1,
                    tipe = TIPE_KB, 
                    macker = MARK,
                    main_cat=item['id']
                )
            )
        )
    
    markup.add(
        InlineKeyboardButton(
            text = "Личный кабинет",
            callback_data=make_callbacK_data(
                level=CURR_LEVEL+1,
                tipe = TIPE_KB + 1, 
                # macker = MARK
            )
        )
    )
    
    markup.add(
            InlineKeyboardButton(
                text = "Справка",
                url="https://www.google.com/webhp?hl=ru&sa=X&ved=0ahUKEwjX2b2zo-zvAhVshosKHcBTDwkQPAgI"
            )
    )
    
    markup.insert(
            InlineKeyboardButton(
                text = "Помощь",
                url="https://t.me/Innkeeper_with_ei_bot"
            )
    )
    
    return markup

#клава второго уровня
async def list_subcategories_kb(main_cut_id):
    CURR_LEVEL = 1
    TIPE_KB = 0
    # MARK = 0
    markup = InlineKeyboardMarkup(row_width=1)

    sub_categories = get_all_sub_cat(main_cat_id=main_cut_id)

    for item in sub_categories:
        markup.insert(
            InlineKeyboardButton(
                text=item['Name'],
                callback_data=make_callbacK_data(
                    level=CURR_LEVEL+1,
                    tipe = TIPE_KB,
                    # macker = MARK,
                    main_cat=main_cut_id,
                    sub_cat=item['id']
                )
            )
        )

    markup.insert(
        InlineKeyboardButton(
            text='BACK',
            callback_data=make_callbacK_data(
                level=CURR_LEVEL-1,
                tipe = TIPE_KB ,
                # macker = MARK,
                main_cat=main_cut_id
            )
        )
    )

async def persona_arial():
    CURR_LEVEL = 1
    TIPE_KB = 1
    # MARK = 0
    markup = InlineKeyboardMarkup(row_width=1)
    
    markup.add(
        InlineKeyboardButton(
            text='Моя реф ссылка',
            # url = "https://t.me/Test_ghbsdhgbh_bot"
            callback_data=make_callbacK_data(
                tipe = TIPE_KB,
                level=CURR_LEVEL + 1,
                macker = 1

            )
        )
    )
    markup.add(
        InlineKeyboardButton(
            text='Пополнить баланс',
            callback_data=make_callbacK_data(
                level=CURR_LEVEL + 1,
                tipe = TIPE_KB,
                # macker = MARK,
            )
        )
    )
    markup.add(
        InlineKeyboardButton(
            text='История покупок',
            callback_data=make_callbacK_data(
                level=CURR_LEVEL + 1,
                tipe = TIPE_KB,
                # macker = MARK,
            )
        )
    )


    markup.add(
        InlineKeyboardButton(
            text='Замена товара',
            url="https://t.me/Innkeeper_with_ei_bot",
            callback_data=make_callbacK_data(
                level=CURR_LEVEL + 1,
                tipe = TIPE_KB,
                # macker = MARK,
            )
        )
    )
    markup.insert(
        InlineKeyboardButton(
            text='BACK',
            callback_data=make_callbacK_data(
                level=CURR_LEVEL-1,
                tipe = TIPE_KB,
                # macker = MARK, 
            )
        )
    )

    return markup 