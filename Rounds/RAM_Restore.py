Moroz_pass = 'novogodnie_podarki_2025'

RAM_list = ['0x' + str(i) for i in range(1, len(Moroz_pass) + 1)]
RAM_data = []

for s in Moroz_pass:
    info = ''
    if s in "oa0":
        RAM_data.append('ERROR')
    else:
        RAM_data.append(str(ord(s)))
address = ' '.join(RAM_list)
RAM_data_s = ' '.join(RAM_data)
task_desc = """
Cистема загрузилась! Так...<br>
Так...<br>
О, нет, обнаружены повреждения в оперативной памяти! Некоторое количество блоков данных утрачено, а значит и пароль к моей базе!<br>
Всё что осталось в ячейках памяти - ASCII коды символов пароля, да и то не все!<br>
Помогите мне восстановить пароль, переведите недостающие символы в ASCII код и <b>пришлите мне их ASCII-коды через пробел в порядке появления в пароле</b>.<br>
Если один символ упоминается несколько раз, то вы должны прислать мне его <b>только один раз</b>.<br>
А я пока проверю целостность своего жёсткого диска..<br>
<br>
Адреса памяти:\n""" + address + "\nДанные:\n" + RAM_data_s

error_message = 'Не подходит...Есть другие варианты?'
success_message = 'Подходит!'
button_text = 'Восстановим бэкап базы'

def check_answer(answer):
    correct_input = '111 97 48'
    return answer.strip().lower() == correct_input