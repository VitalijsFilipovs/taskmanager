Task Manager - Django проект для управления задачами и подзадачами через админ-панель.

Описание:
Task Manager — это учебный проект, выполненный в рамках курса Python Advanced. В проекте реализованы следующие функции:
- Модель Task (Задача)
- Модель SubTask (Подзадача)
- Инлайн-форма SubTask в Task (возможность добавлять подзадачи прямо при создании задачи)
- Сокращённый вывод длинных названий задач в списке (до 10 символов + "...")
- Собственный Admin Action для массовой установки статуса "Done" у подзадач

Установка:
1. Клонируйте репозиторий:
   git clone https://github.com/VitalijsFilipovs/taskmanager.git
   cd taskmanager

2. Активируйте виртуальное окружение (если ещё не активно):
   .\.venv\Scripts\activate (для Windows)
   source .venv/bin/activate (для macOS/Linux)

3. Установите зависимости:
   pip install -r requirements.txt (если есть файл)

4. Примените миграции:
   python manage.py migrate

5. Создайте суперпользователя:
   python manage.py createsuperuser

6. Запустите сервер:
   python manage.py runserver

7. Откройте сайт:
   http://127.0.0.1:8000/admin/

Возможности:
- Создание задач с вложенными подзадачами
- Список задач с укороченными названиями
- Массовое завершение подзадач через Admin Action

Автор: Vitalijs Filipovs
GitHub: https://github.com/VitalijsFilipovs/taskmanager
