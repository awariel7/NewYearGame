from flask import Flask, render_template, request, redirect, url_for
import importlib

app = Flask(__name__)

# Список заданий
TASKS = {
    1: {"title": "Перезагрузка ядра", "module": "Rounds.Kernel_Reload", "task_id": 1},
    2: {"title": "Восстановление RAM", "module": "Rounds.RAM_Restore", "task_id": 2},
    3: {"title": "Дефрагментация диска", "module": "Rounds.Disk_defragmentation", "task_id": 3},
    4: {"title": "Восстановление страницы данных", "module": "Rounds.Data_regeneration", "task_id": 4},
    5: {"title": "Восстановление индекса", "module": "Rounds.Index_restore", "task_id": 5},
    6: {"title": "Распределение потоков", "module": "Rounds.Thread_split", "task_id": 6},
    7: {"title": "Кэширование запросов", "module": "Rounds.Query_cache", "task_id": 7},
}

# Главная страница
@app.route("/")
def index():
    return render_template("index.html", tasks=TASKS)

# Страница конкретного задания
@app.route("/task/<int:task_id>", methods=["GET", "POST"])
def task(task_id):
    if task_id not in TASKS:
        return "Задание не найдено", 404

    task_info = TASKS[task_id]
    module = importlib.import_module(task_info["module"])

    # Получаем описание из модуля
    task_desc = getattr(module, "task_desc", "Описание отсутствует.")
    success_msg = getattr(module, "success_message", "Молодцы! Готовы перейти к следующему заданию?")
    error_msg = getattr(module, "error_message", "Неверный ответ, попробуйте ещё раз!")

    if request.method == "POST":
        user_answer = request.form["answer"]
        if module.check_answer(user_answer):
            return redirect(url_for("success", task_id=task_id))
        else:
            return render_template("task.html", task=task_info, description=task_desc, error=error_msg)

    return render_template("task.html", task=task_info, description=task_desc)

# Страница успеха
@app.route("/success/<int:task_id>")
def success(task_id):
    task_info = TASKS.get(task_id)
    module = importlib.import_module(task_info["module"])
    success_msg = getattr(module, "success_message", "Молодцы! Готовы перейти к следующему заданию?")
    button_text = getattr(module, "button_text", "Следующее задание")
    if not task_info:
        return "Задание не найдено", 404
    return render_template("success.html", task=task_info, tasks=TASKS, success_msg=success_msg, button_txt=button_text)


# Страница прощание
@app.route("/happyend")
def happyend():
    return render_template("happyend.html")

if __name__ == "__main__":
    app.run(debug=True)