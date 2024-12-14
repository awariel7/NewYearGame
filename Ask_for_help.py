import threading
import time
import random
# games
import Rounds.Kernel_Reload
import Rounds.RAM_Restore
import Rounds.Disk_defragmentation
import Rounds.Data_regeneration
import Rounds.Index_restore
import Rounds.Thread_split
import Rounds.Query_cache
#Final
import Happy_End


Moroz_phrases = [
    "Эй! Есть тут кто? Это Дед Мороз, ответьте на это сообщение!"
    , "Это Дед Мороз, мне нужна ваша помощь! Напишите мне в чат"
    , "Алло! Меня кто-нибудь слышит? Этот Дед Мороз, напишите мне"
    , "Привет! Это Дед Мороз и мне нужна срочная помощь! Вы же айтишники?"
    , "Кто-нибудь! Отзовись! Дед Мороз в беде!"
]
global user_input
user_input = None
stop_thread = False

def get_input():
    """Функция для чтения ввода в другом потоке"""
    global user_input
    user_input = input()
def input_with_timeout(timeout):
    input_thread = threading.Thread(target=get_input)
    input_thread.start()

    start_time = time.time()
    while time.time() - start_time < timeout:
        if user_input is not None:  # Проверяем, ввёл ли пользователь данные
            break
        time.sleep(0.1)  # Небольшая задержка для снижения нагрузки на процессор

    if user_input is None:  # Если пользователь ничего не ввёл
        print("\nВремя вышло!")
        input_thread.join(0)  # Убедимся, что поток завершился (если ещё работает)
        return None
    return user_input

while user_input == '':
    print(random.choice(Moroz_phrases))
    input_with_timeout(10)
    if user_input is not None:
        break
    print("Попробуем ещё раз!")

print("Ну наконец-то! Новый год под угрозой!")
info_message = ("Дорогие коллеги-айтишники,\n\
На днях мы наконец завершили импортозамещение и перевели нашу Santa Gift Management System (SGMS) на отечественную базу данных — ОленьДБ.\n\
Всё шло как по маслу, пока я не решил внести последние корректировки в список подарков. Уверенно ввёл SQL-запрос,\n\
нажал Enter… и вся система упала!\n\
Теперь сервер не отвечает, а я застрял с терминалом прямо на своих санях. До Нового года осталось совсем мало времени,\n\
и без вашей помощи я просто не успею поднять систему и восстановить базу данных!\n\
Я подключился к вашему офису, чтобы вы помогли мне с этой задачей. Ваша миссия — восстановить сервер,\n\
исправить базу подарков и настроить доставку подарков детям по всему миру\n\
Вы поможете мне?")
print(info_message)
res = input()

print("Отлично, тогда за работу!")
#1
task_res = Rounds.Kernel_Reload.kernel_reload()
#2
task_res = Rounds.RAM_Restore.RAM_restore()
#3
task_res = Rounds.Disk_defragmentation.disk_defragmentation()
#4
task_res = Rounds.Data_regeneration.data_regeneration()
#5
task_res = Rounds.Index_restore.index_restore()
#6
task_res = Rounds.Thread_split.thread_split()
#7
task_res = Rounds.Query_cache.query_cash()

Happy_End.congratulations()
