from flask import Flask, render_template, request, redirect, url_for, session
import importlib

app = Flask(__name__)
app.secret_key = 'ny-game-secret-key-2025'

# Список заданий
# Все новые задания добавлять сюда, соблюдая нумерацию, так как след. задание должно иметь id на 1 больше
TASKS = {
    1: {"title": "Перезагрузка ядра", "module": "rounds.Kernel_Reload", "task_id": 1},
    2: {"title": "Восстановление RAM", "module": "rounds.RAM_Restore", "task_id": 2},
    # Третье задание удалено, не прошло проверку на испытуемых))
    # 3: {"title": "Дефрагментация диска", "module": "rounds.Disk_defragmentation", "task_id": 3},
    3: {"title": "Восстановление страницы данных", "module": "rounds.Data_regeneration", "task_id": 3},
    4: {"title": "Восстановление индекса", "module": "rounds.Index_restore", "task_id": 4},
    5: {"title": "Распределение потоков", "module": "rounds.Thread_split", "task_id": 5},
    6: {"title": "Кэширование запросов", "module": "rounds.Query_cache", "task_id": 6},
}

def can_access_task(task_id):
    """Проверяет, можно ли открыть задание: первое доступно всегда, остальные — только после предыдущего."""
    if task_id == 1:
        return True
    completed = session.get('completed_tasks', [])
    return (task_id - 1) in completed

# Главная страница
@app.route("/")
def index():
    return render_template("start.html", tasks=TASKS)

# Страница конкретного задания
@app.route("/task/<int:task_id>", methods=["GET", "POST"])
def task(task_id):
    if task_id not in TASKS:
        return "Задание не найдено", 404

    if not can_access_task(task_id):
        # Находим последнее доступное задание и редиректим туда
        completed = session.get('completed_tasks', [])
        next_task_id = max(completed) + 1 if completed else 1
        return redirect(url_for("task", task_id=next_task_id))

    task_info = TASKS[task_id]
    module = importlib.import_module(task_info["module"])

    # Получаем описание и другие параметры из модуля
    task_desc = getattr(module, "task_desc", "Описание отсутствует.")
    success_msg = getattr(module, "success_message", "Молодцы! Готовы перейти к следующему заданию?")
    error_msg = getattr(module, "error_message", "Неверный ответ, попробуйте ещё раз!")
    task_table = getattr(module, "task_table", None)

    # Проверяем ответ
    if request.method == "POST":
        user_answer = request.form["answer"]
        if module.check_answer(user_answer):
            completed = session.get('completed_tasks', [])
            if task_id not in completed:
                completed.append(task_id)
                session['completed_tasks'] = completed
            return redirect(url_for("success", task_id=task_id))
        else:
            return render_template("task.html", task=task_info, description=task_desc, error=error_msg, task_table=task_table)

    return render_template("task.html", task=task_info, description=task_desc, task_table=task_table)

# Страница успеха
@app.route("/success/<int:task_id>")
def success(task_id):
    task_info = TASKS.get(task_id)
    if not task_info:
        return "Задание не найдено", 404

    # Доступна только если задание было пройдено
    completed = session.get('completed_tasks', [])
    if task_id not in completed:
        return redirect(url_for("task", task_id=task_id))

    module = importlib.import_module(task_info["module"])
    success_msg = getattr(module, "success_message", "Молодцы! Готовы перейти к следующему заданию?")
    button_text = getattr(module, "button_text", "Следующее задание")
    return render_template("success.html", task=task_info, tasks=TASKS, success_msg=success_msg, button_txt=button_text)

# Страница прощание
@app.route("/happyend")
def happyend():
    # Доступна только после прохождения последнего задания
    last_task_id = max(TASKS.keys())
    completed = session.get('completed_tasks', [])
    if last_task_id not in completed:
        return redirect(url_for("task", task_id=last_task_id))
    return render_template("happyend.html")

if __name__ == "__main__":
    app.run(debug=True)
