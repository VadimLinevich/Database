# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from AdminWindow import AdminWindow
from CRUDWindow import CRUDWindow
from Enter import Enter
from ModerWindow import ModerWindow
from UserWindow import UserWindow

user_review_CRUD = CRUDWindow('Reviews',
                          select_columns=['iduser', 'idgame', 'content'],
                          delete_columns=['idgame'],
                          insert_columns=['idgame', 'content'],
                          update_columns=['content', 'idgame'])

user_rating_CRUD = CRUDWindow('ratings',
                          select_columns=['iduser', 'idgame', 'grade'],
                          delete_columns=['idgame'],
                          insert_columns=['idgame', 'grade'],
                          update_columns=['grade', 'idgame'])

review_CRUD = CRUDWindow('Reviews',
                          select_columns=['iduser', 'idgame', 'content'],
                          delete_columns=['iduser', 'idgame'],
                          insert_columns=['iduser', 'idgame', 'content'])

rating_CRUD = CRUDWindow('ratings',
                          select_columns=['iduser', 'idgame', 'grade'],
                          delete_columns=['iduser', 'idgame'],
                          insert_columns=['iduser', 'idgame', 'grade'])

genre_CRUD = CRUDWindow('genres',
                        select_columns=['id', 'name'],
                        delete_columns=['id'],
                        insert_columns=['name'],
                        update_columns=['name', 'id'])

gamegenre_CRUD = CRUDWindow('gamegenre',
                        select_columns=['idgenre', 'idgame'],
                        delete_columns=['idgenre', 'idgame'],
                        insert_columns=['idgenre', 'idgame'])

gamecompany_CRUD = CRUDWindow('gamecompany',
                        select_columns=['idcompany', 'idgame'],
                        delete_columns=['idcompany', 'idgame'],
                        insert_columns=['idcompany', 'idgame'])

company_CRUD = CRUDWindow('companies',
                        select_columns=['id', 'name', 'foundation', 'location'],
                        delete_columns=['id'],
                        insert_columns=['name', 'foundation', 'location'],
                        update_columns=['name', 'foundation', 'location', 'id'])

gamedeveloper_CRUD = CRUDWindow('gamedeveloper',
                        select_columns=['iddeveloper', 'idgame'],
                        delete_columns=['iddeveloper', 'idgame'],
                        insert_columns=['iddeveloper', 'idgame'])

developers_CRUD = CRUDWindow('developers',
                        select_columns=['id', 'name', 'age'],
                        delete_columns=['id'],
                        insert_columns=['name', 'age', 'image'],
                        update_columns=['name', 'age', 'image', 'id'])

game_CRUD = CRUDWindow('games',
                        select_columns=['id', 'title', 'description'],
                        delete_columns=['id'],
                        insert_columns=['title', 'poster', 'description', 'year', 'platform', 'agerating', 'mode', 'systemrequirements'],
                        update_columns=['title', 'platform', 'description', 'id'])

user_windows_dict = {'reviews': user_review_CRUD,
                'ratings': user_rating_CRUD
                }

moder_windows_dict = {'reviews': review_CRUD,
                'ratings': rating_CRUD,
                'genres': genre_CRUD,
                'gamegenre': gamegenre_CRUD,
                'gamecompany': gamecompany_CRUD,
                'companies': company_CRUD,
                'gamedeveloper': gamedeveloper_CRUD,
                'developers': developers_CRUD,
                'games': game_CRUD,
                }

if __name__ == '__main__':
    user_window = UserWindow(user_windows_dict)
    moder_window = ModerWindow(moder_windows_dict)
    admin_window = AdminWindow(moder_windows_dict)
    windows_dict = {'user': user_window,
                    'moder': moder_window,
                    'admin': admin_window
                          }
    enter_window = Enter(windows_dict)
    enter_window.run()
