# Сбор новостей с сайта 78.ru
![Black](https://img.shields.io/badge/code%20style-black-black)
 
## Инстукция
Для запуска необходимо:
1. Скопировать содержимое файла `.env.sample` в файл `.env`. Для Linux `cp .env.sample .env`
2. Запустить `docker-compose up --build`

## Демонстрация
Проект доступен по [ссылке](http://77.246.105.150/admin).
Логин - admin, пароль - 123qwe.

## Описание проекта
Проект состоит из  БД PostgreSQL, Nginx, парсера Scrapy + Playwright и панели администратора Django.

Django создает таблицы для хранения постов в начальной миграции. Таблицы, необходимые для работы Django находятся в схеме public, для хранения постов создается схема `content`:

![image](https://github.com/ian-mn/test-russian-news-parser/assets/136719108/94908378-023c-4c14-9b6b-93abeeb764c3)

`post_id` хранится как [UUID](https://dba.stackexchange.com/questions/115271/what-is-the-optimal-data-type-for-an-md5-field), дата публикации поста как timestamp with timezone.

Панель администратора расположена по ссылке `127.0.0.1/admin`:
![image](https://github.com/ian-mn/test-russian-news-parser/assets/136719108/d6a633c6-b37d-490d-885a-3de91e749460)

Можно создавать новые посты, изменять/удалять существующие:
![image](https://github.com/ian-mn/test-russian-news-parser/assets/136719108/1f87ef4a-c5ee-44f8-810e-7f5b312f2bd8)

Для работы с полем `post_text` используется [ckeditor](https://github.com/django-ckeditor/django-ckeditor).

При добавлении/изменении `post_url` поле `post_id` автоматически пересчитывается:
![image](https://github.com/ian-mn/test-russian-news-parser/assets/136719108/d749611d-9261-4382-aeab-17d4c7c8097c)

Панель администратора локализована на русский язык.

Можно выделить несколько постов и выгрузить данные в формате JSON (Действие -> Экспортировать Выбранные -> Выполнить):
![image](https://github.com/ian-mn/test-russian-news-parser/assets/136719108/80c9b7c5-6641-411d-a97e-e1d1c4b81e56)
![image](https://github.com/ian-mn/test-russian-news-parser/assets/136719108/58518fa1-c9ea-4c63-b15e-bb34ebfd95ce)

Статические файлы для снижения нагрузки отдаются через Nginx.

Парсер раз в 15 минут собирает информацию о новых постах, сохраняет их в БД. 
Периодичность парсинга можно настроить через переменную `parsing_period_minutes` в файле `.env`.

В БД сохраняются только новые посты. Проверка происходит по полю `post_id` (MD5 hash от ссылки на новость).

Парсер так же сохраняет данные в JSON-файлы. Сбор информации в файлы можно отключить через переменную окружения `export_to_json=False`. Переменная `export_path=output/` указывает на путь сохранения.
Пример JSON-файлов:
![image](https://github.com/ian-mn/test-russian-news-parser/assets/136719108/ede7b53c-7f6c-4873-a3e0-71ee68242b8f)
![image](https://github.com/ian-mn/test-russian-news-parser/assets/136719108/16c9b478-e3dd-4c63-b0f0-930d496863cc)

В JSON-файлах даты хранятся как UNIX timestamp.
В JSON-файл добавляются все посты, даже если они уже ранее были собраны в БД.

При сборе информации о посте для валидации данных используется Pydantic:
![image](https://github.com/ian-mn/test-russian-news-parser/assets/136719108/8111ae10-5f01-4687-ae52-f0d9f135a3d1)

Работа с БД идет через [automap](https://docs.sqlalchemy.org/en/20/orm/extensions/automap.html) ORM SQLalchemy. 

Вся работа с зависимостями ведется через [poetry](https://python-poetry.org/).

Настроен линтер Black через GitHub Actions. 




