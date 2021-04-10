from tgbot.data_base import connect
#выгрузка бд, категории товаров
def get_all_cat():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute(
        '''
        SELECT * 
        FROM main_cat
        '''
    )
    result = cursor.fetchall()
    conn.close()

    return result
#выгрузка бд товаров

def get_all_sub_cat(main_cat_id):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute(
        '''
        SELECT * 
        FROM sub_cat
        WHERE main_cat_id = %s
        ''' , main_cat_id
    )
    
    result = cursor.fetchall()
    conn.close()
    
    return result