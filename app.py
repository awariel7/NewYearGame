from flask import Flask, render_template, request, redirect, url_for
import importlib

app = Flask(__name__)

# Список заданий
TASKS = {
    1: {"title": "Перезагрузка ядра", "module": "Rounds.Kernel_Reload"},
    2: {"title": "Восстановление RAM", "module": "Rounds.RAM_Restore"},
    3: {"title": "Дефрагментация диска", "module": "Rounds.Disk_defragmentation"},
    4: {"title": "Регенерация данных", "module": "Rounds.Data_regeneration"},
    5: {"title": "Восстановление индекса", "module": "Rounds.Index_restore"},
    6: {"title": "Распределение потоков", "module": "Rounds.Thread_split"},
    7: {"title": "Кэширование запросов", "module": "Rounds.Query_cache"},
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

    if request.method == "POST":
        user_answer = request.form["answer"]
        if module.check_answer(user_answer):
            return redirect(url_for("success", task_id=task_id))
        else:
            return render_template("task.html", task=task_info, description=task_desc, error="Неверный ответ, попробуйте ещё раз!")

    return render_template("task.html", task=task_info, description=task_desc)

# Страница успеха
@app.route("/success/<int:task_id>")
def success(task_id):
    return render_template("success.html", task=TASKS[task_id])

if __name__ == "__main__":
    app.run(debug=True)