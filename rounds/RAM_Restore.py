Moroz_pass = 'noviy_god_2025'

RAM_list = ['0x' + str(i) for i in range(1, len(Moroz_pass) + 1)]
RAM_data = []
Skipped_data = set()

for s in Moroz_pass:
    info = ''
    if s in "oa0g":
        RAM_data.append('ERROR')
        Skipped_data.add(str(ord(s)))
    else:
        RAM_data.append(str(ord(s)))
address = ' '.join(RAM_list)
RAM_data_s = ' '.join(RAM_data)


task_table = '<table style="margin: 1px auto;"><tr>'
for i in range(len(RAM_list)):
    task_table += ('<th>' + RAM_list[i] + '</th>')
task_table += '</tr><tr>'
for i in range(len(RAM_data)):
    task_table += ('<td>' + RAM_data[i] + '</td>')
task_table += '</tr></table>'

task_desc = """
Cистема загрузилась! Так...<br>
Так...<br>
О, нет, обнаружены повреждения в оперативной памяти! Некоторое количество блоков данных утрачено, а значит и пароль к моей базе!<br>
Всё что осталось в ячейках памяти - ASCII коды символов пароля, да и то не все!<br>
Помогите мне восстановить пароль, переведите недостающие символы в ASCII код и <b>пришлите мне их ASCII-коды через пробел в порядке появления в пароле</b>.<br>
Если один символ упоминается несколько раз, то вы должны прислать мне его <b>только один раз</b> без лидирующих нулей.<br>
А я пока проверю целостность своего жёсткого диска..<br>
<br>
Адреса памяти с оставшимися данными:"""

error_message = 'Не подходит...Есть другие варианты?'
success_message = 'Подходит!'
button_text = 'Восстановим бэкап базы'
print(' '.join(list(Skipped_data)))
def check_answer(answer):
    correct_input = '111 103 48' #' '.join(list(Skipped_data))
    return answer.strip().lower() == correct_input