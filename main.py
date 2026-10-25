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
        print("Список задач пуст.")
    else:
        print("Полный показ задач появится позже.")

def show_menu():
    print("Команды: add, list, find, done, search, stats, exit")

def run():
    tasks = []
    while True:
        show_menu()
        command = input("Команда: ").strip().lower()
        if command == "list":
            show_tasks(tasks)
        elif command == "exit":
            break
        elif command in {"add", "find", "done", "search", "stats"}:
            print("Команда пока не подключена.")
        else:
            print("Неизвестная команда.")

run()