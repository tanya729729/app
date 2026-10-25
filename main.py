def normalize_title(title):
    return title.lower().lstrip().rstrip()


def create_task(task_id, title, priority):
    task = {"task_id": task_id, "title": normalize_title(title),"priority": priority, "is_done":False}
    return task

def format_task(task):
    if task["is_done"]==True:
        return f" [{task["task_id"]}] {task["title"]} | приоритет:{task["priority"]} | выполнена"

    return f" [{task["task_id"]}] {task["title"]} | приоритет:{task["priority"]} | не выполнена "


