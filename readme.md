Задание:
1. Файл test.py в архиве. Запустить файл без ошибок(если выйдет). Подробные инструкции по выполнению внутри файла в каждом задании.
2. Создать в своём репазитории публичный Django проект. Реализовать авторизацию. В системе со старта должен быть пользователь:
    login: "4elovekconstanta@vought.com"
    password: "5uperP@sw00rd"

    На главной странице должна отображаться информация:
    1) Колличестве успешных авторизаций пользователя
    2) Колличество неуспешных 
    3) Процентное соотношение успешных и нет. Так же выделить стиль страницы в зависимости от большего значения

Так же в репазитории создать папку "task_1" куда положить исправленый файл из первого задания Предоставить ссылку на репазиторий. 
Конечно можно исполнение файла "test.py" с выводом результата и через страницу в проекте сделать... Но это уже по сугубо личному стремлению к прекрасному.

##############################################################################

Как запустить проект.
- Первый вариант.
0) Спулить проект. Создать виртуальное окружение и активировать его.
1) Установить зависимости в виртуальное окружение: pip install -r requirements.txt
2) Перейти в корень проекта: cd wiseweb
3) Запустить сервер: python manage.py runserver

- Второй вариант
0) Спулить проект.
1) docker-compose build
2) docker-compose up



