def get_page_title(view_name):
    menu = [
        {'title': 'Главная страница', 'view_name': 'main'},
        {'title': 'Посмотреть все задачи', 'view_name': 'all_tasks'},
        {'title': 'Создать новую задачу', 'view_name': 'create_task'},
        {'title': 'Редактор задач', 'view_name': 'edit_task'},
        {'title': 'Просмотр задачи', 'view_name': 'single_task'},
    ]
    for item in menu:
        if item['view_name'] == view_name:
            return item['title']
    return 'PingMe'
