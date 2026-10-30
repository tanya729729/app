def normalize_title(title):
    return title.lower().lstrip().rstrip()


def create_task(task_id, title, priority):
    task = {"task_id": task_id, "title": normalize_title(title),"priority": priority, "is_done":False}
    return task

def format_task(task):
    if task["is_done"]==True:
        return f" [{task["task_id"]}] {task["title"]} | приоритет:{task["priority"]} | выполнена"

    return f" [{task["task_id"]}] {task["title"]} | приоритет:{task["priority"]} | не выполнена "

def calculate_study_minutes(durations):
    total=0
    for duration in durations:
        total=total+duration
    return total

first_title = normalize_title("  Повторить функции  ")
first_task = create_task(41, first_title, 2)
first_card = format_task(first_task)
print(first_card)

second_title = normalize_title("  Сверить учебный план  ")
second_task = create_task(42, second_title, 5)
second_card = format_task(second_task)
print(second_card)

study_durations = [25, 35]
study_minutes = calculate_study_minutes(study_durations)
print(study_minutes)


def show_tasks(tasks):
    if len(tasks) == 0:
        print("Список задач пока пуст.")
        return
    for task in tasks:
        print(format_task(task))

def read_title():
    while True:
        raw_title = input("Название задачи: ")
        title = normalize_title(raw_title)
        if title == "":
            print("Название не должно быть пустым.")
            continue
        return title

def read_priority():
    while True:
        raw_priority = input("Приоритет от 1 до 5: ")
        try:
            priority = int(raw_priority)
        except ValueError:
            print("Введите целое число.")
            continue
        if not 1 <= priority <= 5:
            print("Число должно быть от 1 до 5.")
            continue
        return priority

def get_next_id(tasks):
    largest_id = 0
    for task in tasks:
        task_id = task["id"]
        if task_id > largest_id:
            largest_id = task_id
    return largest_id + 1

def add_task(tasks, title, priority):
    task_id = get_next_id(tasks)
    new_task = create_task(task_id, title, priority)
    tasks.append(new_task)
    return new_task

def handle_add(tasks):
    title = read_title()
    priority = read_priority()
    new_task = add_task(tasks, title, priority)
    print(format_task(new_task))


def read_task_id():
    while True:
        raw_value = input('Номер задачи: ')
        try:
            task_id = int(raw_value)
        except ValueError:
            print('Введите целое число')
            continue
        if task_id > 0:
            return task_id
        print('Номер должен быть положительным')

def find_task(tasks, task_id):
    for task in tasks:
        if task['id'] == task_id:
            return task
    return None


def handle_find(tasks):
    task_id = read_task_id()
    task = find_task(tasks, task_id)
    if task is None:
        print('Задача не найдена')
    else:
        print(format_task(task))


def mark_task_done(tasks, task_id):
    task = find_task(tasks, task_id)
    if task is None:
        return False
    task["is_done"] = True
    return True

def handle_done(tasks):
    task_id = read_task_id()
    was_found = mark_task_done(tasks, task_id)
    if was_found:
        print("Задача выполнена")
    else:
        print("Задача не найдена")

def show_menu():
    print()
    print("StudyHub Planner")
    print("add - добавить задачу")
    print("list - показать задачи")
    print("find - найти задачу по id")
    print("done - завершить задачу")
    print("search - искать по названию")
    print("stats - показать статистику")
    print("exit - завершить работу")

def run():
    tasks = []
    while True:
        show_menu()
        command = input("Команда: ").strip().lower()
        if command not in ("add", "list", "find", "done", "search", "stats", "exit"):
            print("Неизвестная команда")
            continue
        if command == "exit":
            print("Работу завершили")
            break
        if command == "add":
            handle_add(tasks)
        elif command == "find":
            handle_find(tasks)
        elif command == "done":
            handle_done(tasks)
        elif command == "search":
            handle_search(tasks)
        elif command == "stats":
            print("Команда пока не подключена.")
        else:
            show_tasks(tasks)


def search_tasks(tasks, query):
    normalized_query = query.strip().lower()
    if normalized_query == "":
        return []

    matches = []
    for task in tasks:
        if normalized_query in task["title"].lower():
            matches.append(task)
    return matches

def handle_search(tasks):
    query = input("Фрагмент названия: ")
    if query.strip() == "":
        print("Введите непустой фрагмент")
        return

    matches = search_tasks(tasks, query)
    if len(matches) == 0:
        print("Совпадений не найдено")
    else:
        show_tasks(matches)


